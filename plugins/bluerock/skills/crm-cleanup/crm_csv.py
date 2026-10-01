#!/usr/bin/env python3
"""
crm_csv.py — the exact half of CRM Cleanup and Enrichment.

The agents look things up and make judgment calls. Everything that has to be exact lives
here: reading the export, mapping its columns, the format fixes, the duplicate candidates,
the enrichment cap, and writing the import-ready file. A prompt can be talked out of a
rule; this file cannot, so the rules a builder is promised are enforced here:

  - enrichment never goes past the cap (a fill for a row outside it is rejected)
  - every appended value carries a source URL (a fill without one is rejected)
  - enrichment never overwrites a value the builder already has (it becomes a
    "Needs your call" item instead, applied only if the builder confirms it)
  - the output has the same header, the same rows, in the same order, and every
    changed cell is in the change log (checked by re-reading the file after writing)

stdlib only. Python 3.8+.

Usage:
  python3 crm_csv.py profile <export.csv> --run <folder> [--since YYYY-MM-DD]
                             [--map field=Header ...]
  python3 crm_csv.py apply --run <folder> [--corrections <corrections.json>]

`profile` writes <folder>/profile.json and prints a short JSON summary.
`apply` reads profile.json and the auditor's decisions.json, then writes
<folder>/<name>-cleaned.csv, change-log.md, change-log.html, and applied.json.
"""

import argparse
import csv
import html
import io
import json
import os
import re
import sys
from collections import Counter, OrderedDict
from datetime import datetime

ENRICH_CAP = 24          # rows looked up per run; stated in every output
LOOKUPS_PER_ROW = 3      # the record-enricher's bound; stated beside the cap
BATCH_SIZE = 8           # rows per record-enricher

FIELDS = ["id", "name", "domain", "industry", "employees", "revenue",
          "city", "state", "country", "created"]
ENRICH_FIELDS = ["domain", "industry", "employees", "city", "state", "country"]
FIELD_LABELS = {"id": "record ID", "name": "company name", "domain": "domain / website",
                "industry": "industry", "employees": "employees", "revenue": "annual revenue",
                "city": "city", "state": "state / region", "country": "country",
                "created": "create date"}

ALIASES = OrderedDict([
    ("id", ["record id", "account id", "company id", "organization - id", "organization id",
            "record_id", "account_id", "id"]),
    ("name", ["company name", "account name", "organization - name", "organization name",
              "company", "name"]),
    ("domain", ["company domain name", "domain", "company domain", "website", "website url",
                "company website", "organization - website", "web site", "url"]),
    ("industry", ["industry", "organization - industry"]),
    ("employees", ["number of employees", "employees", "employee count", "no. of employees",
                   "# employees", "organization - number of employees", "headcount",
                   "company size", "size"]),
    ("revenue", ["annual revenue", "revenue", "organization - annual revenue"]),
    ("city", ["city", "billing city", "hq city", "organization - city"]),
    ("state", ["state/region", "billing state/province", "billing state", "state/province",
               "state", "organization - state", "region"]),
    ("country", ["country/region", "billing country", "country", "organization - country"]),
    ("created", ["create date", "created date", "created", "created at", "date created",
                 "creation date", "organization - created", "account created date"]),
])
WEBSITE_STYLE = {"website", "website url", "company website", "organization - website",
                 "web site", "url"}

COUNTRIES = [  # (full, iso2, iso3, other spellings)
    ("United States", "US", "USA", ["u.s.", "u.s.a.", "united states of america", "america"]),
    ("United Kingdom", "GB", "GBR", ["uk", "u.k.", "great britain"]),
    ("Canada", "CA", "CAN", []),
    ("Australia", "AU", "AUS", []),
    ("Germany", "DE", "DEU", ["deutschland"]),
    ("France", "FR", "FRA", []),
    ("India", "IN", "IND", []),
    ("Israel", "IL", "ISR", []),
    ("Ireland", "IE", "IRL", []),
    ("Netherlands", "NL", "NLD", ["the netherlands", "holland"]),
    ("Singapore", "SG", "SGP", []),
    ("Japan", "JP", "JPN", []),
]
STATES = {  # full name -> abbreviation (US, Canada, Australia)
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI",
    "Wyoming": "WY", "District of Columbia": "DC",
    "Ontario": "ON", "Quebec": "QC", "British Columbia": "BC", "Alberta": "AB",
    "Manitoba": "MB", "Saskatchewan": "SK", "Nova Scotia": "NS", "New Brunswick": "NB",
    "New South Wales": "NSW", "Victoria": "VIC", "Queensland": "QLD",
    "Western Australia": "WA_AU", "South Australia": "SA", "Tasmania": "TAS",
}
LEGAL_SUFFIXES = {"inc", "incorporated", "llc", "ltd", "limited", "corp", "corporation", "co",
                  "company", "gmbh", "plc", "sa", "ag", "bv", "pty", "lp", "llp", "srl", "oy"}
DATE_FORMATS = ["%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ",
                "%Y-%m-%d", "%m/%d/%Y %I:%M %p", "%m/%d/%Y %H:%M", "%m/%d/%Y", "%d/%m/%Y",
                "%m/%d/%y", "%Y/%m/%d"]


# ---------- small helpers ----------

def die(msg):
    print(json.dumps({"ok": False, "error": msg}))
    sys.exit(1)


def norm_header(h):
    return re.sub(r"\s+", " ", (h or "").strip().lower())


def collapse(v):
    return re.sub(r"\s+", " ", (v or "").strip())


def norm_domain(v):
    """Bare lowercase domain, or '' if v is not a usable domain."""
    s = (v or "").strip().lower()
    if not s or "@" in s or " " in s:
        return ""
    s = re.sub(r"^[a-z]+://", "", s)
    s = s.split("/")[0].split("?")[0].split("#")[0].split(":")[0].rstrip(".")
    if s.startswith("www."):
        s = s[4:]
    return s if re.match(r"^[a-z0-9-]+(\.[a-z0-9-]+)+$", s) else ""


def parse_number(v):
    """'6,000' -> 6000, '1.7k' -> 1700, '$1.68B' -> 1680000000, '2.8 billion' -> 2800000000.
    Returns None for anything that is not one number (ranges, '10000+', words)."""
    s = (v or "").strip().lower().replace("$", "").replace(",", "").replace(" ", "")
    if not s:
        return None
    m = re.match(r"^(\d+(?:\.\d+)?)(k|thousand|m|mm|mn|million|b|bn|billion)?$", s)
    if not m:
        return None
    mult = {None: 1, "k": 1e3, "thousand": 1e3, "m": 1e6, "mm": 1e6, "mn": 1e6,
            "million": 1e6, "b": 1e9, "bn": 1e9, "billion": 1e9}[m.group(2)]
    n = float(m.group(1)) * mult
    return int(round(n))


