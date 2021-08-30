#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    coins = [a, b, c]
    coins.sort(reverse=True)
    return coins[0] + coins[1]

if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception("invalid inout data")
    print("max sum of two coins = " + str(max_sum_of_2(a, b, c)))
