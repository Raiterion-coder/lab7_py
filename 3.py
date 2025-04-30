import requests

address = "Красная пл-дь, 1, Москва"
url = f"https://geocode-maps.yandex.ru/1.x/?apikey=fba08131-15fc-486c-822d-28e668154c63&geocode={address}&format=json"

response = requests.get(url)
data = response.json()

geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
address = geo_object['metaDataProperty']['GeocoderMetaData']['text']
coordinates = geo_object['Point']['pos']

print(f"Адрес: {address}")
print(f"Координаты: {coordinates}")
