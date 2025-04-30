import requests

# Координаты
points = [
    ("ЖД Вокзал", "86.083706,55.354378"),
    ("Кардиодиспансер", "86.107405,55.368800"),
    ("Красная Горка", "86.089901,55.354822"),
    ("Кузбасский парк", "86.182871,55.347820")
]

pt_params = "~".join([f"{coord},pm2gnm" for _, coord in points])

url = f"https://static-maps.yandex.ru/1.x/?ll=86.0975,55.3548&spn=0.1,0.1&l=map&pt={pt_params}"
response = requests.get(url)

with open("kemerovo_map.jpg", "wb") as f:
    f.write(response.content)
