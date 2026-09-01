import json, os

os.makedirs('books', exist_ok=True)
with open('catalog.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

for b in books:
    bid = b.get('Book ID') or b.get('id')
    title = b.get('Title') or b.get('title') or 'Book'
    author = b.get('Author(S)') or b.get('author') or 'Unknown'
    desc = b.get('Description') or b.get('description') or ''
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title} - Pinnah Book Store</title>
    <meta name="description" content="Buy {title} by {author} on Pinnah Book Store via Telegram.">
    <meta http-equiv="refresh" content="0;url=../index.html?book={bid}">
</head>
<body>
    <h1>{title}</h1>
    <h2>By {author}</h2>
    <p>{desc}</p>
    <a href="https://t.me/Pinnah_Books_Order_Bot?start={bid}">Order on Telegram</a>
</body>
</html>"""
    
    with open(f'books/{bid}.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Static HTML pages generated inside /books/ folder!")
