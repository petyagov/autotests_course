# Дан файл 'test_file/task_2.txt'. Можно считать, что это запись покупок в магазине, где указана только цена товара.
# В каждой строке файла записана цена товара.
# Покупки, т.е. несколько подряд идущих цен, разделены пустой строкой.
# Нужно найти сумму трех самых дорогих покупок и записать результат в переменную most_expensive_purchases.
#
#
# Входные данные:
#
# 'test_file/task_2.txt' - путь до файла с записями покупок в магазине
# Выходные данные:
#
# most_expensive_purchases - сумма трех самых дорогих покупок.
#
# Подсказки:
#
#  Hint 1
# Считайте данные из файла с помощью метода readlines.
#  Hint 2
# С помощью функции sorted отсортируйте список цен по возрастанию.
#  Hint 3
# Функция sum поможет найти сумму требуемых элементов.


def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    # Инициализируем переменную для хранения цен покупок
    sum_purchases = 0
    list_purchases = []
    # Читаем файл и собираем цены в список
    with open('test_file/task_2.txt', 'r', encoding='utf-8') as file_purchases:
        for i in file_purchases:
            # Пропускаем пустые строки
            if i == '\n':
                list_purchases.append(sum_purchases)
                sum_purchases = 0
                continue
            sum_purchases += int(i)
    # Вычисляем сумму трех самых дорогих покупок и сортируем список цен в порядке убывания
    three_most_expensive_purchases = sum(sorted(list_purchases)[::-1][0:3])
    assert three_most_expensive_purchases == 202346
    return three_most_expensive_purchases