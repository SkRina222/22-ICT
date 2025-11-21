from deco import readonly

# Приклад використання:
@readonly
def test():
    return "Перша версія"

print(test())  # Перша версія

# Спроба перевизначити
@readonly
def test():
    return "Друга версія"

print(test())  # Все одно: Перша версія
