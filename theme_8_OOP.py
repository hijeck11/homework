# """
# №1. Создайте родительский класс auto, у которого есть атрибуты: brand, age, color, mark and weight. А так же методы; move, birthday и stopю Методы move и stop выводят сообщение на экран....
# """
# class Auto:
#     def __init__(self, brand, age, color, mark, weight):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#
#     def move(self):
#         print('move')
#
#     def stop(self):
#         print('stop')
#
#     def birthday(self):
#         print(self.age + 1)
#
# car1 = Auto('zaz', 30, 'red', '968', 1000)
#
# """
# №2 Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет допонительный .....
# """
# class Truck(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_load):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#         self.max_load = max_load
#
#     def move(self):
#         print('attention')
#         super().move()
#
#     def load(self):
#         import time
#         pause = time.sleep(1)
#         print('load')
#         pause = time.sleep(1)
#
# class Car(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_speed):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print('max speed is:', self.max_speed)
#
# MAN = Truck('MAN', 20, 'black', 'roadwing', 3500, 10)
# DAF = Truck('DAF', 19, 'blue', 'street racing', 4000, 15 )
# print(MAN.color)
# print(DAF.mark)
#
#
# vaz = Car('vaz', 35, 'green', '2109', 1350, 140)
# lada = Car('lada', 15, 'white', 'Priora', 1400, 146)
# print(vaz.mark)
# print(lada.color, lada.max_speed)
"""
№3 Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух
 окружностей, вычитание радиусов произвести по модулю. Если вычитаюстя две окружности с 
 одинаковым значением радиуса, то результатом вычитания будет точка класса Point.
"""

class Circle:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def circle_area(self):
        module_r = abs(self.r1 - self.r2)
        area = 3.14 * module_r*2
        if area == 0:
            print('разница 0')
        else:
            print('Разница окружностей:', area)


a = Circle(8, 5)
a.circle_area()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Circle:
#     def __init__(self, x, y, radius):
#         self.center = Point(x, y)
#         self.radius = abs(radius)
#
#     def subtract(self, other_circle):
#         if self.radius == other_circle.radius:
#             # Если радиусы одинаковы, возвращаем точку
#             return self.center
#         else:
#             # Иначе, возвращаем результат вычитания окружностей
#             radius_difference = abs(self.radius - other_circle.radius)
#             return Circle(self.center.x, self.center.y, radius_difference)
#
# # Пример использования:
# circle1 = Circle(0, 0, 1)
# circle2 = Circle(2, 0, 1)
# result = circle1.subtract(circle2)
#
# if isinstance(result, Point):
#     print(f"Результат - точка: ({result.x}, {result.y})")
# else:
#     print(f"Результат - окружность с радиусом {result.radius}")




