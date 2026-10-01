# CRM Cleanup and Enrichment: answer key for the sample export

**Test file:** `plugins/bluerock/skills/crm-cleanup/sample-accounts-export.csv` (46 rows, HubSpot
companies export shape). **Grader:** `evals/crm-cleanup/grade.py`, which reads the same
expectations from `answer-key.json`. This file is the explanation; the JSON is what is checked.

**Why this lives outside `plugins/bluerock/`:** nothing here ships to builders, and no agent in a
run can read it. A key the agents can see is a key they can copy.

**Why real companies:** enrichment has to find something on the public web, so the pipeline
mock's invented companies would make every enrichment row a "could not resolve". These are
real, well-known companies with firmographic fields deliberately blanked or wrong. Phone
numbers (`+1 555-01xx`) and owner names are fictional. There are no contact rows.

**Reference values were set on 2026-10-01** from general knowledge, not from a fetch.
Headquarters are stable; employee counts move, so each is a band, and a run that lands outside
a band is checked by hand before it counts as a miss.

## What the file plants, by row

| Rows | Plant | Expected result |
|---|---|---|
| 1001–1008 | Clean controls | Every cell unchanged |
| 1009 Zillow | **Wrong HQ on a complete row** (Portland, Oregon; actual Seattle, Washington) | **Expected miss, by design.** Only flagged rows are enriched, so a complete row is never looked up. Reported, not failed |
| 1010–1016 | Format errors only | Exact fixes below; no enrichment |
| 1017–1035, 1037–1039, 1041, 1043 | Blank or invalid firmographic fields, newest first | Enriched (24 rows, the cap) |
| 1018, 1044, 1045, 1046 | Blank fields, the **four oldest** flagged rows | **Over the cap.** Not enriched, unchanged, named as queued for the next run |
| 1036 Mercury | Name only, no domain, nothing else | **Could not resolve.** Mercury (fintech), Mercury Insurance, Mercury Marine. No value appended |
| 1037 Salesforce | Employees `45` (actual ~70,000+) | City and state filled; employees **listed for the builder's call, not overwritten** |
| 1038 Zendesk | Industry `Retail` (actual software) | Employees filled; industry **listed for the builder's call** |
| 1039 Instacart | HQ `Chicago, Illinois` (actual San Francisco, California) | Employees filled; city and state **listed for the builder's call** |
| 1040 / 1001 | Same domain, `Hubspot Inc` vs `HubSpot` | **Same company.** Survivor 1001. 1040 is not enriched |
| 1042 / 1003 | `https://www.twilio.com` vs `twilio.com` | **Same company** once the domain is normalized. Survivor 1003. 1042 is not enriched |
| 1041 / 1002 | `Datadog, Inc.` with no domain vs `Datadog` | Name match only. Enrichment finds `datadoghq.com`, which **confirms the duplicate** |
| 1043 / 1004 / 1005 | `Delta`, no domain, Atlanta, Georgia | **The trap.** Never merged with Delta Dental (1005). Either could not resolve, or resolved to `delta.com` and listed as a possible duplicate of 1004. Never `deltadental.com` |
| 1027 Box | Industry `Tech`, outside the column's vocabulary | Either changed to `Computer Software` or `Internet` with a source, or listed for the builder's call |
| 1031 Expensify | Employees `51-200`, a range in a number column | Invalid; enriched to a number |

## Exact format fixes (no web lookup needed)

| Row | Column | Before | After |
|---|---|---|---|
| 1010 | Company name | `  Okta, Inc. ` | `Okta, Inc.` |
| 1010 | Company Domain Name | `https://www.okta.com/` | `okta.com` |
| 1010 | Number of Employees | `6,000` | `6000` |
| 1010 | State/Region | `CA` | `California` |
| 1011 | Company Domain Name | `MONGODB.COM` | `mongodb.com` |
| 1011 | Annual Revenue | `$1.68B` | `1680000000` |
| 1011 | State/Region | `NY` | `New York` |
| 1011 | Country/Region | `USA` | `United States` |
| 1012 | Company Domain Name | `cloudflare.com/` | `cloudflare.com` |
| 1012 | Number of Employees | `4,200` | `4200` |
| 1012 | Country/Region | `US` | `United States` |
| 1013 | Industry | `computer software` | `Computer Software` |
| 1014 | Company Domain Name | `www.zoom.us` | `zoom.us` |
| 1014 | State/Region | `california` | `California` |
| 1015 | Annual Revenue | `2.8 billion` | `2800000000` |
| 1015 | Country/Region | `U.S.A.` | `United States` |
| 1016 | Number of Employees | `1.7k` | `1700` |
| 1016 | Country/Region | `united states` | `United States` |
| 1042 | Company Domain Name | `https://www.twilio.com` | `twilio.com` |

