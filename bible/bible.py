#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""


from pathlib import Path
from string import punctuation, whitespace
from collections import defaultdict


def most_freq_bible_words(n: int) -> list:
    f = Path(__file__).parent.absolute() / "king_james_bible.txt"
    BIBLE = f.read_text()
    for i in punctuation:
        BIBLE = BIBLE.replace(i, " ")
    for i in whitespace:
        BIBLE = BIBLE.replace(i, " ")
    bible_dict = defaultdict(int)    # def-словарь в котором содежатся пары "слово:колличество повторений"
    for i in BIBLE.lower().split():
        bible_dict[i] += 1
    bible_list_value = sorted(bible_dict.values())         # сортировка поторений
    bible_list = []
    for i in range(1, n + 1):
        for j in bible_dict:
            if bible_dict[j] == bible_list_value[-i]:
                bible_list.append(j)
    return bible_list
