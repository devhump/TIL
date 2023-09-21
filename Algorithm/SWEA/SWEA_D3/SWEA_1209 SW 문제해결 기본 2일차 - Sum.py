# SWEA_1209 [S/W 문제해결 기본] 2일차 - Sum

import sys
sys.stdin = open('SWEA_1209_input.txt', 'r')

T = 10

for t in range(T):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    temp = []

    temp3, temp4 = 0, 0
    for i in range(100):
        temp.append(sum(matrix[i])) # 각 행의 합
        temp3 += matrix[i][i] # 좌상단 우하단 대각선의 합
        temp4 += matrix[i][99-i] # 우상단 좌하단 대각선의 합
    temp.append(temp3)
    temp.append(temp4)

    for i in range(100):
        temp2 = 0
        for j in range(100):
            temp2 += matrix[j][i] # 각 열의 합
        
        temp.append(temp2)

    print(f'#{t+1} {max(temp)}')
    
