import datetime
import time
import pytest

@pytest.fixture(scope="session")
def class_fixture():
    start_time = time.time()
    print(f"\n 'Начало выполнения класса с тестами'")
    yield
    end_time = time.time()
    print(f'\n Окончание выполнения класса с тестами. Время выполнения: {end_time - start_time} секунд')

@pytest.fixture
def test_fixture():
    start_time = time.time()
    print("Начало выполнения теста")
    yield
    end_time = time.time()
    print(f'\n Окончание выполнения теста. Время выполнения: {end_time - start_time} секунд')