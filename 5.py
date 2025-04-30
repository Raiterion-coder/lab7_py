import requests

address = "Петровка, 38, Москва"
url = f"https://geocode-maps.yandex.ru/1.x/?apikey=fba08131-15fc-486c-822d-28e668154c63&geocode={address}&format=json"

response = requests.get(url)
data = response.json()

postal_code = \
data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData'][
    'Address']['postal_code']
print(f"Почтовый индекс: {postal_code}")