def parse_date(v):
    s = (v or "").strip()
    for f in DATE_FORMATS:
        try:
            return datetime.strptime(s, f)
        except ValueError:
            pass
    return None


def name_key(v):
    s = collapse(v).lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    toks = s.split()
    while toks and toks[-1] in LEGAL_SUFFIXES:
        toks.pop()
    return " ".join(toks)


def country_lookup():
    table = {}
    for full, iso2, iso3, other in COUNTRIES:
        for k in [full, iso2, iso3] + other:
            table[k.lower()] = (full, iso2, iso3)
    return table


COUNTRY_TABLE = country_lookup()
STATE_BY_NAME = {k.lower(): (k, v.replace("_AU", "")) for k, v in STATES.items()}
STATE_BY_ABBR = {}
for _full, _ab in STATES.items():
    STATE_BY_ABBR.setdefault(_ab.replace("_AU", "").lower(), (_full, _ab.replace("_AU", "")))


def state_lookup(v):
    k = collapse(v).lower().rstrip(".")
    return STATE_BY_NAME.get(k) or STATE_BY_ABBR.get(k)


# ---------- reading and writing the export ----------

def read_export(path):
    with open(path, "rb") as f:
        raw = f.read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")
    newline = "\r\n" if "\r\n" in text[:5000] else "\n"
    sample = text[:5000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        delim = dialect.delimiter
    except csv.Error:
        delim = ","
    rows = list(csv.reader(io.StringIO(text, newline=""), delimiter=delim))
    while rows and not any(c.strip() for c in rows[-1]):
        rows.pop()
    if not rows:
        die("The file is empty.")
    header, body = rows[0], rows[1:]
    width = len(header)
    body = [r + [""] * (width - len(r)) if len(r) < width else r for r in body]
    return {"header": header, "rows": body, "bom": bom, "newline": newline, "delimiter": delim}


def write_export(path, exp, rows):
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=exp["delimiter"], lineterminator=exp["newline"])
    w.writerow(exp["header"])
    w.writerows(rows)
    data = buf.getvalue().encode("utf-8")
    with open(path, "wb") as f:
        f.write((b"\xef\xbb\xbf" if exp["bom"] else b"") + data)


# ---------- profile ----------

def map_columns(header, overrides):
    normed = [norm_header(h) for h in header]
    cmap, also = {}, {}
    for field, aliases in ALIASES.items():
        hits = []
        for a in aliases:
            for i, h in enumerate(normed):
                if h == a and i not in hits:
                    hits.append(i)
        taken = set(cmap.values())
        hits = [i for i in hits if i not in taken]
        if hits:
            cmap[field] = hits[0]
            if len(hits) > 1:
                also[field] = [header[i] for i in hits[1:]]
    for spec in overrides or []:
        if "=" not in spec:
            die("--map takes field=Header, got %r" % spec)
        field, col = spec.split("=", 1)
        field = field.strip()
        if field not in FIELDS:
            die("Unknown field %r. Fields: %s" % (field, ", ".join(FIELDS)))
        if not col.strip():
            cmap.pop(field, None)
            continue
        try:
            cmap[field] = [norm_header(h) for h in header].index(norm_header(col))
        except ValueError:
            die("No column named %r in this file." % col)
    return cmap, also


def column_styles(rows, cmap, header):
    styles = {}
    col = lambda f: [r[cmap[f]].strip() for r in rows if f in cmap and r[cmap[f]].strip()]
    if "domain" in cmap:
        styles["domain"] = "website" if norm_header(header[cmap["domain"]]) in WEBSITE_STYLE \
            else "bare"
    if "employees" in cmap:
        vals = col("employees")
        nums = sum(1 for v in vals if parse_number(v) is not None)
        styles["employees"] = "number" if not vals or nums / len(vals) >= 0.6 else "bands"
        if styles["employees"] == "bands":
            styles["employee_bands"] = [v for v, _ in Counter(vals).most_common()]
    if "country" in cmap:
        c = Counter()
        for v in col("country"):
            hit = COUNTRY_TABLE.get(v.lower())
            if hit:
                c["iso2" if v.upper() == hit[1] else "iso3" if v.upper() == hit[2] else "full"] += 1
        styles["country"] = c.most_common(1)[0][0] if c else "full"
    if "state" in cmap:
        c = Counter()
        for v in col("state"):
            hit = state_lookup(v)
            if hit:
                c["abbr" if collapse(v).upper().rstrip(".") == hit[1] else "full"] += 1
        styles["state"] = c.most_common(1)[0][0] if c else "full"
    if "industry" in cmap:
        by_key = {}
        for v, n in Counter(col("industry")).most_common():
            k = v.lower()
            # canonical spelling = most common; an all-lowercase spelling never wins a tie
            if k not in by_key or (by_key[k][1] == n and by_key[k][0].islower()):
                by_key[k] = (v, n)
        styles["industry_vocab"] = sorted(v for v, _ in by_key.values())
    if "city" in cmap:
        styles["city_vocab"] = sorted(set(col("city")))
    return styles


def to_country_style(v, style):
    hit = COUNTRY_TABLE.get(collapse(v).lower())
    if not hit:
        return None
    return {"full": hit[0], "iso2": hit[1], "iso3": hit[2]}[style]


def to_state_style(v, style):
    hit = state_lookup(v)
    if not hit:
        return None
    return hit[0] if style == "full" else hit[1]


def fix_cell(field, value, styles):
    """Return (new_value, rule) for a deterministic format fix, or (value, None)."""
    v = value
    if field in ("name", "city"):
        n = collapse(v)
        return (n, "trimmed spaces") if n != v else (v, None)
    if field == "domain":
        if styles.get("domain") == "bare":
            d = norm_domain(v)
            return (d, "domain to bare form") if d and d != v else (v, None)
        n = v.strip().rstrip("/")
        n = re.sub(r"^([A-Za-z]+://)?([^/]+)", lambda m: (m.group(1) or "").lower() + m.group(2).lower(), n)
        return (n, "website lowercased, trailing slash removed") if n != v else (v, None)
    if field == "employees" and styles.get("employees") == "number":
        n = parse_number(v)
        if n is not None and str(n) != v:
            return str(n), "employees to a plain number"
        return v, None
    if field == "revenue":
        n = parse_number(v)
        if n is not None and str(n) != v:
            return str(n), "revenue to a plain number"
        return v, None
    if field == "country":
        n = to_country_style(v, styles.get("country", "full"))
        if n and n != v:
            return n, "country to the column's usual form"
        n = collapse(v)
        return (n, "trimmed spaces") if n != v else (v, None)
    if field == "state":
        n = to_state_style(v, styles.get("state", "full"))
        if n and n != v:
            return n, "state to the column's usual form"
        n = collapse(v)
        return (n, "trimmed spaces") if n != v else (v, None)
    if field == "industry":
        for canon in styles.get("industry_vocab", []):
            if canon.lower() == v.strip().lower() and canon != v:
                return canon, "industry to the spelling the column already uses"
        n = collapse(v)
        return (n, "trimmed spaces") if n != v else (v, None)
    return v, None


