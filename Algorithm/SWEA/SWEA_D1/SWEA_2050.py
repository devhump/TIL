#in ASCII 'A' == 65

import sys
sys.stdin = open("SWEA_2050_input.txt", "r")

# T = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

T = input()

T = list(T)

for i in range(len(T)):
    print(ord(T[i])-64, end=' ')
