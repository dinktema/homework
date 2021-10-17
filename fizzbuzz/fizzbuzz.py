#!/usr/bin/env python

"""
Напишите функцию, которая возвращает для чисел:

- кратных 3 - Fizz
- кратных 5 - Buzz
- одновременно кратных и 3 и 5 - FizzBuzz
- строковое представление этих чисел (т.е. "1" для 1)

https://en.wikipedia.org/wiki/Fizz_buzz
"""



def fizzbuzz(n: int) -> str:
    list = []
    for i in range(1, 100 + 1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("Fizzbuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
    return list

print(fizzbuzz(list))
