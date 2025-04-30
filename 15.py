import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_user_price():
    try:
        return float(input("Введите цену товара: "))
    except ValueError:
        print("Ошибка: Введите число")
        exit()


def fetch_all_products():
    base_site = 'https://scrapingclub.com'
    base_url = 'https://scrapingclub.com/exercise/list_basic/'
    products = []
    page = 1

    while True:
        try:
            url = base_url if page == 1 else f"{base_url}?page={page}"
            response = requests.get(url, verify=False, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', class_='w-full rounded border')

            if not items:
                break

            for item in items:
                name_tag = item.find('h4').find('a') if item.find('h4') else None
                name = name_tag.text.strip() if name_tag else 'Без названия'

                price_tag = item.find('h5')
                price_text = price_tag.text.strip() if price_tag else ''
                try:
                    price = float(price_text.replace('$', '')) if price_text else 0.0
                except:
                    price = 0.0

                img_tag = item.find('img')
                img_path = img_tag['src'] if img_tag else ''
                img_url = f"{base_site}{img_path}" if img_path else 'Нет изображения'

                products.append({
                    'name': name,
                    'price': price,
                    'image': img_url
                })

            page += 1

        except Exception as e:
            print(f"Ошибка при получении данных: {str(e)}")
            break

    return products


def find_closest_product(products, target_price):
    if not products:
        return None

    min_diff = float('inf')
    candidates = []

    for product in products:
        diff = abs(product['price'] - target_price)
        if diff < min_diff:
            min_diff = diff
            candidates = [product]
        elif diff == min_diff:
            candidates.append(product)

    return min(candidates, key=lambda x: x['name']) if candidates else None


def main():
    target_price = get_user_price()
    products = fetch_all_products()

    if not products:
        print("Товары не найдены.")
        return

    result = find_closest_product(products, target_price)

    if result:
        print("\nНайден подходящий товар:")
        print(f"Название: {result['name']}")
        print(f"Изображение: {result['image']}")
        print(f"Цена: ${result['price']:.2f}")
    else:
        print("Подходящих товаров не найдено.")


if __name__ == "__main__":
    main()
