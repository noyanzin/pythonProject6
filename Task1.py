import threading
import time


class Color:
    RED = 0
    YELLOW = 1
    GREEN = 2


class SingleLight:
    color: Color
    duration: int

    def __str__(self):
        c = ['RED', 'YELLOW', 'GREEN'][self.color]
        return f"Color: {c}, duration: {self.duration}"

    def __init__(self, color, duration):
        self.color = color
        self.duration = duration


class TrafficLight:
    __color = Color.RED
    __lights = dict()
    __light_number = 0
    __timer: threading.Timer

    def running(self):
        self.__timer.cancel()
        self.next_light()
        light = self.__lights[self.__light_number]
        print(f'{time.time()}:light_number = {self.__light_number} {light}')
        self.__timer = threading.Timer(light.duration, self.running)
        self.__timer.start()

    def next_light(self):
        before_light = self.__light_number
        # Выбор следующего цвета
        if self.__light_number == 2:
            self.__light_number = 0
        else:
            self.__light_number += 1
        # Проверка правильности переключения светофора
        if (self.__light_number == 2 and before_light != 1) or \
            (self.__light_number == 1 and before_light != 0) or \
            (self.__light_number == 0 and before_light != 2):
            print("Неправильный порядок переключения светофора!")
            exit()

    def __init__(self):
        self.__lights = [
            SingleLight(Color.RED, 7),
            SingleLight(Color.YELLOW, 2),
            SingleLight(Color.GREEN, 5)]
        self.__timer = threading.Timer(self.__lights[1].duration, self.running)
        self.__timer.start()


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()

for i in range(0, 100):
    time.sleep(1)
    print(i)

