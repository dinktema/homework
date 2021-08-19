#!/usr/bin/env python

# В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде
# <улица> <номер дома>-<номер квартиры>
#
# Приезжая по указанному адресу, Вася видит f-этажное здание.
# Для простоты будем считать, что на каждом этаже в подъезде находятся 4 квартиры.
#
# Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная квартира n.
#
# Для решения понадобится использовать деление по модулю %
# или целочисленное деление //.


def find_entrance(floors, flat_num):
    count_flats_in_entrance = floors * 4
    entrance = flat_num / count_flats_in_entrance
    if entrance != 1:
        entrance = (flat_num // count_flats_in_entrance) + 1
    return entrance


def find_floor(floors, flat_num, entrance, count_flats_in_entrance):
    floor = (flat_num // 4) // entrance
    if not floor:
        if flat_num < floors:
            floor = 1
        else: floor = floors
    elif floor >= 1:
        if flat_num < count_flats_in_entrance:
            floor = ((flat_num // 4) + 1
        else: floor = 1 + ((flat_num // 4) - (floors * entrance))
    elif flat_num <= 4:
        floor = 1

    return floor



if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    if not floors or floors < 0:
        raise Exception("invalid input data")
    flat_num = int(input("Номер квартиры: "))
    if not flat_num or flat_num < 0:
        raise Exception("invalid input data")

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num, entrance)
    print("entrance = " + str(entrance), "floor = " + str(floor))