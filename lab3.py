grades = {}

while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ").strip()
    if name.lower() == 'stop':
        break
    try:
        grade = int(input(f"Введіть оцінку для {name} (1-12): ").strip())
        if grade < 1 or grade > 12:
            print("Оцінка має бути від 1 до 12. Спробуйте ще раз.")
            continue
        grades[name] = grade
    except ValueError:
        print("Будь ласка, введіть ціле число для оцінки.")
        continue

print("\nСписок студентів та їх оцінки:")
for student, score in grades.items():
    print(f"{student}: {score}")

if grades:
    average = sum(grades.values()) / len(grades)
    print(f"\nСередній бал по групі: {average:.2f}")

excellent_students = []  # відмінники 10-12
good_students = []       # хорошисти 7-9
average_students = []    # відстаючі 4-6
failed_students = []     # не здали 1-3

for student, score in grades.items():
    if 10 <= score <= 12:
        excellent_students.append(student)
    elif 7 <= score <= 9:
        good_students.append(student)
    elif 4 <= score <= 6:
        average_students.append(student)
    elif 1 <= score <= 3:
        failed_students.append(student)


print(f"\nВідмінники ({len(excellent_students)}):")
for student in excellent_students:
    print(f"- {student}")

print(f"\nХорошисти ({len(good_students)}):")
for student in good_students:
    print(f"- {student}")

print(f"\nВідстаючі ({len(average_students)}):")
for student in average_students:
    print(f"- {student}")

print(f"\nНе здали ({len(failed_students)}):")
for student in failed_students:
    print(f"- {student}")
