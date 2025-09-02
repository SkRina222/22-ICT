# main.py - Лаба 1: створити 10 змінних різних типів, вивести їх значення і типи

user_age = 25                              # int - вік користувача
account_balance = 12345.67                 # float - баланс на рахунку
is_active = True                           # bool - чи активний акаунт
username = "ivan_ivanov"                   # str - ім'я користувача
shopping_list = ["eggs", "milk", "bread"]  # list - список покупок
gps_coordinates = (50.4501, 30.5234)       # tuple - координати (широта, довгота)
permissions = {"read", "write"}            # set - множина прав
settings = {"theme": "dark", "notifications": True}  # dict - налаштування
last_login = None                          # NoneType - час останнього входу (невідомий)
file_bytes = b'\x50\x4b\x03\x04'           # bytes - сирі байти (приклад)

variables = [
    ("user_age", user_age),
    ("account_balance", account_balance),
    ("is_active", is_active),
    ("username", username),
    ("shopping_list", shopping_list),
    ("gps_coordinates", gps_coordinates),
    ("permissions", permissions),
    ("settings", settings),
    ("last_login", last_login),
    ("file_bytes", file_bytes),
]

for name, value in variables:
    print(f"{name} = {value!r}  -> type: {type(value).__name__}")
