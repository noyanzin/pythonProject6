class Road:
    _length = float()
    _width = float()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, weight_road_unit: float, thickness: float):
        return self._width * self._length * weight_road_unit * (thickness / 100)


road = Road(20, 5000)
s = road.weight(25, 5)
print(s)
if s != 125000:
    print("Задача решена неправильно!")
else:
    print("Расчет верный!")
