import requests

API_KEY = ""

cities = input("Введите города через запятую: ").split(",")
cities = [city.strip() for city in cities]

coordinates = []
for city in cities:
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city}&format=json"
    response = requests.get(url)
    data = response.json()

    pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    lat = float(pos.split()[1])
    coordinates.append((city, lat))

southernmost = min(coordinates, key=lambda x: x[1])
print(f"Самый южный город: {southernmost[0]}")
