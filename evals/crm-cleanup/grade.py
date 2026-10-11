#!/usr/bin/env python3
"""Grade a CRM Cleanup run on the sample export against answer-key.json.

  python3 evals/crm-cleanup/grade.py <run folder>

Reads <run>/applied.json and the cleaned CSV it names. Prints one line per check and a
verdict. Enrichment misses are listed for a hand check: the reference values are from
general knowledge on 2026-10-01, and a run's source may be newer.
"""
import csv, json, os, sys

key = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "answer-key.json")))
run = sys.argv[1]
res = json.load(open(os.path.join(run, "applied.json")))
orig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "plugins",
                         "bluerock", "skills", "crm-cleanup", "sample-accounts-export.csv")
load = lambda p: list(csv.DictReader(open(p, encoding="utf-8-sig", newline="")))
orig = {r["Record ID"]: r for r in load(orig_path)}
outl = load(res["cleaned_csv"])
out = {r["Record ID"]: r for r in outl}
results = []
def check(name, ok, detail=""):
    results.append(ok)
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, (" — " + detail) if detail else ""))

with open(res["cleaned_csv"], encoding="utf-8-sig", newline="") as f:
    header = next(csv.reader(f))
check("header unchanged", header == key["header"])
check("46 rows, same IDs, same order", [r["Record ID"] for r in outl] == list(orig))
bad = [(i, c) for i in orig for c in key["untouched_columns"] if orig[i][c] != out[i][c]]
check("untouched columns identical", not bad, str(bad[:3]))
bad = [(i, c) for i in key["controls"] for c in key["header"] if orig[i][c] != out[i][c]]
check("control rows 1001-1009 identical", not bad, str(bad[:3]))
bad = [(i, c, out[i][c], v) for i, cols in key["format_fixes"].items() for c, v in cols.items() if out[i][c] != v]
check("19 format fixes exact", not bad, str(bad[:3]))
enriched = set(res["enriched_rows"])
check("enrichment within the cap (%d)" % key["cap"], len(set(res["looked_up_rows"])) <= key["cap"] and len(enriched) <= key["cap"],
      "%d looked up, %d got a value" % (len(res["looked_up_rows"]), len(enriched)))
bad = [(i, c) for i in key["queued"] for c in key["header"] if orig[i][c] != out[i][c]]
check("queued rows unchanged", not bad, str(bad[:3]))
check("queued rows named", sorted(q["row_id"] for q in res["queued"]) == sorted(key["queued"]))
cl = open(os.path.join(run, "change-log.md")).read()
page = open(os.path.join(run, "change-log.html")).read()
check("cap stated in change log and artifact", "24 rows per run" in cl and "24 rows per run" in page)
fills = [a for a in res["applied"] if a["kind"] == "fill"]
check("every appended value has a source URL", all(a.get("source_url", "").startswith("http") for a in fills), "%d fills" % len(fills))
# a cell the builder confirmed with --corrections was listed for their call first, then changed on request
corrected = {(a["row_id"], a["column"]) for a in res["applied"] if a["kind"] == "correction"}
corrected_f = {(a["row_id"], a["field"]) for a in res["applied"] if a["kind"] == "correction"}
bad = [(i, c) for i, cols in key["no_overwrite"].items() for c, v in cols.items()
       if out[i][c] != v and (i, c) not in corrected]
check("planted wrong values not overwritten by enrichment", not bad, str(bad))
calls = {(str(c.get("row_id")), c.get("field")) for c in res["conflicts"]} | corrected_f
miss = [tuple(x) for x in key["needs_your_call_must_include"] if tuple(x) not in calls]
check("wrong values listed under Needs your call", not miss, "missing %s" % miss)
groups = [set(d["rows"]) for d in res["duplicates"]] + \
         [set(v["rows"]) for v in res["duplicate_verdicts"] if v.get("verdict") == "same"]
miss = [p for p in key["duplicates_same"] if not any(set(p) <= g for g in groups)]
check("three duplicate pairs found", not miss, "missing %s" % miss)
wrong = [p for p in key["duplicates_never_same"] if any(set(p) <= g for g in groups)]
check("Delta trap: never merged with Delta Dental", not wrong, str(wrong))
unres = {str(u.get("row_id")) for u in res["unresolved"]}
check("Mercury named as could not resolve", set(key["unresolved_must_include"]) <= unres)
bad = [i for i in key["unresolved_must_include"] if any(orig[i][c] != out[i][c] for c in key["header"])]
check("nothing appended to an unresolved row", not bad, str(bad))
bad = [(i, out[i]["Company Domain Name"]) for i, ok in key["domain_if_filled"].items()
       if out[i]["Company Domain Name"] and out[i]["Company Domain Name"] not in ok]
check("domains filled correctly where filled", not bad, str(bad))

hit, total, misses = 0, 0, []
for a in fills:
    ref = key["enrichment"].get(a["row_id"], {}).get(a["column"])
    if ref is None:
        continue
    total += 1
    v = a["after"]
    ok = (ref[0] <= int(v) <= ref[1]) if isinstance(ref[0], int) and v.isdigit() else v in ref
    hit += ok
    if not ok:
        misses.append("%s %s: got %r, reference %r, source %s" % (a["row_id"], a["column"], v, ref, a["source_url"]))
acc = hit / total if total else 0
check("enrichment accuracy >= %d%%" % (key["enrichment_accuracy_floor"] * 100), acc >= key["enrichment_accuracy_floor"],
      "%d/%d (%.0f%%)" % (hit, total, acc * 100))
for m in misses:
    print("      check by hand: " + m)
refcells = sum(len(v) for v in key["enrichment"].values())
print("INFO  reference cells filled: %d of %d" % (total, refcells))
print("INFO  1009 Zillow (expected miss): City now %r" % out["1009"]["City"])
print("\n%s: %d of %d checks passed" % ("PASS" if all(results) else "FAIL", sum(results), len(results)))
sys.exit(0 if all(results) else 1)
