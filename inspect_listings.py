from bs4 import BeautifulSoup

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.price'):
    print(tag.text)

selectors = [
    '.item',
    '.badge',
    '.free-shipping',
    '.sponsored',
    '#results > li',
    '.item + .item',
    'li.item > a'
]

for selector in selectors:
    print(selector, len(soup.select(selector)))

from lab_selectors import extract_listings

listings = extract_listings(html)
print(len(listings))
print(listings[0])
print(listings[-1])

for listing in listings:
    print(listing['name'])