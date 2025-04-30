import requests

API_KEY = "fba08131-15fc-486c-822d-28e668154c63"


def geocode(address, verbose=False):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json"
    response = requests.get(url).json()
    if verbose:
        print(f"Запрос: {address}\nОтвет: {response}\n")
    return response


def get_coordinates(response):
    #    Извлечение координат из ответа геокодера
    pos = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, pos.split())
    return lat, lon


def get_federal_district(response):
    # Извлечение федерального округа из ответа геокодера
    try:
        components = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["Address"]["Components"]
        for component in components:
            if component.get("kind") == "province":
                return component["name"]
        district = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"].get("AdministrativeAreaName",
                                                                                       "Не определен")
        return district
    except Exception as e:
        print(f"Ошибка при определении округа: {e}")
        return "Не определен"


def get_kemgu_postal_code():
    queries = [
        "Кемеровский государственный университет, ул. Красная, 6, Кемерово",
        "КемГУ, Кемерово",
        "Кемеровский госуниверситет"
    ]

    for query in queries:
        response = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={query}&format=json"
        ).json()

        try:
            # Проверка наличия почтового индекса в ответе
            feature = response["response"]["GeoObjectCollection"]["featureMember"][0]
            postal_code = feature["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"].get("postal_code")

            if postal_code:
                return postal_code

        except (KeyError, IndexError):
            continue

    return "Не удалось определить"


# a) Координаты Якутска и Магадана
yakutsk = geocode("Якутск")
magadan = geocode("Магадан")

lat_yakutsk, lon_yakutsk = get_coordinates(yakutsk)
lat_magadan, lon_magadan = get_coordinates(magadan)

print("a) Координаты:")
print(f"Якутск: {lat_yakutsk}° с.ш., {lon_yakutsk}° в.д.")
print(f"Магадан: {lat_magadan}° с.ш., {lon_magadan}° в.д.")
print("Севернее:", "Якутск" if lat_yakutsk > lat_magadan else "Магадан")

# b) Координаты родного города и Торонто
hometown = geocode("Кемерово")
toronto = geocode("Торонто, Канада")

lat_hometown, lon_hometown = get_coordinates(hometown)
lat_toronto, lon_toronto = get_coordinates(toronto)

print("\nb) Координаты:")
print(f"Родной город: {lat_hometown}° с.ш., {lon_hometown}° в.д.")
print(f"Торонто: {lat_toronto}° с.ш., {lon_toronto}° з.д.")
print("Южнее:", "Торонто" if lat_toronto < lat_hometown else "Родной город")

# c) Федеральные округа городов
cities = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград", "Москва"]  # Замените последний на свой город
print("\nc) Федеральные округа:")
for city in cities:
    response = geocode(city)
    district = get_federal_district(response)
    print(f"{city}: {district}")

# d) Почтовый индекс КемГУ
kemgu = geocode("Кемеровский государственный университет, Кемерово")
postal_code = get_kemgu_postal_code()
print("\nd) Почтовый индекс КемГУ:", postal_code)
