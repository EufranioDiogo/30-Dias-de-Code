#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = 0
flagSwap = False

for i in range(n):
    flagSwap = False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1
            flagSwap = True
    if flagSwap == False:
        break
print(f'''Array is sorted in {swaps} swaps.
First Element: {a[0]}
Last Element: {a[-1]}''')
