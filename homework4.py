"""
    4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
# Получаем вводные данные от пользователя. Приводм число x по модулю, тем самым невелируем вероятность того, что
# пользователь введен отрицательное число. Число y проверяем на отрицательность
x = abs(int(input("Введите положительное число: ")))
y = int(input("Введите отрицательное число: "))
if y > 0:
    y *= -1


# Первое решение задачи
def my_func_v1(x, y): return x ** y

# Второе решение
def my_func_v2(x, y):
    pow_x = x
    for _ in range(1, abs(y)):
        pow_x *= x
    return 1 / pow_x


print(my_func_v1(x, y))
print(my_func_v2(x, y))
