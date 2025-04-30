import requests

# Координаты городов
route = [
    "86.089901,55.354867",  # Кемерово
    "86.161734,54.656934",  # Ленинск-Кузнецкий
    "87.109482,53.757535",  # Новокузнецк
    "87.989932,52.920934"  # Шерегеш
]

pl = ",".join(route)

url = f"https://static-maps.yandex.ru/1.x/?ll=86.5,54.5&spn=4.7,4.7&l=map&pl={pl}"
response = requests.get(url)

with open("kemerovo_lom.jpg", "wb") as f:
    f.write(response.content)
