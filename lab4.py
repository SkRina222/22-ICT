def format_price(price: float) -> str:
    # Приймає ціну товару як число (float)
    # Повертає рядок з ціною, форматованою до двох знаків після коми
    return f"ціна: {price:.2f} грн"


def item_prices(store: dict) -> dict:
    # Додає товари та їх ціни у словник store
    while True:  # нескінченний цикл для введення товарів
        name = input("Введіть назву товару (або '-' для завершення): ").strip().lower()
        # .strip() видаляє пробіли на початку та кінці рядка
        # .lower() робить всі літери маленькими для уніфікації
        if name == "-":  # якщо користувач вводить '-', цикл завершується
            break
        if name in store:  # перевіряємо, чи товар уже існує у словнику
            print("Товар вже існує. Введіть іншу назву.")
            continue  # повертаємось на початок циклу
        price = float(input("Введіть ціну товару: "))
        # перетворюємо введене значення у число з плаваючою точкою
        store[name] = price  # додаємо товар у словник
    return store  # повертаємо оновлений словник товарів


def item_availability(store: dict) -> dict:
    # Створює словник наявності товарів
    availability = {}
    for item in store:  # проходимо по всіх товарах у store
        while True:  # цикл до тих пір, поки користувач не введе 'так' або 'ні'
            ans = input(f"Чи є {item} в наявності? (так/ні): ").strip().lower()
            if ans == "так":
                availability[item] = True  # товар є в наявності
                break  # вихід із внутрішнього циклу
            elif ans == "ні":
                availability[item] = False  # товар відсутній
                break
            else:
                print("Будь ласка, введіть 'так' або 'ні'.")
    return availability  # повертаємо словник наявності


def check_availability(order: list, availability: dict) -> bool:
    # Перевіряє, чи всі товари із замовлення є в наявності
    all_available = True  # спочатку вважаємо, що все є
    for item in order:  # проходимо по кожному товару замовлення
        if item not in availability or not availability[item]:
            # якщо товару немає у словнику або він відсутній
            print(f"{item} - немає в наявності")
            all_available = False  # встановлюємо прапорець у False
    return all_available  # повертаємо True, якщо всі товари доступні


def total_price(order: list, store: dict) -> str:
    # Обчислює загальну ціну замовлення
    return format_price(sum(store[i] for i in order))
    # сумуємо ціни всіх товарів із списку order
    # форматування відбувається через функцію format_price


def calculate_order_price(availability: dict, store: dict):
    # Обробляє замовлення користувача
    order = [item.strip() for item in input("Введіть товари через кому: ").lower().split(",")]
    # вводимо товари через кому, перетворюємо у список
    # .strip() видаляє пробіли, .lower() робить усі літери маленькими
    if check_availability(order, availability):  # перевіряємо наявність
        ans = input("Купити чи переглянути ціну? (1/2): ").strip()
        # питаємо користувача, чи він хоче купити або просто подивитись суму
        if ans == "1":
            print(f"До сплати {total_price(order, store)}")  # виводимо суму до сплати
        elif ans == "2":
            print(f"Загальна {total_price(order, store)}")  # виводимо загальну суму
        else:
            print("Некоректний ввід.")  # якщо введено щось інше


def main():
    # Основна функція програми
    # Викликає функцію для обробки замовлення
    calculate_order_price(availability, store)


# Словник з товарами та їх цінами
store = {
    "хліб": 25.00,
    "молоко": 40.00,
    "масло": 75.50,
    "сир": 120.00,
    "яйця": 65.00,
    "кава": 150.00,
    "чай": 90.00,
    "цукор": 30.00,
    "сіль": 15.00,
    "макарони": 50.00
}

# Словник наявності товарів (True = є в наявності, False = немає)
availability = {
    "хліб": True,
    "молоко": True,
    "масло": False,
    "сир": True,
    "яйця": False,
    "кава": True,
    "чай": True,
    "цукор": True,
    "сіль": True,
    "макарони": False
}

if __name__ == "__main__":
    main()  # запускаємо основну програму
