# SWEA_1945 간단한 소인수분해

import sys
sys.stdin = open('SWEA_1945_input.txt', 'r')

T = int(input())

for t in range(T):
    num = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0
    while num != 1:

        if num % 2 == 0:
            num /= 2
            num = int(num)
            a += 1
        if num % 3 == 0:
            num /= 3
            num = int(num)
            b += 1
        if num % 5 == 0:
            num /= 5
            num = int(num)
            c += 1
        if num % 7 == 0:
            num /= 7
            num = int(num)
            d += 1
        if num % 11 == 0:
            num /= 11
            num = int(num)
            e += 1

    print(f'#{t+1}',a,b,c,d,e)