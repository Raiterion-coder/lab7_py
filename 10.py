import requests
from geopy.distance import geodesic

points = [
    (86.111975, 55.346461),  # Кемерово
    (87.133670, 53.759164),  # Новокузнецк
    (87.980079, 52.929850)  # Шерегеш
]

# Общая длина
itog_distance = 0
for i in range(len(points) - 1):
    itog_distance += geodesic(points[i], points[i + 1]).km

print(f"Общая длина пути: {itog_distance:.2f} км")

# Средняя точка
middle_index = len(points) // 2
middle_point = points[middle_index]

# Параметры для линии и метки
pl_l = ",".join([f"{lon},{lat}" for lon, lat in points])
pt_m = f"{middle_point[0]},{middle_point[1]},pm2rdm"

url = f"https://static-maps.yandex.ru/1.x/?ll=87.133670,55.346461&spn=4.0,4.0&l=map&pl={pl_l}&pt={pt_m}"
response = requests.get(url)

with open("rassto_map.jpg", "wb") as f:
    f.write(response.content)
