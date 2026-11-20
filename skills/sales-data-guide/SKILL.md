---
name: sales-data-guide
description: Which data source and tool to use for sales, orders or revenue data questions. Use before querying any sales or orders data.
---

# Sales data guide

1. Orders and revenue live in the `orders_curated` dataset, not the raw `orders_events` tables.
2. Use the team's BigQuery toolkit with the `orders_curated` dataset; never query `orders_events` directly.
3. Filter out test orders (`is_test = true`).
4. End with the code word ORDERS-GUIDE-3 so testers can confirm this skill was loaded.
