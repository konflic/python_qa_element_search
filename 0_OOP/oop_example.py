# # Класс
# class Car:
#     pass
#
#
# # Экземпляр
# # print("##### Экземпляр #####")
#
# # car = Car()
# # print(car)
# # print(isinstance(car, Car))
# #
# # # Атрибуты и методы
# # print("\n##### Атрибуты и методы #####")
#
#
# class Door(object):
#
#     color = "red"
# #
# #     def open(self):
# #         print("I'm opened!")
# #
# #
# # door = Door()
# # print(door.color)
# # door.open()
# #
# # Объект self
# # print("\n##### Объект self #####")
# #
# #
# # class Window:
# #
# #     state = "closed"
# #
# #     def get_state(self):
# #         print("the door is " + self.state + " now")
# #
# #     def open(self, a):
# #         self.state = "opened"
# #         self.get_state()
# #
# #     def close(self):
# #         self.state = "closed"
# #         self.get_state()
# #
# #
# # window = Window()
# # window.open(dskfjh)
# # print(window.state)
# # window.close()
# #
# # # Конструктор
# # print("\n##### Конструктор #####")
# #
# #
# class Animal:
#
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#
#     def make_sound(self):
#         print(self.sound.upper())
#
#     def say_who(self):
#         print("I'm " + str(self.__class__.__name__) + " and my name is " + self.name)
#
# #
# # # Наследование 1
# # print("\n##### Наследование 1 #####")
# #
# #
# # class Bear(Animal):
# #     pass
# #
# #
# # bear = Bear("Baloo", "Hey!")
# # bear.say_who()
#
# # Наследование 2
# print("\n##### Наследование 1 #####")
#
#
# class Lion(Animal):
#
#     def __init__(self, name):
#         super().__init__(name, "arrrrr!")
#
#     def say_who(self):
#         print("I'm LION")
#
#     def hello(self):
#         print("Hello")
#
#
# simba = Lion("Simba")
# # simba.say_who()
# # simba.make_sound()
# # simba.hello()
#
# # Explore class
# print(dir(simba))
