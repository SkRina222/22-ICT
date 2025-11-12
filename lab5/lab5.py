import json
import random
import time
import os
import requests
import datetime
import collections
import logging
import hashlib # MD5 бкзпера данних та перевірка їх цілісності
import csv

# 1. Використання json
try:
    person_data = {"name": "Катерина", "age": 25}
    json_str = json.dumps(person_data, ensure_ascii=False)
    print("JSON рядок:", json_str)
except Exception as err:
    print("Помилка json:", err)


# 2. Використання random
try:
    rand_list = [random.randint(1, 100) for _ in range(5)]
    print("Список випадкових чисел:", rand_list)
except Exception as err:
    print("Помилка random:", err)


# 3. Використання time
try:
    start_time = time.time()
    time.sleep(0.5)
    print(f"Час виконання: {time.time() - start_time:.3f} секунд")
except Exception as err:
    print("Помилка time:", err)


# 4. Використання os
try:
    current_dir = os.getcwd()
    print("Поточний каталог:", current_dir)
except Exception as err:
    print("Помилка os:", err)


# 5. Використання datetime
try:
    now = datetime.datetime.now()
    print("Поточний час:", now.strftime("%Y-%m-%d %H:%M:%S"))
except Exception as err:
    print("Помилка datetime:", err)
