"""
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = str()

    def draw(self, subject):
        print(f"Запуск отрисовки {subject}.")


class Pen(Stationery):
    def draw(self):
        super().draw("ручки")


class Pencil(Stationery):
    def draw(self):
        super().draw("карандаша")


class Handle(Stationery):
    def draw(self):
        super().draw("маркера")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()