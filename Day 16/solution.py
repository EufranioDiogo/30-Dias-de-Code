#!/bin/python3

import sys


S = input().strip()

try:
    S = int(S)
    print(S)
except (TypeError, ValueError):
    print('Bad String')
