import json

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('extracted_summary.txt', 'w', encoding='utf-8') as out:
    out.write("==================================================\n")
    out.write("PDF CONTENTS SUMMARY\n")
    out.write("==================================================\n")
    for pdf_name, pages in data['pdfs'].items():
        out.write(f"\n==================== {pdf_name} ====================\n")
        for p in pages:
            out.write(f"\n--- Page {p['page']} ---\n")
            out.write(p['text'] + "\n")

    out.write("\n==================================================\n")
    out.write("EXCEL SHEETS SUMMARY\n")
    out.write("==================================================\n")
    for sheet_name, rows in data['excel'].items():
        out.write(f"\n==================== Sheet: {sheet_name} (Total rows: {len(rows)}) ====================\n")
        for i, r in enumerate(rows):
            non_empty = [c for c in r if c != '']
            if non_empty:
                out.write(f"Row {i+1}: {non_empty}\n")

print("Successfully wrote extracted_summary.txt in UTF-8")