The target form is the column's own majority form (bare domains, full state names, "United
States"), not a form the skill prefers. A Salesforce-shaped file with two-letter states should
normalize the other way.

## Enrichment reference (rows inside the cap)

Industry must be a value already in the file's Industry column. Employees are bands.

| Row | Company | Fields to fill | Reference |
|---|---|---|---|
| 1017 | Asana | industry, employees | Computer Software · 1,000–3,500 |
| 1019 | Figma | industry, employees | Computer Software / Internet · 1,000–3,500 |
| 1020 | Airtable | employees, city, state | 300–1,500 · San Francisco, California |
| 1021 | Rippling | industry, city, state, country | Computer Software · San Francisco, California, United States |
| 1022 | Ramp | employees, city, state, country | 500–2,500 · New York, New York, United States |
| 1023 | Gusto | industry, employees, state | Computer Software / Financial Services · 1,500–4,000 · California |
| 1024 | Calendly | employees, state, country | 250–1,200 · Georgia, United States |
| 1025 | Workday | industry, city | Computer Software · Pleasanton |
| 1026 | ServiceNow | employees, country | 18,000–35,000 · United States |
| 1027 | Box | employees, city, state, country (+ industry review) | 1,800–4,000 · Redwood City, California, United States |
| 1028 | Peloton | employees, country | 1,500–5,000 · United States |
| 1029 | Warby Parker | industry, employees, city, state | Retail / Consumer Goods / Apparel & Fashion · 1,500–6,000 · New York, New York |
| 1030 | Chewy | employees, city | 12,000–25,000 · Plantation or Dania Beach |
| 1031 | Expensify | industry, employees, state | Computer Software / Financial Services · 60–300 · Oregon |
| 1032 | Canva | industry, employees, city, state | Computer Software / Internet · 3,000–7,000 · Sydney, New South Wales |
| 1033 | Carvana | industry, employees | Internet / Retail · 8,000–25,000 |
| 1034 | Patagonia | employees, city | 1,500–5,000 · Ventura |
| 1035 | Allbirds | domain, industry, employees | allbirds.com · Apparel & Fashion / Retail / Consumer Goods · 150–1,200 |
| 1037 | Salesforce | city, state | San Francisco, California |
| 1038 | Zendesk | employees | 3,500–8,000 |
| 1039 | Instacart | employees | 2,000–5,000 |
| 1041 | Datadog, Inc. | domain (confirms duplicate) | datadoghq.com |
| 1043 | Delta | see the trap row above | delta.com or unresolved |

## Pass conditions

1. **Shape:** 46 rows out, same Record IDs in the same order, same header. Phone Number, Company
   owner, Create Date, and Lifecycle Stage identical on every row.
2. **Controls:** rows 1001–1009 identical, cell for cell.
3. **Format fixes:** all 19 above, exact.
4. **Cap:** exactly 24 rows enriched; 1018, 1044, 1045, 1046 unchanged and named as queued; the
   cap (24 rows, 3 lookups each) stated in the change log and on the artifact's meta line.
5. **Sources:** every appended value carries a source URL in the change log.
6. **No overwrite:** no non-blank, valid value is replaced by enrichment. 1037, 1038, and 1039's
   wrong values stay in the CSV and appear under "Needs your call" with the proposed value and
   its source.
7. **Duplicates:** 1001+1040, 1003+1042, 1002+1041 listed as the same company; 1004/1005 and
   1005/1043 never listed as the same company.
8. **Could not resolve:** 1036 named with its candidates; nothing appended to it.
9. **Enrichment accuracy:** at least 80% of filled values inside the reference above. A miss is
   checked by hand before it counts: the reference is from general knowledge, the run's source
   may be newer.

1009 is reported as the known limit, not failed.
