# SWEA_1217 [S/W 문제해결 기본] 4일차 - 거듭 제곱 

#1 43046721
#2 256

import sys
sys.stdin = open('SWEA_1217_input.txt', 'r')



def pow_multiple(a,b, res):
    if b > 0:
        res *= a
        res = pow_multiple(a, b-1, res)
    return res

T = 10

for t in range(T):
    N = int(input())


    a, b = map(int, input().split())
    res = 1
    print(f'#{N} {pow_multiple(a, b, res)}')