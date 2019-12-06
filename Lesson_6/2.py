"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof
from sys import getsizeof


class Vehicle(object):
    """docstring"""
    __slots__ = ('color', 'doors', 'tires')

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"


BC_OBJ = Vehicle('green', 5, 4)
print(BC_OBJ.__slots__)
print(asizeof.asizeof((BC_OBJ)))
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4)
#     print(car.color)
#
#     truck = Vehicle("red", 3, 6)
#     print(truck.color)


"""Реализация без слотов
{'color': 'green', 'doors': 5, 'tires': 4}
264
----------------------------------------
При реализации со слотами - 
('color', 'doors', 'tires')
104

Отсюда вывод что заранее выделенная память в таких случаях эффективней( в данном случае более чам в 2 с половиной раза)
"""
