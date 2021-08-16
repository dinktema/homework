#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.

from math import pi

def check(diameter):
    if diameter < 0:
        raise Exception("invalid diameter")

def perimeter(diameter):
    check(diameter)
    return pi * diameter / 2



def square(diameter):
    check(diameter)
    return pi * ((diameter / 2) ** 2)



if __name__ == "__main__":
    diameter = int(input("Диаметр сковородки = "))

    print(perimeter(diameter))
    print(square(diameter))

