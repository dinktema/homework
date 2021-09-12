#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
import string


def is_strong_password(pwd: str) -> bool:
    dig = False
    punc = False
    if len(pwd) >= 10 and not pwd.islower() and not pwd.isupper():
        for i in pwd:
            if i in string.digits:
                dig = True
            elif i in string.punctuation:
                punc = True
    if dig and punc:
         return True
    return False

