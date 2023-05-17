# SWEA_1966 숫자를 정렬하자 

import sys
sys.stdin = open('SWEA_1966_input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    temp = list(map(int, input().split()))

    temp.sort()

    print(f'#{t+1}', end=" ")
    for i in range(N):
        print(temp[i], end=" ")
    print()