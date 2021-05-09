"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = int()
    color = str()
    name = str()
    is_police = bool()
    direction = str()

    def __str__(self):
        return "Текущее состояние: \n" + \
               f'-name: {self.name}\n' + \
               f'-color: {self.color}\n' + \
               f'-speed: {self.speed}\n' + \
               f'-is_police: {self.is_police}\n' + \
               f'-direction: {self.direction}\n'

    def __init__(self, name, color="BLACK", speed=0, is_police=False, direction="ahead"):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.direction = direction

    def show_speed(self):
        print(f'Cкорость: {self.speed}')

    def go(self, speed):
        self.speed = speed
        print("car_going_ahead")

    def stop(self):
        self.speed = 0
        print("Car stopped")

    def turn(self, direction):
        self.direction = direction
        print(f'car_turned_to_{self.direction}')


class TownCar(Car):
    def __init__(self, name, color="BLACK", speed=0):
        super().__init__(name, color, speed)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, name, color="BLACK", speed=0):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def __init__(self, name, color="BLACK", speed=0):
        super().__init__(name, color, speed)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, color="BLACK", speed=0):
        super().__init__(name, color, speed, True)


car1 = TownCar("Lada", "Green", 80)
print(car1)
car1.show_speed()
car1.speed = 20
print(car1)
car1.show_speed()

car2 = WorkCar("Ferrary", "В горошек", 10)
print(car2)
car2.show_speed()
car2.turn("Left")
car2.stop()
print(car2)
