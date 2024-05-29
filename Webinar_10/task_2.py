# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Тест на положительные числа
def test_all_division_positive_numbers():
    assert all_division(10, 2, 2) == 2.5

# Тест на отрицательные числа
@pytest.mark.smoke
def test_all_division_negative_numbers():
    assert all_division(-10, 2, -5) == 1

# Тест на числа с плавающей точкой
def test_all_division_float():
    assert all_division(5, 2) == 2.5

# Тест на большие числа
def test_all_division_large_numbers():
    assert all_division(1000, 10, 2, 5) == 10

# Тест на деление на ноль
def test_all_division_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        all_division(20, 5, 0)