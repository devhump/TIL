# SWEA_1216 [S/W 문제해결 기본] 3일차 - 회문2
# ! 으아... 답이 안 나온다아...
#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18

import sys
sys.stdin = open('SWEA_1216_input.txt', 'r')


import math

T = 10

for t in range(T):
    N = int(input())

    matrix = [list(input()) for _ in range(100)]
    
    max_cnt = 0
    for i in range(100):    
        for j in range(99, -1, -1):
            for k in range(100-j):
                if matrix[i][k:j+k] == matrix[i][k:j+k][::-1]: 
                    if len(matrix[i][k:j]) > max_cnt:
                        max_cnt = len(matrix[i][k:j+1])
                        break
    # @ 좌로 90도 회전해서
    rot_matrix = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            rot_matrix[i][j] = matrix[j][100-1-i]

    for i in range(100):    
        for j in range(99, -1, -1):
            for k in range(100-j):
                if rot_matrix[i][k:j+k] == rot_matrix[i][k:j+k][::-1]: 
                    if len(rot_matrix[i][k:j]) > max_cnt:
                        max_cnt = len(rot_matrix[i][k:j])
                        break
    print(f'#{t+1} {max_cnt}')