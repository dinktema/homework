#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be >= 0")
    list = [0, 1]
    ind_f = 0   # первый индекс суммирования
    ind_s = 1   # второй индекс суммирования
    if n == 0:
        return 0
    else:
        while len(list) <= n:
            list.append(list[ind_f] + list[ind_s])
            ind_f += 1
            ind_s += 1

    return list[-1]

print(fibonacci(n = 17))
