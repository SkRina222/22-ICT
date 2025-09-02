age = 17  # вік як ціле число (integer)
price = 10.5  # ціна як число з плаваючою комою (float)
name = "Karina"  # ім'я як рядок (string)
is_student = True  # булеве значення: чи є людина студентом (True/False)
classmates = ["Alice", "Bob", "Charlie"]  # список імен однокласників (mutable list)
grades = {"Alice": 90, "Bob": 85, "Charlie": 92}  # словник: ім'я -> оцінка (key-value)
prices = (9.99, 19.99, 29.99)  # кортеж цін (tuple, незмінний)
number = {1, 2, 3, 4, 5}  # множина чисел (set, унікальні елементи)
friends = ["David", "Eva", "Frank"]  # список імен друзів (mutable list)
i_heve_mom = False  # булеве значення: чи є у людини мама (True/False)

a = [age, price, name, is_student, classmates, grades, prices, number, friends, i_heve_mom]  # список усіх змінних
b = 0  # лічильник для нумерації елементів при виведенні

for item in a:  # перебір кожного елемента в списку a
    b += 1  # збільшити лічильник на 1
    print(f"{b} {item} is of type {type(item)}")  # вивести номер, значення та тип елемента
