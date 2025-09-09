numbers = []
words = []
evens = []
upper_words = []

main_data = [7, 14, 27, 6, 21, 33, 9, 18, 25, 4, "кіт", "пес", "миша", "тигр", "лев", "зебра", "слон", "жирафа", "лисиця", "вовк"]

for i in main_data:
    if type(i) == int:
        numbers.append(i)
    elif type(i) == str: 
        words.append(i)

sorted_data = sorted(numbers).extend(sorted(words))

for i in numbers:
    if i % 2 == 0:
        evens.append(i)

for i in sorted(words):
    upper_words.append(i.upper())

print(f"Оригінальні дані: {main_data}")
print(f"Відсортовані числа і слова: {sorted_data}")
print(f"Парні числа: {evens}")
print(f"Слова у верхньому регістрі: {upper_words}")
