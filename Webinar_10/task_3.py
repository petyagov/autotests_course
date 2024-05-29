# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

@pytest.mark.parametrize("num1, num2, result", [
    (10, 2, 5),
    (20, 4, 5),
    pytest.param(30, 3, 10, marks=pytest.mark.skip),
    pytest.param(40, 5, 8, marks=pytest.mark.smoke)
])
def test_division_parametrize(num1, num2, result):
    assert all_division(num1, num2) == result

    # текст