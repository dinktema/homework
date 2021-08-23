#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    sum1 = a + b
    sum2 = a + c
    sum3 = b + c
    if sum1 > sum2 and sum1 > sum3:
        return sum1
    if sum2 > sum1 and sum2 > sum3:
        return sum2
    if sum3 > sum1 and sum3 > sum2:
        return sum3
    else:
        print("sums of all coins is same")

if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception("invalid inout data")
    print("max sum of two coins = " + str(max_sum_of_2(a, b, c)))
