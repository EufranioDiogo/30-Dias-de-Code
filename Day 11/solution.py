#!/bin/python3

import math
import os
import random
import re
import sys


def calcular_total(*elementos):
    total = 0

    for elemento in elementos:
        total += elemento
    return total

if __name__ == '__main__':
    arr = []
    a = e = 0
    b = d = f = 1
    c = g = 2
    max_total = 0
    flag_maior = True
    linha = 0

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    while linha < (len(arr) - 2):
        if c == len(arr):
            linha += 1
            a = e = 0
            b = d = f = 1
            c = g = 2

        if linha == len(arr) - 2:
            break
            

        total = calcular_total(arr[linha][a], arr[linha][b], arr[linha][c], arr[linha + 1][d], arr[linha + 2][e], arr[linha + 2][f], arr[linha + 2][g])

        if flag_maior == True:
            max_total = total
            flag_maior = False

        if total > max_total:
            max_total = total

        a += 1
        b += 1
        c += 1
        d = f = b
        e = a
        g = c
        
    print(max_total)