# Лаба 4 створити функцію яка буде приймати ціну та повертати їх у форматі 'ціна: xxx.xx грн'. 
# Створити функцію яка буде приймати довільну кількість товарів та повертати словник в якому буде лише передані товари як ключі та тру або 
# фолс відповідно чи вони наявні в магазиці створити функцію яка буде приймати замовлення в користувача та видавати інфу про ціну. 
# Замовлення можливе лише якщо всі вибрані товари є в наявності. В користувача має бути дві опції купити і переглянути ціну

def format_price(price: float) -> str:
    # Форматує число як ціну з двома знаками після коми
    return f"ціна: {price:.2f} грн"

def item_availability (item: list) -> dict:
    # Додає товари і їх наявність до словника availability
    availability = {}
    for name in item:
        while True:
            status = input(f"Чи є продукт '{name}' в наявності? (так/ні): ").strip().lower()
            if status in ['так', 'ні']:
                availability[name] = (status == 'так')  # зберігаємо True або False
                break
            else:
                print("Будь ласка, введіть 'так' або 'ні'.")
    print(availability)
    return availability  # повертаємо словник наявності

def item_prices(stores: list) -> dict:
    store = {}
    for name in stores:
        while True:
            try:
                price = float(input(f"Введіть ціну для продукту '{name}': ").strip())
                store[name] = format_price(price)
                break
            except ValueError:
                print("Будь ласка, введіть коректну числову ціну.")
    print(store)
    return store
    
def check_availability(products_to_check: list, availability: dict) -> bool:
    # Перевіряє, чи всі товари є в наявності
    all_available = True
    for item in products_to_check:
        if item not in availability or not availability[item]:
            print(f"На жаль, '{item}' зараз немає в наявності")
            all_available = False
    return all_available

def total_price(order: list, store: dict) -> str:
    total = 0
    for i in order:
        # Беремо значення, наприклад "Вартість замовлення: 25.50 грн"
        text = store[i]
        
        # Витягуємо частину між двокрапкою і "грн"
        start = text.find(":") + 1
        end = text.find("грн")
        
        # Вирізаємо цю частину і очищаємо від пробілів
        number_part = text[start:end].strip()
        
        # Замінюємо кому на крапку, якщо є, і переводимо в число
        price = float(number_part.replace(",", "."))
        
        total += price

    return total

def calculate_order_price(availability: dict, store: dict):
    # Приймає замовлення, перевіряє наявність та показує суму
    while True:
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
            break
        
def main():
    # Основна функція програми
    items = input("Введіть список товарів через кому: ").lower().split(",")
    items = [item.strip() for item in items]
    availability = item_availability(items)
    store = item_prices(items)
    
    calculate_order_price(availability, store)

if __name__ == "__main__":
    main()
