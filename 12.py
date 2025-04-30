import requests
from bs4 import BeautifulSoup
from collections import defaultdict

base_url = "https://quotes.toscrape.com"
authors = defaultdict(int)

page = 1
while True:
    url = f"{base_url}/page/{page}/"
    response = requests.get(url)

    if "No quotes found!" in response.text:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        author = quote.find('small', class_='author').text
        authors[author] += 1

    page += 1

sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)
for author, count in sorted_authors:
    print(f"{author}: {count} цитат")
