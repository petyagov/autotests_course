# I. Напишите класс PublicTransport
# Экземпляр класса создается из следующих атрибутов:
#   1. brand - Марка транспорта
#   2. ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя
#   3. year - Год выпуска
#   4. color - Цвет
#   5. max_speed - Максимальная скорость
# У класса должно быть СВОЙСТВО info, которое выводить на печать информацию о:
# марке, цвете, годе выпуска и мощности двигателя
#
# II. Напишите класс Bus унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. passengers - кол-во пассажиров
#   2. ПРИВАТНЫЙ (private) атрибут park - Парк приписки автобуса
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# Добавить свойство park, которое будет возвращать значение park
# а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999
#
# III. Напишите класс Tram унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. ПРИВАТНЫЙ (private) атрибут route - маршрут трамвая
#   2. path - длина маршрута
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# У класса должно быть СВОЙСТВО how_long, которое вычисляет время за прохождение маршрута по формуле max_speed/(4*path)

# Здесь пишем код
class PublicTransport:
    """
    Класс для работы с параметрами общественного транспорта
    """
    def __init__(self, brand, engine_power, year, color, max_speed):
        """
        Функция инициализирует создание объекта общественный транспорт
        :param brand: марка авто
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет авто
        :param max_speed: максимальная скорость
        """
        self.brand = brand
        self._engine_power = engine_power  # защищённый атрибут через _
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property # объявляем метод как свойство
    def info(self):
        """
        Функция выводит на печать информацию о марке, цвете, годе выпуска и мощности двигателя
        :return: марка, цвет, год выпуска, мощность двигателя
        """
        return self.brand, self.color, self.year, self._engine_power


class Bus(PublicTransport):
    """
    Класс для работы с параметрами наследуемого класса PublicTransport и параметрами Автобус
    """
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        """
        Функция инициализирует создание объекта Автобус из наследуемого класса + доп. параметры
        :param brand: марка авто
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет авто
        :param max_speed: максимальная скорость
        :param passengers: кол-во пассажиров
        :param park: парк приписки автобуса
        :param fare: стоимоть проезда
        """
        super().__init__(brand, engine_power, year, color, max_speed) # доступ к унаследованному классу через функцию super()
        self.passengers = passengers
        self.__park =  park  # приватный атрибут Парк приписки автобуса через __
        self._fare = fare  # защищённый атрибут Стоимость проезда через _

    @property  # объявляем метод как свойство
    def park(self):
        """
        Функция возвращает парк приписки автобуса
        """
        return self.__park

    @park.setter  # определяем метод установки свойства, чтобы изменить значение свойства
    def park(self, number):
        """
        Функция проверяет добавленное значение атрибута парка в диапазоне от 1000 до 9999
        :param number: парк приписки автобуса
        """
        if 9999 >= number >= 1000:
            self.__park = number
        assert self.__park == number, "Номер парка не входит в допустимый диапазон"

class Tram(PublicTransport):
    """
    Класс для работы с унаследованным классом PublicTransport и параметрами Трамвай
    """
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        """
        Функция инициализирует создание объекта Трамвай из наследуемого класса + доп. параметры
        :param brand: марка авто
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет авто
        :param max_speed: максимальная скорость
        :param route: маршрут трамвая
        :param path: длина маршрута
        :param fare: стоимоть проезда
        """
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route # приватный атрибут Маршрут трамвая через __
        self.path = path
        self._fare = fare # защищённый атрибут Стоимость проезда через _

    @property  # объявляем метод как свойство
    def how_long(self):
        """
        Функция вычисляет время за прохождение маршрута по формуле max_speed/(4*path)
        :return: время за прохождение маршрута
        """
        time = self.max_speed / (4 * self.path)
        return time



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
transport = PublicTransport('Автомобиль', 500, 2040, 'Фиолетовый', 300)
first_bus = Bus('ЛиАЗ', 210, 2015, 'Зеленый', 100, 70, 1232, 32)
second_bus = Bus('VOLGABUS', 320, 2019, 'Желтый', 110, 39, 1111, 32)
first_tram = Tram('71-931M', 125, 2010, 'Красный', 75, 5, 15, 32)
second_tram = Tram('71-409-1', 240, 2018, 'Белый', 85, 7, 17, 32)

assert isinstance(type(transport).info, property), 'В классе PublicTransport, info - не свойство класса'
assert transport._engine_power, 'В классе PublicTransport, engine_power не защищенный атрибут'
assert first_bus._Bus__park, 'В классе Bus, park не приватный атрибут'
assert second_bus._fare, 'В классе Bus, fare не защищенный атрибут'
assert first_tram._fare, 'В классе Tram, fare не защищенный атрибут'
assert second_tram._Tram__route, 'В классе Tram, route не приватный атрибут'
assert isinstance(type(first_tram).how_long, property), 'В классе Tram, how_long - не свойство класса'
assert first_tram.how_long == 1.25, 'В классе Tram, how_long неверно вычисляется'
assert isinstance(type(second_bus).park, property), 'В классе Bus, park - не свойство класса'
try:
    second_bus.park = 999
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
try:
    second_bus.park = 1234
    print('Проверка на правильность диапазона пройдена')
except AssertionError:
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
try:
    second_bus.park = 10000
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
print('Всё ок')