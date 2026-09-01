import json

DOMAIN = "https://pinnahbooks.pages.dev"  # your domain

with open('catalog.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml += f'  <url><loc>{DOMAIN}/</loc><priority>1.0</priority></url>\n'

for b in books:
    book_id = b.get('Book ID') or b.get('id')
    if book_id:
        xml += f'  <url><loc>{DOMAIN}/?book={book_id}</loc><priority>0.8</priority></url>\n'

xml += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)

print("sitemap.xml generated successfully!")
