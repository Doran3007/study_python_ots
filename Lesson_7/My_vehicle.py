from Lesson_7.Klass_vehicle import Airplane
from Lesson_7.Klass_vehicle import Car
from Lesson_7.Klass_vehicle import Ship

# Вывод класса Car
print('ВЫВОД КЛАССА АВТОМОБИЛЬ')
My_car = Car(mark='BMW', model='M3', max_fuel=100, Type='car', weight=1500, height=1.5, color='Black', fuel=50)
print(My_car.mark)
print(My_car.model)
My_car.launch()
My_car.add_fuel(60)

# Вывод класса Airplane
print('ВЫВОД КЛАССА САМОЛЕТ')
My_plane = Airplane(Type='Boeing', weight=16000, height=5, max_attitude=1000, crew_num=3, max_passanger=100, fuel_consumption=10, fuel=1500)
print('Тип самолета:', My_plane.Type)
print('Максимальная высота полета:', My_plane.max_attitude)
My_plane.check_fuel(50)

# Вывод класса Ship     def __init__(self, Type, weight, height, draft, lifting):
print('ВЫВОД КЛАССА МОРСКОЕ СУДНО')
My_Ship = Ship(Type='Tanker', weight=10000, height=20, draft=10, lifting=5000)
print('Тип судна:', My_Ship.Type)
print('Осадка судна:', My_Ship.draft)
print('Грузоподьемность судна:', My_Ship.lifting)
My_Ship.check_shallow(50)