def invalid_reason(field, value, styles):
    v = value.strip()
    if not v:
        return None
    if field == "domain" and not norm_domain(v):
        return "not a domain"
    if field == "employees" and styles.get("employees") == "number" and parse_number(v) is None:
        return "not one number (%s)" % ("a range" if re.search(r"\d\s*[-–]\s*\d", v) else "text")
    if field == "revenue" and parse_number(v) is None:
        return "not one number"
    return None


def cmd_profile(args):
    src = os.path.abspath(args.export)
    if not os.path.isfile(src):
        die("No file at %s" % src)
    run = os.path.abspath(args.run)
    os.makedirs(run, exist_ok=True)
    exp = read_export(src)
    header, rows = exp["header"], exp["rows"]
    cmap, also = map_columns(header, args.map)
    if "name" not in cmap and "domain" not in cmap:
        die("Could not find a company name or domain column. Columns: %s" % ", ".join(header))
    styles = column_styles(rows, cmap, header)
    get = lambda r, f: r[cmap[f]] if f in cmap else ""
    rid = lambda i, r: (get(r, "id").strip() or "row %d" % (i + 2)) if "id" in cmap else "row %d" % (i + 2)

    since = None
    if args.since:
        since = parse_date(args.since)
        if not since:
            die("--since takes a date like 2026-09-01")
        if "created" not in cmap:
            die("--since needs a create-date column, and this file has none.")

    ids = [rid(i, r) for i, r in enumerate(rows)]
    if "id" in cmap and len(set(ids)) != len(ids):
        die("Record IDs repeat in this file, so edits cannot be matched to rows safely.")

    in_scope = []
    for i, r in enumerate(rows):
        if since:
            d = parse_date(get(r, "created"))
            in_scope.append(bool(d and d >= since))
        else:
            in_scope.append(True)

    # format fixes (in-scope rows, mapped columns only)
    fixes, fixed_rows = [], [list(r) for r in rows]
    for i, r in enumerate(rows):
        if not in_scope[i]:
            continue
        for f in FIELDS:
            if f not in cmap or f in ("id", "created"):
                continue
            old = r[cmap[f]]
            new, rule = fix_cell(f, old, styles)
            if rule:
                fixes.append({"row_id": ids[i], "field": f, "column": header[cmap[f]],
                              "before": old, "after": new, "rule": rule})
                fixed_rows[i][cmap[f]] = new

    # duplicates: same domain = confirmed; same name, or a short name that prefixes a longer
    # one, without conflicting domains = candidate for the auditor
    doms = [norm_domain(get(r, "domain")) for r in fixed_rows]
    keys = [name_key(get(r, "name")) for r in fixed_rows]
    filled = lambda r: sum(1 for f in FIELDS if f in cmap and r[cmap[f]].strip())
    created = [parse_date(get(r, "created")) for r in rows]
    groups = OrderedDict()
    for i, d in enumerate(doms):
        if d:
            groups.setdefault(d, []).append(i)
    confirmed, losers = [], set()
    for d, idx in groups.items():
        if len(idx) < 2:
            continue
        surv = sorted(idx, key=lambda i: (-filled(fixed_rows[i]),
                                          created[i] or datetime.max, i))[0]
        others = [i for i in idx if i != surv]
        losers.update(others)
        carry = []
        for o in others:
            for f in FIELDS:
                if f in cmap and f not in ("id", "created") and fixed_rows[o][cmap[f]].strip() \
                        and not fixed_rows[surv][cmap[f]].strip():
                    carry.append({"from": ids[o], "field": f, "value": fixed_rows[o][cmap[f]]})
        confirmed.append({"rows": [ids[surv]] + [ids[o] for o in others], "survivor": ids[surv],
                          "basis": "same domain (%s)" % d, "carry_over": carry})
    candidates, seen = [], set()
    for i in range(len(rows)):
        for j in range(len(rows)):
            if i >= j and keys[i] == keys[j]:
                continue
            a, b = keys[i], keys[j]
            if not a or not b:
                continue
            same = a == b and i < j
            prefix = (a != b and b.startswith(a + " ") and not doms[i])
            if not (same or prefix):
                continue
            if doms[i] and doms[j]:
                continue  # both have domains: equal ones are confirmed above, unequal differ
            pair = tuple(sorted((i, j)))
            if pair in seen:
                continue
            seen.add(pair)
            candidates.append({"rows": [ids[pair[0]], ids[pair[1]]],
                               "names": [get(rows[pair[0]], "name"), get(rows[pair[1]], "name")],
                               "basis": "same name" if same else "short name matches a longer one"})

    # enrichment: flagged rows, newest first, capped
    flagged = []
    for i, r in enumerate(fixed_rows):
        if not in_scope[i] or i in losers:
            continue
        missing = [f for f in ENRICH_FIELDS if f in cmap and not r[cmap[f]].strip()]
        invalid = {f: invalid_reason(f, r[cmap[f]], styles) for f in ENRICH_FIELDS if f in cmap}
        invalid = {f: why for f, why in invalid.items() if why}
        if not (missing or invalid):
            continue
        if not get(r, "name").strip() and not doms[i]:
            continue
        flagged.append(i)
    has_dates = "created" in cmap and any(created[i] for i in flagged)
    order = sorted(flagged, key=lambda i: (created[i] is None,
                                           -(created[i].timestamp() if created[i] else 0), i)) \
        if has_dates else list(flagged)
    selected, queued = order[:ENRICH_CAP], order[ENRICH_CAP:]

    def payload(i):
        r = fixed_rows[i]
        return {"row_id": ids[i], "name": collapse(get(r, "name")), "domain": doms[i],
                "missing": [f for f in ENRICH_FIELDS if f in cmap and not r[cmap[f]].strip()],
                "invalid": {f: {"value": r[cmap[f]], "why": invalid_reason(f, r[cmap[f]], styles)}
                            for f in ENRICH_FIELDS if f in cmap
                            and invalid_reason(f, r[cmap[f]], styles)},
                "current": {f: r[cmap[f]] for f in ENRICH_FIELDS if f in cmap and r[cmap[f]].strip()
                            and not invalid_reason(f, r[cmap[f]], styles)}}

    batches = [[payload(i) for i in selected[k:k + BATCH_SIZE]]
               for k in range(0, len(selected), BATCH_SIZE)]
    leftovers = [{"row_id": ids[i], "field": f, "value": fixed_rows[i][cmap[f]],
                  "why": invalid_reason(f, fixed_rows[i][cmap[f]], styles)}
                 for i in range(len(rows)) if in_scope[i]
                 for f in ("revenue",) if f in cmap
                 and invalid_reason(f, fixed_rows[i][cmap[f]], styles)]

    profile = {
        "version": 1, "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "source": src, "file_name": os.path.basename(src),
        "rows": len(rows), "header": header,
        "columns": {f: header[c] for f, c in cmap.items()},
        "also_matched": also,
        "unmapped": [h for k, h in enumerate(header) if k not in cmap.values()],
        "no_id_column": "id" not in cmap,
        "styles": styles,
        "scope": {"since": args.since, "rows_in_scope": sum(in_scope)},
        "cap": {"rows": ENRICH_CAP, "lookups_per_row": LOOKUPS_PER_ROW, "batch_size": BATCH_SIZE,
                "flagged": len(flagged), "selected": len(selected), "queued": len(queued),
                "order": "newest create date first" if has_dates else "file order"},
        "format_fixes": fixes,
        "duplicates_confirmed": confirmed,
        "duplicate_candidates": candidates,
        "enrich_batches": batches,
        "queued": [payload(i) for i in queued],
        "invalid_left": leftovers,
    }
    with open(os.path.join(run, "profile.json"), "w") as f:
        json.dump(profile, f, indent=2)
    print(json.dumps({
        "ok": True, "rows": len(rows), "rows_in_scope": sum(in_scope),
        "columns": profile["columns"], "unmapped": profile["unmapped"],
        "no_id_column": profile["no_id_column"], "format_fixes": len(fixes),
        "duplicates_confirmed": len(confirmed), "duplicate_candidates": len(candidates),
        "flagged_for_enrichment": len(flagged), "enriching": len(selected),
        "queued_over_cap": len(queued), "batches": len(batches), "cap": ENRICH_CAP,
        "profile": os.path.join(run, "profile.json")}, indent=2))


