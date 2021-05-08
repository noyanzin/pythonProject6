import threading
import time


class Color:
    RED = 1
    YELLOW = 2
    GREEN = 3


class SingleLight:
    color: Color
    duration: int

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
        if self.__light_number == 3:
            self.__light_number = 1
        else:
            self.__light_number += 1
        print(f'light_number = {self.__light_number}')
        light = self.__lights[self.__light_number]
        print(f'{time.time()}: color: {light.color}, duration: {light.duration}')
        self.__timer = threading.Timer(light.duration, self.running)
        self.__timer.start()

    def __init__(self):
        self.__lights[1] = SingleLight(Color.RED, 7)
        self.__lights[2] = SingleLight(Color.YELLOW, 2)
        self.__lights[3] = SingleLight(Color.GREEN, 5)
        self.__timer = threading.Timer(self.__lights[1].duration, self.running)
        self.__timer.start()


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()

for i in range(0, 100):
    time.sleep(1)
    print(i)

