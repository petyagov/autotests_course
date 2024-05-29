# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from task_2 import all_division


@pytest.mark.usefixtures('start_time')
class TestDivisionFunction:
    """Класс с тестами функции деления"""
    @pytest.mark.parametrize('args, result',
                             [
                                 pytest.param([1, 2], 0.5, marks=pytest.mark.smoke),
                                 pytest.param([15, 5, 1], 3, marks=pytest.mark.skip('not now')),
                                 ([999, 111, 2], 4.5),
                                 ([12, 2, 2, 2], 1.5)
                             ])
    def test_positive(self, args, result):
        """Позитивные кейсы деления переданных чисел"""
        assert all_division(*args) == result

    @pytest.mark.usefixtures('running_time')
    @pytest.mark.parametrize('args, exception',
                             [
                                 ((1, 0), ZeroDivisionError),
                                 ((2, '1'), TypeError),
                                 ((), IndexError)
                             ])
    def test_exceptions(self, args, exception):
        """Проверяем наличие исключений при передаче данных отличных от чисел/пустой ввод"""
        with pytest.raises(exception):
            all_division(*args)