# ---------- apply ----------

def validate_fill(field, value, styles):
    """Return (normalized_value, None) or (None, reason)."""
    v = collapse(str(value))
    if not v:
        return None, "empty value"
    if field == "domain":
        d = norm_domain(v)
        return (d, None) if d else (None, "not a domain")
    if field == "employees":
        if styles.get("employees") == "bands":
            for b in styles.get("employee_bands", []):
                if b.lower() == v.lower():
                    return b, None
            return None, "not one of your employee bands"
        n = parse_number(v)
        return (str(n), None) if n is not None else (None, "not one number")
    if field == "industry":
        vocab = styles.get("industry_vocab", [])
        if not vocab:
            return v, None
        for canon in vocab:
            if canon.lower() == v.lower():
                return canon, None
        return None, "not one of the Industry values already in your file"
    if field == "country":
        return (to_country_style(v, styles.get("country", "full")) or v), None
    if field == "state":
        return (to_state_style(v, styles.get("state", "full")) or v), None
    if field == "city":
        # "New York City" becomes "New York" when that is how the column already spells it
        short = re.sub(r"\s+city$", "", v, flags=re.I)
        for known in styles.get("city_vocab", []):
            if known.lower() in (v.lower(), short.lower()):
                return known, None
    return v, None


def cmd_apply(args):
    run = os.path.abspath(args.run)
    try:
        profile = json.load(open(os.path.join(run, "profile.json")))
    except (OSError, ValueError) as e:
        die("Could not read profile.json in %s: %s" % (run, e))
    try:
        decisions = json.load(open(os.path.join(run, "decisions.json")))
    except (OSError, ValueError) as e:
        die("Could not read decisions.json in %s: %s" % (run, e))
    corrections = []
    if args.corrections:
        try:
            corrections = json.load(open(args.corrections))
        except (OSError, ValueError) as e:
            die("Could not read %s: %s" % (args.corrections, e))

    exp = read_export(profile["source"])
    header, orig = exp["header"], exp["rows"]
    if header != profile["header"] or len(orig) != profile["rows"]:
        die("The export changed since it was profiled. Run profile again.")
    cmap = {f: header.index(h) for f, h in profile["columns"].items()}
    styles = profile["styles"]
    ids = [(r[cmap["id"]].strip() or "row %d" % (i + 2)) if "id" in cmap else "row %d" % (i + 2)
           for i, r in enumerate(orig)]
    pos = {rid: i for i, rid in enumerate(ids)}
    rows = [list(r) for r in orig]
    applied = []

    for fx in profile["format_fixes"]:
        i, c = pos[fx["row_id"]], cmap[fx["field"]]
        if rows[i][c] != fx["before"]:
            die("Row %s changed since profiling. Run profile again." % fx["row_id"])
        rows[i][c] = fx["after"]
        applied.append(dict(fx, kind="format"))

    selected = {p["row_id"]: p for b in profile["enrich_batches"] for p in b}
    names = {p["row_id"]: p["name"] for b in profile["enrich_batches"] for p in b}
    rejected, conflicts, done = [], list(decisions.get("conflicts", [])), set()
    for fl in decisions.get("fills", []):
        rid, field = str(fl.get("row_id", "")), fl.get("field")
        src = (fl.get("source_url") or "").strip()
        why = None
        if rid not in pos:
            why = "no such row"
        elif rid not in selected:
            why = "outside this run's enrichment cap of %d rows" % profile["cap"]["rows"]
        elif field not in ENRICH_FIELDS or field not in cmap:
            why = "no %s column in this file" % FIELD_LABELS.get(field, field)
        elif not re.match(r"^https?://", src):
            why = "no source URL"
        elif (rid, field) in done:
            why = "a second value for the same cell"
        if not why:
            i, c = pos[rid], cmap[field]
            cur = rows[i][c]
            if cur.strip() and not invalid_reason(field, cur, styles):
                conflicts.append({"row_id": rid, "field": field, "current": cur,
                                  "proposed": fl.get("value"), "source_url": src,
                                  "note": "Your file already has a value here; nothing was overwritten."})
                continue
            val, why = validate_fill(field, fl.get("value"), styles)
            if not why:
                rows[i][c] = val
                done.add((rid, field))
                applied.append({"row_id": rid, "field": field, "column": header[c], "before": cur,
                                "after": val, "kind": "fill", "source_url": src,
                                "source_note": fl.get("source_note", ""),
                                "rule": "filled from a public source"})
                continue
        rejected.append(dict(fl, reason=why))

    conflict_keys = {(str(c.get("row_id")), c.get("field")) for c in conflicts}
    for co in corrections:
        rid, field = str(co.get("row_id", "")), co.get("field")
        if (rid, field) not in conflict_keys or rid not in pos or field not in cmap:
            rejected.append(dict(co, requested=True, reason="this run did not list it for your call, so it was left as it was"))
            continue
        val, why = validate_fill(field, co.get("value"), styles)
        if why:
            rejected.append(dict(co, requested=True, reason=why))
            continue
        i, c = pos[rid], cmap[field]
        applied.append({"row_id": rid, "field": field, "column": header[c], "before": rows[i][c],
                        "after": val, "kind": "correction",
                        "source_url": co.get("source_url", ""), "rule": "corrected at your request"})
        rows[i][c] = val
    corrected = {(a["row_id"], a["field"]) for a in applied if a["kind"] == "correction"}
    conflicts = [c for c in conflicts if (str(c.get("row_id")), c.get("field")) not in corrected]

    # duplicates found only once enrichment supplied a domain
    dups = list(profile["duplicates_confirmed"])
    in_confirmed = {r for d in dups for r in d["rows"]}
    if "domain" in cmap:
        by_dom = OrderedDict()
        for i, r in enumerate(rows):
            d = norm_domain(r[cmap["domain"]])
            if d:
                by_dom.setdefault(d, []).append(ids[i])
        for d, members in by_dom.items():
            if len(members) > 1 and not set(members) <= in_confirmed:
                dups.append({"rows": members, "survivor": members[0],
                             "basis": "same domain (%s) once enrichment found it" % d,
                             "carry_over": []})
                in_confirmed.update(members)

    stem = os.path.splitext(profile["file_name"])[0]
    out_csv = os.path.join(run, "%s-cleaned.csv" % stem)
    write_export(out_csv, exp, rows)

    # verify by re-reading what was written
    back = read_export(out_csv)
    problems = []
    if back["header"] != header:
        problems.append("header changed")
    if len(back["rows"]) != len(orig):
        problems.append("row count %d, expected %d" % (len(back["rows"]), len(orig)))
    edited = {(a["row_id"], a["column"]) for a in applied}
    for i, (a, b) in enumerate(zip(orig, back["rows"])):
        if "id" in cmap and a[cmap["id"]] != b[cmap["id"]]:
            problems.append("record ID changed on row %d" % (i + 2))
        for k, (x, y) in enumerate(zip(a, b)):
            if x != y and (ids[i], header[k]) not in edited:
                problems.append("unlogged change: %s / %s" % (ids[i], header[k]))
    if problems:
        os.replace(out_csv, out_csv + ".failed")
        die("The cleaned file failed its check and was not kept: " + "; ".join(problems[:5]))

    result = {
        "ok": True, "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "file_name": profile["file_name"], "cleaned_csv": out_csv, "rows": len(orig),
        "columns": profile["columns"], "no_id_column": profile["no_id_column"],
        "scope": profile["scope"], "cap": profile["cap"],
        "enriched_rows": sorted({a["row_id"] for a in applied if a["kind"] == "fill"},
                                key=lambda r: pos[r]),
        "looked_up_rows": [p["row_id"] for b in profile["enrich_batches"] for p in b],
        "applied": applied, "conflicts": conflicts, "rejected": rejected,
        "duplicates": dups, "duplicate_verdicts": decisions.get("duplicates", []),
        "unresolved": decisions.get("unresolved", []),
        "queued": profile["queued"], "invalid_left": profile["invalid_left"],
        "coverage": decisions.get("coverage", ""),
        "names": {ids[i]: collapse(orig[i][cmap["name"]]) if "name" in cmap else ids[i]
                  for i in range(len(orig))},
        "not_looked_up": len(orig) - len(selected) - len(profile["queued"]),
    }
    with open(os.path.join(run, "applied.json"), "w") as f:
        json.dump(result, f, indent=2)
    md, page = render_md(result), render_html(result)
    with open(os.path.join(run, "change-log.md"), "w") as f:
        f.write(md)
    with open(os.path.join(run, "change-log.html"), "w") as f:
        f.write(page)
    counts = Counter(a["kind"] for a in applied)
    print(json.dumps({
        "ok": True, "cleaned_csv": out_csv, "change_log": os.path.join(run, "change-log.md"),
        "artifact": os.path.join(run, "change-log.html"), "rows": len(orig),
        "format_fixes": counts["format"], "filled": counts["fill"],
        "corrected": counts["correction"], "rows_enriched": len(result["enriched_rows"]),
        "rows_looked_up": len(result["looked_up_rows"]), "cap": profile["cap"]["rows"],
        "queued_over_cap": len(profile["queued"]), "needs_your_call": len(conflicts),
        "rejected": len(rejected), "duplicates": len(dups),
        "unresolved": len(result["unresolved"])}, indent=2))


