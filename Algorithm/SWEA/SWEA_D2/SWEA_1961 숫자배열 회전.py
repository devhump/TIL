# SWEA_1961 숫자배열 회전

import sys
sys.stdin = open('SWEA_1961_input.txt', 'r')

# def p_print(list):
#     for row in list:
#         print(row)

T = int(input())

for t in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    temp90 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp90[i][j] = matrix[N-j-1][i]

    temp180 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp180[i][j] = temp90[N-j-1][i]

    temp270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp270[i][j] = temp180[N-j-1][i]
    
    print(f'#{t+1}')
    for i in range(N):
        for j in range(N):
            print(temp90[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(temp180[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(temp270[i][j], end="")
        print()
        