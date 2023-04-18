# BOJ_15953 상금헌터

import sys
sys.stdin = open("BOJ_15953_input.txt", "r")

T = int(input())

for t in range(T):
    rank = list(map(int, input().split()))

    result = 0

    if rank[0] == 1:
        result += 500
    elif rank[0] <= 3:
        result += 300
    elif rank[0] <= 6:
        result += 200
    elif rank[0] <= 10:
        result += 50
    elif rank[0] <= 15:
        result += 30
    elif rank[0] <= 21:
        result += 10
    else:
        result += 0

    if rank[1] == 1:
        result += 512
    elif rank[1] <= 3:
        result += 256
    elif rank[1] <= 7:
        result += 128
    elif rank[1] <= 15:
        result += 64
    elif rank[1] <= 31:
        result += 32
    else:
        result += 0

    # cutline = 0
    # for i in range(5):
    #     cutline += 2**i
    #     # print(cutline, int(512//((2**i))))
    #     if rank[1] <= cutline:
    #         result += int(512//((2**i)))
    #         break

    if result == 0:
        print("0")
    else:
        print(str(result) +'0000')