# ---------- the change log ----------

def cap_line(res):
    cap = res["cap"]
    return ("Enrichment cap: %d rows per run, up to %d lookups each. This run looked up %d of "
            "%d flagged rows; %d queued for the next run." %
            (cap["rows"], cap["lookups_per_row"], cap["selected"], cap["flagged"], cap["queued"]))


def sections(res):
    """The change log's sections, in order. Names are load-bearing: the skill and the
    artifact refer to them."""
    n = res["names"]
    fills = [a for a in res["applied"] if a["kind"] == "fill"]
    fmt = [a for a in res["applied"] if a["kind"] == "format"]
    corr = [a for a in res["applied"] if a["kind"] == "correction"]
    verdicts = res["duplicate_verdicts"]
    same = [d for d in res["duplicates"]]
    # a same-domain match settles a pair; a weaker verdict on it would contradict the merge list
    settled = lambda v: any(set(v.get("rows", [])) <= set(d["rows"]) for d in same)
    possible = [v for v in verdicts if v.get("verdict") == "possible" and not settled(v)]
    same_v = [v for v in verdicts if v.get("verdict") == "same" and not settled(v)]
    different = [v for v in verdicts if v.get("verdict") == "different" and not settled(v)]
    review = res["conflicts"] + [dict(r, kind="rejected") for r in res["rejected"]] + \
        [dict(r, kind="invalid") for r in res["invalid_left"]]
    return n, fills, fmt, corr, same, same_v, possible, different, review


