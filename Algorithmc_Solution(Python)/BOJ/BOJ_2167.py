# BOJ_2167. 2차원 배열의 합

import sys
sys.stdin = open("BOJ_2167_input.txt")

# M: 가로 행
# N: 세로 열

M, N = map(int, input().split())

array_list = []
for i in range(M):
    array_list.append(list(map(int, input().split())))
# print(array_list)

num = int(input())
# print(num)

for i in range(num):
    i, j, x, y = map(int, input().split())
    # print(i, j, x, y)

    i -= 1
    j -= 1
    x -= 1
    y -= 1

    result = 0

    for idx_i in range(i, x+1):
        for idx_j in range(j, y+1):
            result += array_list[idx_i][idx_j]
    
    print(result)

    

