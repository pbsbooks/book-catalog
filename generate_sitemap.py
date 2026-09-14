import json

# Load catalog records
with open('catalog.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

# Split into chunks of 2,500 URLs
CHUNK_SIZE = 2500
chunks = [books[i:i + CHUNK_SIZE] for i in range(0, len(books), CHUNK_SIZE)]

# 1. Generate child sitemaps (sitemap1.xml, sitemap2.xml, etc.)
for idx, chunk in enumerate(chunks, start=1):
    filename = f"sitemap{idx}.xml"
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    if idx == 1:
        xml += '  <url><loc>https://pinnahbooks.pages.dev/</loc><priority>1.0</priority></url>\n'
        
    for book in chunk:
        book_id = book.get('id') or book.get('book_id')
        xml += f'  <url><loc>https://pinnahbooks.pages.dev/?book={book_id}</loc><priority>0.8</priority></url>\n'
        
    xml += '</urlset>'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml)

# 2. Generate root Sitemap Index (sitemap.xml)
index_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
index_xml += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for idx in range(1, len(chunks) + 1):
    index_xml += f'  <sitemap><loc>https://pinnahbooks.pages.dev/sitemap{idx}.xml</loc></sitemap>\n'

index_xml += '</sitemapindex>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(index_xml)

print(f"Generated {len(chunks)} sitemaps and 1 sitemap index successfully.")