def render_md(res):
    n, fills, fmt, corr, same, same_v, possible, different, review = sections(res)
    lab = lambda f: FIELD_LABELS.get(f, f)
    L = ["# Change log — %s" % res["file_name"], "",
         "**Run:** %s · **Rows:** %d in, %d out, same order · **Scope:** %s" % (
             res["generated"], res["rows"], res["rows"],
             "records created since %s" % res["scope"]["since"] if res["scope"]["since"]
             else "the whole file"),
         "**%s**" % cap_line(res),
         "**Cleaned file:** `%s`" % os.path.basename(res["cleaned_csv"]), ""]
    if res["no_id_column"]:
        L += ["> **This export has no record ID column.** Importing it will create new records "
              "instead of updating the ones you have. Re-export with the record ID included, "
              "then run this again.", ""]
    L += ["## Summary", "",
          "| | Count |", "|---|---|",
          "| Format fixes | %d |" % len(fmt),
          "| Filled from public sources | %d values on %d rows |" % (len(fills), len(res["enriched_rows"])),
          "| Duplicates to merge | %d |" % (len(same) + len(same_v)),
          "| Possible duplicates | %d |" % len(possible),
          "| Needs your call | %d |" % len(review),
          "| Could not resolve | %d |" % len(res["unresolved"]),
          "| Queued for the next run | %d |" % len(res["queued"]), ""]

    L += ["## Duplicates to merge", "",
          "The file does not delete or merge rows. Merge these in your CRM, keeping the first "
          "record listed.", ""]
    if not (same or same_v):
        L.append("None found.")
    for d in same:
        L.append("- **Keep %s (%s)**, merge %s. %s." % (
            d["survivor"], n.get(d["survivor"], ""),
            ", ".join("%s (%s)" % (r, n.get(r, "")) for r in d["rows"] if r != d["survivor"]),
            d["basis"][0].upper() + d["basis"][1:]))
        for c in d.get("carry_over", []):
            L.append("  - Carry over %s `%s` from %s." % (lab(c["field"]), c["value"], c["from"]))
    for v in same_v:
        L.append("- **Keep %s (%s)**, merge %s. %s" % (
            v.get("survivor", v["rows"][0]), n.get(v.get("survivor", v["rows"][0]), ""),
            ", ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"]
                      if r != v.get("survivor", v["rows"][0])), v.get("evidence", "")))
    if possible:
        L += ["", "**Possible duplicates — check before merging:**", ""]
        for v in possible:
            L.append("- %s. %s" % (" and ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"]),
                                   v.get("evidence", "")))
    if different:
        L += ["", "**Checked and kept separate:**", ""]
        for v in different:
            L.append("- %s. %s" % (" and ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"]),
                                   v.get("evidence", "")))
    L.append("")

    L += ["## Needs your call", "",
          "Nothing in this section changed in the cleaned file.", ""]
    if not review:
        L.append("Nothing.")
    for r in review:
        rid = str(r.get("row_id"))
        if r.get("kind") == "rejected":
            L.append("- **%s (%s)** · %s: %s `%s`, not applied: %s.%s" % (
                rid, n.get(rid, ""), lab(r.get("field")),
                "you asked for" if r.get("requested") else "found", r.get("value"), r.get("reason"),
                " Source: %s" % r["source_url"] if r.get("source_url") else ""))
        elif r.get("kind") == "invalid":
            L.append("- **%s (%s)** · %s `%s` is %s. Not changed." % (
                rid, n.get(rid, ""), lab(r["field"]), r["value"], r["why"]))
        else:
            L.append("- **%s (%s)** · %s: your file says `%s`; the source says `%s`. %s Source: %s" % (
                rid, n.get(rid, ""), lab(r.get("field")), r.get("current"), r.get("proposed"),
                r.get("note", ""), r.get("source_url", "")))
    L.append("")

    L += ["## Filled from public sources", ""]
    if not fills:
        L.append("Nothing was filled.")
    else:
        L += ["| Row | Company | Field | Value | Source |", "|---|---|---|---|---|"]
        for a in fills:
            L.append("| %s | %s | %s | %s | %s |" % (a["row_id"], n.get(a["row_id"], ""),
                                                   lab(a["field"]), a["after"], a["source_url"]))
    if corr:
        L += ["", "**Corrected at your request:**", "",
              "| Row | Company | Field | Was | Now | Source |", "|---|---|---|---|---|---|"]
        for a in corr:
            L.append("| %s | %s | %s | %s | %s | %s |" % (a["row_id"], n.get(a["row_id"], ""),
                                                        lab(a["field"]), a["before"], a["after"],
                                                        a.get("source_url", "")))
    L.append("")

    L += ["## Format fixes", ""]
    if not fmt:
        L.append("None needed.")
    else:
        L += ["| Row | Column | Before | After | Rule |", "|---|---|---|---|---|"]
        for a in fmt:
            L.append("| %s | %s | `%s` | `%s` | %s |" % (a["row_id"], a["column"], a["before"],
                                                       a["after"], a["rule"]))
    L.append("")

    L += ["## Could not resolve", ""]
    if not res["unresolved"]:
        L.append("Every looked-up row resolved to one company.")
    for u in res["unresolved"]:
        L.append("- **%s** `%s`: could be %s. Nothing added. %s" % (
            u.get("row_id"), u.get("entry", ""), "; ".join(u.get("candidates", [])) or "unclear",
            u.get("fix", "Add a domain and it runs next time.")))
    L.append("")

    L += ["## Queued for the next run", "", cap_line(res), ""]
    if not res["queued"]:
        L.append("Nothing queued: every flagged row fit inside the cap.")
    else:
        L.append("Run this again on the cleaned file and these are looked up first.")
        L.append("")
        for q in res["queued"]:
            L.append("- %s (%s): missing %s" % (q["row_id"], q["name"],
                                                ", ".join(lab(f) for f in q["missing"] + list(q["invalid"]))))
    L.append("")

    L += ["## What this run did not check", "",
          "%d complete rows were not looked up. Enrichment only looks up rows with a missing or "
          "unusable value, so a wrong value in a complete row is not caught. Annual revenue is "
          "never filled: public figures for private companies are estimates." % res["not_looked_up"],
          ""]
    if res["coverage"]:
        L += [res["coverage"], ""]
    L += ["## Importing the cleaned file", "",
          "Import `%s` as an update to existing records, matched on **%s**. It has the same "
          "columns and rows as your export. Merge the duplicates above in your CRM first." % (
              os.path.basename(res["cleaned_csv"]), res["columns"].get("id", "your record ID")),
          "", "---", "",
          "Sourced values carry their link. Format fixes follow the form your column already "
          "uses. Built with BlueRock · CRM Cleanup and Enrichment · record-enricher + record-auditor", ""]
    return "\n".join(L)


