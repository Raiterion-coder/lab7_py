import requests

geo_url = "https://geocode-maps.yandex.ru/1.x/"

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

for city in cities:
    params = {
        "apikey": "fba08131-15fc-486c-822d-28e668154c63",
        "geocode": city,
        "format": "json",
        "results": 1,
        "lang": "ru_RU"
    }

    response = requests.get(geo_url, params=params)
    data = response.json()

    try:
        components = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["Address"]["Components"]

        # Собирает все компоненты типа 'province'
        provinces = [comp["name"] for comp in components if comp["kind"] == "province"]

        # Берет второй, т.е. субъект РФ
        region = provinces[1] if len(provinces) > 1 else provinces[0] if provinces else "Не найден"

        print(f"{city} находится в субъекте РФ: {region}")

    except Exception as e:
        print(f"{city}: ошибка при обработке - {e}")
