"""Drop test orders (email ends with @example.com) and print cleaned row count. Test fixture for eGateway skills dogfooding."""
import csv, sys
rows = [r for r in csv.DictReader(open(sys.argv[1])) if not r.get("email", "").endswith("@example.com")]
print(f"clean rows: {len(rows)}  (marker SCRIPT-RAN-7)")
