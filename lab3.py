# Створюємо порожній словник для збереження балів студентів
grades = {}

# Введення даних про студентів
while True:
    student_name = input("Введіть ім'я учня (або 'stop' для завершення введення): ").strip()
    # Перевірка на завершення введення
    if student_name.lower() == 'stop':
        break
    try:
        # Введення оцінки студента
        score = int(input(f"Вкажіть бал для {student_name} (1-12): ").strip())
        if score < 1 or score > 12:
            print("Помилка: бал повинен бути від 1 до 12. Спробуйте ще раз.")
            continue
        grades[student_name] = score  # Додаємо студента і його бал у словник
    except ValueError:
        print("Будь ласка, введіть ціле число від 1 до 12.")
        continue

# Вивід списку студентів та їх балів
print("\nСписок учнів і їхні бали:")
for student, score in grades.items():
    print(f"{student}: {score}")

# Обчислення середнього балу класу
if grades:
    average_score = sum(grades.values()) / len(grades)
    print(f"\nСередній бал класу: {average_score:.2f}")

# Розподіл студентів за категоріями
top_students = []       # відмінники 10-12
good_students = []      # хорошисти 7-9
average_students = []   # середні 4-6
failing_students = []   # не склали 1-3

for student, score in grades.items():
    if 10 <= score <= 12:
        top_students.append(student)
    elif 7 <= score <= 9:
        good_students.append(student)
    elif 4 <= score <= 6:
        average_students.append(student)
    elif 1 <= score <= 3:
        failing_students.append(student)

# Вивід категорій студентів
print(f"\nВідмінники ({len(top_students)}): {', '.join(top_students) if top_students else 'немає'}")
print(f"Хорошисти ({len(good_students)}): {', '.join(good_students) if good_students else 'немає'}")
print(f"Середні ({len(average_students)}): {', '.join(average_students) if average_students else 'немає'}")
print(f"Не склали ({len(failing_students)}): {', '.join(failing_students) if failing_students else 'немає'}")
