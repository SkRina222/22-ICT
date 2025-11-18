
def pair_generator(filepath, target_pairs, encoding="utf-8"):
    # Генератор біграм усередині одного слова
    def get_pairs(word):
        for i in range(len(word) - 1):
            yield word[i:i+2]

    with open(filepath, "r", encoding=encoding) as f:
        for line in f:
            words = line.strip().split()
            if not words:
                continue
            # лічильник для поточного рядка
            found = {pair: 0 for pair in target_pairs}

            for word in words:
                word = word.lower()

                # біграми лише всередині слова
                for pair in get_pairs(word):
                    if pair in found:
                        found[pair] += 1

            # повертаємо кортеж кількостей у порядку target_pairs
            yield found


# ======== Використання генератора ========

pairs = ["но", "ен", "ий"]  # шукані пари
a = 1

for result in pair_generator("text.txt", pairs):
    print(f"line {a} --- {result}")
    a += 1

    
