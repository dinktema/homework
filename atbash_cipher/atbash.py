#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z,
 b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""

BLOCK_SIZE = 5
import string


def atbash_encode(text: str) -> str:
    words = text.split()
    cipher = ''
    for word in words:
        word = word.lower()
        for letter in word:
             if letter in string.ascii_lowercase:
                letind = string.ascii_lowercase.index(letter) + 1  #-> int
                newletter = list(string.ascii_lowercase)[len(string.ascii_lowercase) - letind] #-> str
                cipher += newletter
        cipher += ' '
    return cipher


def atbash_decode(cipher: str) -> str:
    cipher = cipher.split()
    text = ''
    for word in cipher:
        for letter in word:
            if letter in string.ascii_lowercase:
                letind = string.ascii_lowercase.index(letter) +1  # -> int shifer
                newletter = list(string.ascii_lowercase)[len(string.ascii_lowercase) - letind]  # -> str
                text += newletter
        text += ' '
    return text

cipfer = 'dzi rh kvzxv uivvwln rh hozevib rtmlizmxv rh hgivmtgs '
text = 'War is Peace,\t Freedom is Slavery,\n Ignorance is Strength.'
print(atbash_encode(text))
print(atbash_decode(cipfer))
