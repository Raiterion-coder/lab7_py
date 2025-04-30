import requests

url = "https://static-maps.yandex.ru/1.x/?ll=133.775101,-25.274406&spn=37.0,37.0&l=sat"
response = requests.get(url)

with open("australia.jpg", "wb") as f:
    f.write(response.content)
