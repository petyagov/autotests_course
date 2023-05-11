# Напишите функцию sum_digits, которая принимает положительное число num,
# и возвращает сумму цифр our_sum.
# Например (Ввод --> Вывод) :
#
# 39 --> 12
# 999 --> 27
# 4 --> 4

def sum_digits(num):
    # Здесь нужно написать код
    our_sum = 0
    while num != 0:
        digit = num % 10  # Извлекаем последнюю цифру числа и присваиваем переменной
        our_sum = our_sum + digit  # Добавляем значение переменной digit к значению переменной our_sum
        num = num // 10  # Уменьшаем число на один разряд и снова идём к заголовку цикла
    return our_sum

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')