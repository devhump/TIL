# SWEA_1208 [S/W 문제해결 기본] 1일차 - Flatten


import sys
sys.stdin = open('SWEA_1208_input.txt', 'r')

T = 10

for t in range(T):

    N = int(input())
    boxes = list(map(int, input().split()))

    boxes.sort()

    for i in range(N):
        boxes[-1] -= 1
        boxes[0] += 1

        boxes.sort()

    print(f'#{t+1} {boxes[-1]-boxes[0]}')