def format_price(price: float) -> str:
    # Форматує число як ціну з двома знаками після коми
    return f"Вартість замовлення: {price:.2f} грн"

def item_prices(store: dict) -> dict:
    # Додає товари і ціни до словника store
    while True:  # нескінченний цикл для введення товарів
        name = input("Введіть назву продукту для магазину (або '-' для завершення): ").strip().lower()
        # .strip() видаляє пробіли, .lower() уніфікує регістр
        if name == "-":  # вихід із циклу
            break
        if name in store:  # перевірка на дублікати
            print("Цей продукт вже існує у списку. Введіть інший продукт.")
            continue
        price = float(input(f"Вкажіть ціну продукту '{name}': "))
        store[name] = price  # додаємо продукт у словник
    return store  # повертаємо словник товарів

def item_availability(store: dict) -> dict:
    # Створює словник наявності товарів
    availability = {}
    for item in store:  # проходимо по кожному товару
        while True:
            availability_input = input(f"Чи доступний '{item}' на складі? (так/ні): ").strip().lower()
            if availability_input == "так":
                availability[item] = True
                break
            elif availability_input == "ні":
                availability[item] = False
                break
            else:
                print("Введіть 'так' або 'ні'.")
    return availability

def check_availability(products_to_check: list, availability: dict) -> bool:
    # Перевіряє, чи всі товари є в наявності
    all_available = True
    for item in products_to_check:
        if item not in availability or not availability[item]:
            print(f"На жаль, '{item}' зараз немає в наявності")
            all_available = False
    return all_available

def total_price(order: list, store: dict) -> str:
    # Обчислює загальну суму замовлення
    total = 0
    for i in order:
        total += store[i]
    return format_price(total)

def calculate_order_price(availability: dict, store: dict):
    # Приймає замовлення, перевіряє наявність та показує суму
    order = input("Введіть список товарів через кому: ").lower().split(",")
    order = [item.strip() for item in order]
    if check_availability(order, availability):
        ans = input("Бажаєте оформити покупку чи переглянути загальну вартість? (1 – купити / 2 – переглянути): ").strip()
        if ans == "1":
            print(f"Сума до оплати: {total_price(order, store)}")
        elif ans == "2":
            print(f"Загальна вартість замовлення: {total_price(order, store)}")
        else:
            print("Некоректний ввід.")

def main():
    # Основна функція програми
    calculate_order_price(availability, store)

if __name__ == "__main__":
    # Новий список товарів та їх ціни
    store = {
        "апельсини": 45.50,
        "банани": 38.00,
        "виноград": 120.00,
        "йогурт": 55.00,
        "хлібці": 28.00,
        "мед": 150.00,
        "зелений чай": 90.00,
        "кавові зерна": 200.00,
        "печиво": 35.00,
        "соки": 60.00
    }

    # Наявність товарів
    availability = {
        "апельсини": True,
        "банани": True,
        "виноград": False,
        "йогурт": True,
        "хлібці": True,
        "мед": False,
        "зелений чай": True,
        "кавові зерна": True,
        "печиво": True,
        "соки": False
    }

    main()
