import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://books.toscrape.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

books = []
for item in soup.find_all('article', class_='product_pod'):
    title = item.h3.a['title']
    price = item.find('p', class_='price_color').text
    rating = item.p['class'][1]
    image_rel_url = item.find('img')['src']  # relative image url
    # Fix image URL to absolute
    image_url = 'http://books.toscrape.com/' + image_rel_url.replace('../', '')
    
    books.append({
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Image': image_url
    })

# Save to Excel
df = pd.DataFrame(books)
df.to_excel('products.xlsx', index=False)
print("✅ Scraped and saved to products.xlsx with images")
