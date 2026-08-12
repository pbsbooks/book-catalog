import pandas as pd
import json
import os

excel_path = os.path.expanduser('~/catalog_updated.xlsx')
df = pd.read_excel(excel_path)

catalog = []
for idx, row in df.iterrows():
    book_id = row.get("Book ID", idx + 1)
    
    # Handle standard zero-padded webp filenames based on ID
    if pd.notna(book_id):
        try:
            cover_filename = f"BK-{int(book_id):05d}.webp"
        except ValueError:
            cover_filename = str(row.get("Cover Image", "placeholder.webp"))
    else:
        cover_filename = "placeholder.webp"

    # Fallback to placeholder if file doesn't exist locally
    cover_path = os.path.join("covers", cover_filename)
    final_cover = cover_filename if os.path.exists(cover_path) else "placeholder.webp"

    catalog.append({
        "id": int(book_id) if pd.notna(book_id) and str(book_id).isdigit() else idx + 1,
        "title": str(row.get("Title", "Unknown Title")),
        "author": str(row.get("Author(s)", "Unknown Author")),
        "category": str(row.get("Category", "General")),
        "price": str(row.get("Price (ETB)", "0")),
        "cover_image": final_cover,
        "language": str(row.get("Language", "English")),
        "publisher": str(row.get("Publisher", "")),
        "format": str(row.get("Format", "PDF")),
        "page_count": str(row.get("Page Count", ""))
    })

with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)

print(f"Successfully created catalog.json with {len(catalog)} entries.")
