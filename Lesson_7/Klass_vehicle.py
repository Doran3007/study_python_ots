from dataclasses import dataclass


class Vehicle:
    def __init__(self, Type, weight, height):
        self.Type = Type
        self.weight = weight
        self.height = height


class Car(Vehicle):
    def __init__(self, max_fuel, weight, height, mark, model, color, Type, fuel=100):
        super().__init__(Type, weight, height)
        self.mark = mark
        self.model = model
        self.color = color
        self.max_fuel = max_fuel
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    def launch(self):
        if self.__fuel < 0:
            raise ValueError('Бак не может иметь отрицательное значения кол-ва топлива')
        if self.__fuel == 0:
            raise Exception("Бак пустой, заправьте авто")
        print(f"Двигатель запустился, мы готовы ехать! У нас есть {self.__fuel} литров топлива")

    def add_fuel(self, value):
        self.__fuel += value
        if self.__fuel > self.max_fuel:
            print("Недостаточный обьем бака", 'Залейте на', self.__fuel - self.max_fuel, "литров меньше")
        elif self.__fuel == self.max_fuel:
            print("Полный бак, заправка не требуеться")
        else:
            self.__fuel += value
            print('Бак дозаправлен на', value, 'литров')
        return self.__fuel



class Airplane(Vehicle):
    def __init__(self, Type, weight, height, max_attitude, crew_num, max_passanger, fuel_consumption, fuel):
        super().__init__(Type, weight, height)
        self.max_attitude = max_attitude
        self.crew_num = crew_num
        self.max_passanger = max_passanger
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    def check_fuel(self, distance):
        necessary_fuel = self.fuel_consumption * distance
        if necessary_fuel > self.__fuel:
            diff_fuel = necessary_fuel - self.__fuel
            print(f'Для полета нужно добавить {diff_fuel} литров топлива')
        else:
            print('Мы готовы лететь')


class Ship(Vehicle):
    def __init__(self, Type, weight, height, draft, lifting):
        super().__init__(Type, weight, height)
        self.draft = draft
        self.lifting = lifting

    def check_shallow(self, deep):
        if deep < self.draft:
            diff = self.draft - deep
            print(f'Тут нельзя проплыть, у нас на {diff} м меньше осадка судна')
        else:
            print(f'Глубина  {deep} м,  тут можно смело плыть')


@dataclass
class Engine:
    volum: float
    piston_nums: int
    rpm: int
    max_speed: float
    mileage: float


# Вывод класса Car
# My_car = Car(mark='BMW', model='M3', max_fuel=100, Type='car', weight=1500, height=1.5, color='Black', fuel=50)
# print(My_car.mark, My_car.model)
# My_car.launch()
# My_car.add_fuel(60)

# Вывод класса Airplane
# My_plane = Airplane(Type='Boeing', weight=16000, height=5, max_attitude=1000, crew_num=3, max_passanger=100, fuel_consumption=10, fuel=1500)
# print('Тип самолета:',My_plane.Type, 'Максимальная высота полета:',My_plane.max_attitude)
# My_plane.check_fuel(50)

# Вывод класса Ship     def __init__(self, Type, weight, height, draft, lifting):
# My_Ship = Ship(Type='Tanker', weight=10000, height=20, draft=10, lifting=5000)
# print('Тип судна:', My_Ship.Type, 'Осадка судна:', My_Ship.draft, 'Грузоподьемность судна:', My_Ship.lifting )
# My_Ship.check_shallow(50)