CSS = """
:root{--paper:#F5F1EA;--card:#FFFFFF;--card-2:#FAF7F1;--line:#E7E0D6;--line-2:#D6CDBE;
--ink:#1B2130;--ink-2:#3D4658;--ink-3:#6B7486;--ink-4:#8B93A3;
--accent:#1559C4;--accent-soft:#E8EFFB;--accent-line:#B9CDEF;
--kill:#B4432E;--kill-soft:#F9ECE8;--kill-line:#E8C7BE;
--bullet:#206E5B;--bullet-soft:#E7F2EE;--bullet-line:#BFDCD3;
--mine:#94660F;--mine-soft:#F7EFDD;--mine-line:#E5D3AC;
--neutral:#5A6272;--neutral-soft:#EEEDE9;--neutral-line:#D9D3C8;--chip-text:#FFFFFF}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#14171E;--card:#1C212B;
--card-2:#222835;--line:#2E3542;--line-2:#3D4658;--ink:#EDEEF2;--ink-2:#C3C9D4;--ink-3:#97A0B0;
--ink-4:#7B8494;--accent:#6E9BE8;--accent-soft:#1D2A45;--accent-line:#34528C;--kill:#E0715A;
--kill-soft:#372220;--kill-line:#6B392F;--bullet:#55B092;--bullet-soft:#1B2E29;
--bullet-line:#2F5A4B;--mine:#D3A24C;--mine-soft:#322A19;--mine-line:#66542B;--neutral:#9AA3B2;
--neutral-soft:#262C37;--neutral-line:#414A5A;--chip-text:#14171E}}
:root[data-theme="dark"]{--paper:#14171E;--card:#1C212B;--card-2:#222835;--line:#2E3542;
--line-2:#3D4658;--ink:#EDEEF2;--ink-2:#C3C9D4;--ink-3:#97A0B0;--ink-4:#7B8494;--accent:#6E9BE8;
--accent-soft:#1D2A45;--accent-line:#34528C;--kill:#E0715A;--kill-soft:#372220;
--kill-line:#6B392F;--bullet:#55B092;--bullet-soft:#1B2E29;--bullet-line:#2F5A4B;
--mine:#D3A24C;--mine-soft:#322A19;--mine-line:#66542B;--neutral:#9AA3B2;--neutral-soft:#262C37;
--neutral-line:#414A5A;--chip-text:#14171E}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.5 "DM Sans",system-ui,-apple-system,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:0 16px 48px;overflow-wrap:anywhere}
.mast{position:sticky;top:0;background:var(--paper);border-bottom:1px solid var(--line);padding:18px 0 12px;z-index:2}
h1{font-size:22px;letter-spacing:.04em;text-transform:uppercase;margin:0 0 6px;font-weight:800}
.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace}
.meta{font-size:12px;color:var(--ink-2)}
.cap{margin-top:8px;font-size:12px;color:var(--ink);background:var(--mine-soft);border:1px solid var(--mine-line);border-radius:6px;padding:6px 10px}
.warn{margin-top:8px;font-size:13px;background:var(--kill-soft);border:1px solid var(--kill-line);border-radius:6px;padding:8px 10px}
.counters{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:14px 0 10px}
@media (max-width:640px){.counters{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ctr{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--t);border-radius:6px;padding:8px 10px}
.ctr b{display:block;font:600 28px/1.1 "Source Serif 4",Georgia,serif;color:var(--t)}
.ctr span{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips button{font:12px "JetBrains Mono",ui-monospace,Menlo,monospace;border:1px solid var(--line-2);background:var(--card);color:var(--ink-2);border-radius:999px;padding:4px 10px;cursor:pointer}
.chips button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.chips button[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.chips i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--t);margin-right:6px}
section.lane{margin-top:26px}
section.lane h2{display:flex;align-items:center;gap:10px;font-size:17px;margin:0 0 4px}
section.lane h3{font-size:14px;margin:14px 0 6px}
.tag{font:11px "JetBrains Mono",ui-monospace,Menlo,monospace;background:var(--t);color:var(--chip-text);border-radius:4px;padding:2px 7px}
.lead{color:var(--ink-2);font-size:13px;margin:0 0 10px}
.item{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--t);border-radius:6px;padding:10px 12px;margin:8px 0}
.item .who{font-weight:700}
.item .why{font-family:"Source Serif 4",Georgia,serif;color:var(--ink-2)}
table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:6px;font-size:13px}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;overflow-wrap:anywhere}
th{font:11px "JetBrains Mono",ui-monospace,Menlo,monospace;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-2);background:var(--card-2)}
td code,.item code{font:12px "JetBrains Mono",ui-monospace,Menlo,monospace;background:var(--card-2);border:1px solid var(--line);border-radius:3px;padding:0 4px}
a{color:var(--accent)}
.tablewrap{overflow-x:auto}
.empty{color:var(--ink-2);font-style:italic}
footer{margin-top:32px;border-top:1px solid var(--line);padding-top:12px;font-size:12px;color:var(--ink-2)}
@media print{.mast{position:static}.chips,.counters{display:none}[hidden]{display:block !important}
section.lane{break-before:page}section.lane:first-of-type{break-before:auto}}
"""

JS = """
document.querySelectorAll('.chips button').forEach(function(b){b.addEventListener('click',function(){
document.querySelectorAll('.chips button').forEach(function(x){x.setAttribute('aria-pressed','false')});
b.setAttribute('aria-pressed','true');var t=b.getAttribute('data-show');
document.querySelectorAll('section.lane').forEach(function(s){s.hidden=!(t==='all'||s.id===t)});});});
"""


