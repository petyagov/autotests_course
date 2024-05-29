# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

# Здесь пишем код


import random
import string

def generate_random_name():
    """Генерим строку длинной от 1 до 15 символов, разделенных пробелом из латинских букв
    и составляем строку из 2-х слов, полученных с помощью генератора"""
    while True:
        word1 = ''.join(random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(1, 15)))
        word2 = ''.join(random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(1, 15)))
        yield f"{word1} {word2}"

gen = generate_random_name()
# Вызываем функцию next() для получения следующей случайно сгенерированной пары слов
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

