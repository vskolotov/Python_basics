"""
 Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Пишем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рируем карашдашом")


class Handle(Stationery):
    def draw(self):
        print("Закрашиваем фломастером")


brush = Stationery('Белка')
print(brush.title)
brush.draw()
pen = Pen('Erich Krause')
print(pen.title)
pen.draw()
pencil = Pencil('Buro')
print(pencil.title)
pencil.draw()
handle = Handle('Silwerhof')
print(handle.title)
handle.draw()