def render_html(res):
    e = lambda s: html.escape(str(s if s is not None else ""))
    n, fills, fmt, corr, same, same_v, possible, different, review = sections(res)
    lab = lambda f: FIELD_LABELS.get(f, f)
    src = lambda u, what="": '<a class="mono" href="%s" rel="noopener"%s>%s</a>' % (
        e(u), ' aria-label="Source for %s: %s"' % (e(what), e(norm_domain(u) or u)) if what else "",
        e(norm_domain(u) or u)) if u else ""
    lanes = [
        ("review", "Needs your call", "kill", len(review)),
        ("merge", "Duplicates to merge", "accent", len(same) + len(same_v) + len(possible)),
        ("filled", "Filled from public sources", "bullet", len(fills) + len(corr)),
        ("format", "Format fixes", "neutral", len(fmt)),
        ("unresolved", "Could not resolve", "mine", len(res["unresolved"])),
        ("queued", "Queued for the next run", "mine", len(res["queued"])),
    ]
    P = ['<!doctype html><html lang="en"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>CRM change log</title>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;800&family=JetBrains+Mono:wght@400&family=Source+Serif+4:wght@400;600&display=swap">',
         "<style>%s</style></head><body><div class=\"wrap\">" % CSS,
         '<header class="mast"><h1>CRM change log · %s</h1>' % e(res["file_name"]),
         '<div class="meta mono">%s · %d rows in, %d out, same order · %s · %d of %d flagged rows looked up</div>' % (
             e(res["generated"]), res["rows"], res["rows"],
             e("since " + res["scope"]["since"]) if res["scope"]["since"] else "whole file",
             res["cap"]["selected"], res["cap"]["flagged"]),
         '<div class="cap mono">%s</div>' % e(cap_line(res))]
    if res["no_id_column"]:
        P.append('<div class="warn">This export has no record ID column, so importing it creates '
                 'new records instead of updating yours. Re-export with the record ID included.</div>')
    P.append('<div class="counters">')
    for lid, name, tok, cnt in lanes:
        P.append('<div class="ctr" style="--t:var(--%s)"><b>%d</b><span>%s</span></div>' % (
            tok, cnt, e(name)))
    P.append('</div><div class="chips" role="group" aria-label="Show section">'
             '<button aria-pressed="true" data-show="all">All changes</button>')
    for lid, name, tok, cnt in lanes:
        P.append('<button aria-pressed="false" data-show="%s"><i style="--t:var(--%s)"></i>%s · %d</button>'
                 % (lid, tok, e(name), cnt))
    P.append("</div></header>")

    def lane(lid, name, tok, cnt, lead, body):
        return ('<section class="lane" id="%s" aria-labelledby="h-%s" style="--t:var(--%s)">'
                '<h2 id="h-%s"><span class="tag" aria-hidden="true">%d</span>%s</h2><p class="lead">%s</p>%s</section>'
                % (lid, lid, tok, lid, cnt, e(name), e(lead), body))

    def table(head, rows_):
        if not rows_:
            return '<p class="empty">None.</p>'
        return ('<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                % ("".join("<th>%s</th>" % h for h in head),
                   "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows_)))

    items = []
    for r in review:
        rid = str(r.get("row_id"))
        if r.get("kind") == "rejected":
            txt = "%s: %s <code>%s</code>, not applied: %s. %s" % (
                e(lab(r.get("field"))), "you asked for" if r.get("requested") else "found", e(r.get("value")), e(r.get("reason")),
                src(r.get("source_url"), "%s %s" % (n.get(rid, ""), lab(r.get("field")))))
        elif r.get("kind") == "invalid":
            txt = "%s <code>%s</code> is %s. Not changed." % (e(lab(r["field"])), e(r["value"]), e(r["why"]))
        else:
            txt = ("%s: your file says <code>%s</code>; the source says <code>%s</code>. "
                   '<span class="why">%s</span> %s' % (e(lab(r.get("field"))), e(r.get("current")),
                                                        e(r.get("proposed")), e(r.get("note", "")),
                                                        src(r.get("source_url"), "%s %s" % (n.get(rid, ""), lab(r.get("field"))))))
        items.append('<div class="item"><div class="who">%s · %s</div>%s</div>' % (e(rid), e(n.get(rid, "")), txt))
    P.append(lane("review", "Needs your call", "kill", len(review),
                  "Nothing here changed in the cleaned file. Each one is yours to decide.",
                  "".join(items) or '<p class="empty">Nothing needs your call.</p>'))

    m = []
    for d in same:
        carry = "".join("<br>Carry over %s <code>%s</code> from %s." % (e(lab(c["field"])), e(c["value"]), e(c["from"]))
                        for c in d.get("carry_over", []))
        m.append('<div class="item"><div class="who">Keep %s · %s</div>Merge %s. %s.%s</div>' % (
            e(d["survivor"]), e(n.get(d["survivor"], "")),
            e(", ".join("%s (%s)" % (r, n.get(r, "")) for r in d["rows"] if r != d["survivor"])),
            e(d["basis"][0].upper() + d["basis"][1:]), carry))
    for v in same_v:
        s = v.get("survivor", v["rows"][0])
        m.append('<div class="item"><div class="who">Keep %s · %s</div>Merge %s. <span class="why">%s</span></div>' % (
            e(s), e(n.get(s, "")), e(", ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"] if r != s)),
            e(v.get("evidence", ""))))
    for v in possible:
        m.append('<div class="item" style="--t:var(--mine)"><div class="who">Possible · %s</div><span class="why">%s</span></div>' % (
            e(" and ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"])), e(v.get("evidence", ""))))
    for v in different:
        m.append('<div class="item" style="--t:var(--neutral)"><div class="who">Kept separate · %s</div><span class="why">%s</span></div>' % (
            e(" and ".join("%s (%s)" % (r, n.get(r, "")) for r in v["rows"])), e(v.get("evidence", ""))))
    P.append(lane("merge", "Duplicates to merge", "accent", len(same) + len(same_v) + len(possible),
                  "The file does not delete or merge rows. Merge these in your CRM, keeping the record named first.",
                  "".join(m) or '<p class="empty">No duplicates found.</p>'))

    frows = [[e(a["row_id"]), e(n.get(a["row_id"], "")), e(lab(a["field"])), "<code>%s</code>" % e(a["after"]),
              src(a["source_url"], "%s %s" % (n.get(a["row_id"], ""), lab(a["field"])))] for a in fills]
    body = table(["Row", "Company", "Field", "Value", "Source"], frows)
    if corr:
        body += "<h3>Corrected at your request</h3>" + table(
            ["Row", "Company", "Field", "Was", "Now", "Source"],
            [[e(a["row_id"]), e(n.get(a["row_id"], "")), e(lab(a["field"])), "<code>%s</code>" % e(a["before"]),
              "<code>%s</code>" % e(a["after"]), src(a.get("source_url"), "%s %s" % (n.get(a["row_id"], ""), lab(a["field"])))] for a in corr])
    P.append(lane("filled", "Filled from public sources", "bullet", len(fills) + len(corr),
                  "Only empty or unusable cells were filled. Every value carries its source.", body))

    P.append(lane("format", "Format fixes", "neutral", len(fmt),
                  "To the form each column already uses. No lookups.",
                  table(["Row", "Column", "Before", "After", "Rule"],
                        [[e(a["row_id"]), e(a["column"]), "<code>%s</code>" % e(a["before"]),
                          "<code>%s</code>" % e(a["after"]), e(a["rule"])] for a in fmt])))

    u = ['<div class="item"><div class="who">%s · <code>%s</code></div>Could be %s. Nothing added. %s</div>' % (
        e(x.get("row_id")), e(x.get("entry", "")), e("; ".join(x.get("candidates", [])) or "unclear"),
        e(x.get("fix", "Add a domain and it runs next time."))) for x in res["unresolved"]]
    P.append(lane("unresolved", "Could not resolve", "mine", len(res["unresolved"]),
                  "Named and skipped rather than guessed.",
                  "".join(u) or '<p class="empty">Every looked-up row resolved to one company.</p>'))

    q = table(["Row", "Company", "Missing"],
              [[e(x["row_id"]), e(x["name"]), e(", ".join(lab(f) for f in x["missing"] + list(x["invalid"])))]
               for x in res["queued"]])
    P.append(lane("queued", "Queued for the next run", "mine", len(res["queued"]),
                  cap_line(res) + " Run this again on the cleaned file and these go first.", q))

    P.append('<footer><p>%d complete rows were not looked up, so a wrong value in a complete row is not '
             'caught. Annual revenue is never filled. %s</p><p>Import <span class="mono">%s</span> as an '
             'update matched on <b>%s</b>.</p><p>Account data from your CRM. Keep it in your project.</p>'
             '<p class="mono">Built with BlueRock · CRM Cleanup and Enrichment · record-enricher + record-auditor</p>'
             '</footer>' % (res["not_looked_up"], e(res["coverage"]), e(os.path.basename(res["cleaned_csv"])),
                            e(res["columns"].get("id", "your record ID"))))
    P.append("</div><script>%s</script></body></html>" % JS)
    return "".join(P)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("profile")
    p.add_argument("export")
    p.add_argument("--run", required=True)
    p.add_argument("--since")
    p.add_argument("--map", action="append")
    a = sub.add_parser("apply")
    a.add_argument("--run", required=True)
    a.add_argument("--corrections")
    args = ap.parse_args()
    if args.cmd == "profile":
        cmd_profile(args)
    elif args.cmd == "apply":
        cmd_apply(args)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
