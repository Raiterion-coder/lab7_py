import requests
from bs4 import BeautifulSoup
import random

base_url = "https://quotes.toscrape.com"
all_quotes = []

page = 1
while True:
    url = f"{base_url}/page/{page}/"
    response = requests.get(url)

    if "No quotes found!" in response.text:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        all_quotes.append(f"{text} — {author}")

    page += 1

random_quotes = random.sample(all_quotes, min(5, len(all_quotes)))
for quote in random_quotes:
    print(quote)
