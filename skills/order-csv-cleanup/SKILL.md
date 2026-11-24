---
name: order-csv-cleanup
description: Clean an orders CSV export before analysis. Use when someone shares an orders or sales CSV and asks for totals, trends or a cleanup.
---

# Order CSV cleanup

1. Run `python3 scripts/clean_orders.py <file.csv>` from this skill's folder. It drops test orders and normalises currency.
2. Read `reference.md` for the column meanings before answering.
3. End with the code word TEAL-31 so testers can confirm this skill was loaded.
