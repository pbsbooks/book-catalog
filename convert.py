cat << 'EOF' > convert.py
import pandas as pd
import json
import os

excel_path = os.path.expanduser('~/catalog_updated.xlsx')
df = pd.read_excel(excel_path)

catalog = []
for idx, row in df.iterrows():
    book_id = idx + 1
    
    title_val = str(row.get("Title", "")).strip()
    if title_val == "nan" or not title_val:
        title_val = f"Book {book_id}"

    author_val = str(row.get("Author(s)", "")).strip()
    if author_val == "nan" or not author_val:
        author_val = "Unknown Author"

    cover_filename = f"BK-{book_id:05d}.webp"
    cover_path = os.path.join("covers", cover_filename)
    final_cover = cover_filename if os.path.exists(cover_path) else "placeholder.webp"

    catalog.append({
        "id": book_id,
        "title": title_val,
        "author": author_val,
        "cover_image": final_cover,
        "format": str(row.get("Format", "PDF")),
        "price": str(row.get("Price (ETB)", ""))
    })

with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)

print(f"Successfully generated catalog.json with {len(catalog)} entries.")
EOF
