import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

logo_match = re.search(r'(<img src="data:image/png;base64,[^"]+" alt="Career Width"[^>]*>)', idx_content)
if not logo_match:
    print("Logo not found in index.html")
    exit(1)

logo_tag = logo_match.group(1)

with open('thank-you.html', 'r', encoding='utf-8') as f:
    ty_content = f.read()

# Replace the text/CW placeholder logo with the exact logo image tag
pattern = r'<a href="/" class="flex items-center gap-2\.5">[\s\S]*?</a>'
replacement = f'<a href="/" class="flex items-center gap-3">\n        {logo_tag}\n      </a>'

new_ty_content = re.sub(pattern, replacement, ty_content, count=1)

with open('thank-you.html', 'w', encoding='utf-8') as f:
    f.write(new_ty_content)

print("Successfully synced the exact official Career Width logo to thank-you.html!")
