#!/usr/bin/env python

"""
Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса (FEN - Forsyth–Edwards Notation)
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
Короли с доски не снимаются, поэтому учитывать их нет смысла.

---

Добавьте функцию, которая возвращает строковое представление доски, например, для начальной позиции:

```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
p p p p p p p p
R N B Q K B N R
```
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь


def calc_chess_balance(fen: str) -> int:
    figure = ["q", "r", "b", "n", "p", "Q", "R", "B", "N", "P"]
    cost = [QUEEN_VAL, ROOK_VAL, KNIGHT_VAL, BISHOP_VAL, PAWN_VAL, QUEEN_VAL, ROOK_VAL, KNIGHT_VAL, BISHOP_VAL, PAWN_VAL]
    white_list = []
    black_list = []
    white_price = 0
    black_price = 0
    for i in fen:
        if i.isupper() and i in figure:
            white_list.append(i)
        elif i.islower() and i in figure:
            black_list.append(i)
    for i in white_list:
        white_price = white_price + int(cost[figure.index(i)])
    for i in black_list:
        black_price = black_price + int(cost[figure.index(i)])

    return white_price - black_price


fen = "4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"
print(calc_chess_balance(fen))



def chess_board(fen: str) -> str:
    strings = fen.split(' w ')[0].split('/')
    desk = ''
    for i in strings:
        string = ''
        for e in i:
            if e.isdigit():
                string += '. ' * int(e)
            elif e.isalpha():
                string += e + ' '
        string = string.strip()
        desk += string + '\n'
    return '\n' + desk


fen = "4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"
print(chess_board(fen))



