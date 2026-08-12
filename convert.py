import csv
import json
import os

input_csv = 'audit.csv'
output_json = 'catalog.json'

catalog = []

if not os.path.exists(input_csv):
    print(f"Error: {input_csv} not found in current directory.")
    exit(1)

with open(input_csv, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader, start=1):
        # Extract title or fallback to filename/ID
        title = row.get('title') or row.get('filename') or f"Book {idx}"
        cover = row.get('cover_image') or f"{idx}.jpg"
        file_format = row.get('format') or "PDF"

        catalog.append({
            "id": idx,
            "title": title.strip(),
            "cover_image": cover.strip(),
            "format": file_format.strip().upper()
        })

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Successfully created {output_json} with {len(catalog)} entries.")
