#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    n_list = []    #делим посимвольно в виде списка
    while n > 0:
        n_list.append(n % 10)   #определяем первый символ
        n //= 10                #определяем последний символ
    rev = list(reversed(n_list))   #сравниваем с обратным списком
    if n_list == rev:
        return True
    else:
        return False

