# Задача 1
# Дан текстовый файл "test_file/task1_data.txt".
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры, создать файл "test_file/task1_answer.txt" и записать в него получившийся текст.
#
#
# Входные данные:
#
# "test_file/task1_data.txt" - путь до файла с исходными данными
# Выходные данные:
#
# файл "test_file/task1_answer.txt" с итоговыми данными.

#  Hint 1
# Используйте конструкцию with ... as, чтобы открыть файл для чтения или записи.
#  Hint 2
# Используйте метод isdigit, чтобы проверить, является ли символ текста цифрой.


final_str = ''
# Открываем файл для чтения
with open("test_file/task1_data.txt", "r", encoding='utf-8') as file:
    for i in file.read():
        if i.isdigit():
            continue
        final_str += i

# Открываем файл для записи
with open("test_file/task1_answer.txt", "w", encoding='utf-8') as file:
    file.write(final_str)