from time import time
# Функция квадрата чисел
def square():
    print('Введите числа для возведения в степень:', end=' ')
    nums = map(int, input().split())
    print('Введите значения степени:', end=' ')
    sq = int(input())
    print('Результат:', end=' ')
    num_list = []
    for n in nums:
        n = n**sq
        num_list.append(n)
    print(num_list)



def time_decorator(func):
    def wrapper(*args):
        start_time = time()
        print("Начало операции", start_time)
        res = func(*args)
        end_time = time()
        print("Конец операции", end_time)
        print("Время на выполение", end_time - start_time)
        return res
    return wrapper


@time_decorator
def parity_nums():
    print('Введите числа для проверки:', end=' ')
    nums = map(int, input().split())
    parity_list = []
    unparity_list = []
    for n in nums:
        if n % 2 == 0:
            parity_list.append(n)
        elif n % 2 != 0:
            unparity_list.append(n)
    print('Четные числа:', parity_list)
    print('Нечетные числа:', unparity_list)


parity_nums()

#  square()