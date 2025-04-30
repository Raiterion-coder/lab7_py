import requests
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

profile_links = [
    "http://olympus.realpython.org" + i["href"]
    for i in soup.find_all("a", href=True)
    if i["href"].startswith("/profiles/")
]

for link in profile_links:
    print(link)