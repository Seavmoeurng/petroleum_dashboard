import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('petroleum_data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)

# Print all sheets and their column headers in excel
print("=== EXCEL SHEETS AND HEADERS ===")
for sname, rows in ext_data['excel'].items():
    print(f"\nSheet: {sname}")
    for idx, r in enumerate(rows[:5]):
        non_empty = [c for c in r if c != '']
        if non_empty:
            print(f"  Row {idx+1}: {non_empty[:8]}")
