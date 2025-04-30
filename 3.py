import requests

API_KEY = ""
address = "Красная пл-дь, 1, Москва"
url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json"

response = requests.get(url)
data = response.json()

geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
address = geo_object['metaDataProperty']['GeocoderMetaData']['text']
coordinates = geo_object['Point']['pos']

print(f"Адрес: {address}")
print(f"Координаты: {coordinates}")
