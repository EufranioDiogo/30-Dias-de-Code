#!/bin/python3

import math
import os
import random
import re
import sys


def consecutivy_1s(binary_number):
    quant = 1
    consecutivy_1s_quant = 1
    size = len(binary_number)

    for i in range(1, size):
        if binary_number[i] == '1' and binary_number[i - 1] == '1':
            quant += 1
        else:
            if consecutivy_1s_quant < quant:
                consecutivy_1s_quant = quant
            quant = 1
    
    return quant if quant > consecutivy_1s_quant else consecutivy_1s_quant

if __name__ == '__main__':
    n = int(input())
    binary_number = bin(n)[2:]
    number_of_consecutivy_1s = consecutivy_1s(binary_number)
    print(number_of_consecutivy_1s)