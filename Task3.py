class Worker:
    _income = {"wage": 0, "bonus": 0}
    name: str
    surname: str
    position: str

    def __init__(self, name, surname, position, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


# Проверка работы класса

worker = Position("Mark", "Noyanzin", "Programmer", 1000000000, 20000000000)
print(f'name: {worker.name}')
print(f'surname: {worker.surname}')
print(f'full name: {worker.get_full_name()}')
print(f'total income: {worker.get_total_income()}')
