import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
tags = input("Введите теги через запятую: ").split(",")
tags = [tag.strip().lower() for tag in tags]

found_quotes = set()  # Множество для избежания дубликатов

for tag in tags:
    page = 1
    while True:
        url = f"{base_url}/tag/{tag}/page/{page}/"
        response = requests.get(url)

        if "No quotes found!" in response.text:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quote_tags = [t.text.lower() for t in quote.find_all('a', class_='tag')]

            # Проверка, содержит ли цитата хотя бы один из искомых тегов
            if any(t in quote_tags for t in tags):
                matched_tags = [t for t in quote_tags if t in tags]
                tags_str = ", ".join(matched_tags)
                quote_entry = f"{text} — {author} (теги: {tags_str})"
                found_quotes.add(quote_entry)

        page += 1

for quote in sorted(found_quotes):
    print(quote)
