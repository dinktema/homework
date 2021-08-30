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

def count_flats_in_entrance(floors, flats_on_floor):
    count_flats = floors * flats_on_floor
    return count_flats

def find_entrance(flat_num, count_flats):
    entrance = flat_num // count_flats
    if flat_num % count_flats != 0:
        entrance = (flat_num // count_flats) + 1
    return int(entrance)


def find_floor(flat_num, entrance, count_flats, flats_on_floor):
    floor = ((flat_num - count_flats * (entrance - 1)) // flats_on_floor) + 1
    if flat_num % flats_on_floor == 0:
        floor = floor - 1
    elif floor > 1:
        if flat_num < count_flats:
            floor = (flat_num // flats_on_floor) + 1
    return floor



if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    if not floors or floors < 0:
        raise Exception("invalid input data")
    flats_on_floor = int(input("Кол-во квартир на этаже: "))
    if not flats_on_floor or flats_on_floor < 0:
        raise Exception("invalid input data")
    flat_num = int(input("Номер квартиры: "))
    if not flat_num or flat_num < 0:
        raise Exception("invalid input data")

    count_flats = count_flats_in_entrance(floors, flats_on_floor)
    entrance = find_entrance(flat_num, count_flats)
    floor = find_floor(flat_num, entrance, count_flats, flats_on_floor)
    print("entrance = " + str(entrance), "floor = " + str(floor))
