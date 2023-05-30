# SWEA_1215 [S/W 문제해결 기본] 3일차 - 회문1
#1 12
#2 10
#3 31
#4 11
#5 1
#6 43
#7 2
#8 11
#9 34
#10 8
def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('SWEA_1215_input.txt', 'r')


import math

T = 10

for t in range(T):
    N = int(input())

    matrix = [list(input()) for _ in range(8)]
    
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            check = True
            for k in range(math.floor(N/2)): # 회문인지 확인
                # @ 쓰면서 이게 될까 했는데 이게 되네.. 파이썬 짱
                if matrix[i][j:j+N][k] != matrix[i][j:j+N][-k-1]: 
                    check = False 
                    continue # 아니면 중단하고 다음 케이스 확인
            if check:
                cnt += 1
            
    # @ 좌로 90도 회전해서
    rot_matrix = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            rot_matrix[i][j] = matrix[j][8-1-i]

    # @ 똑같은 연산 수행
    for i in range(8):
        for j in range(8-N+1):        
            check2 = True
            for k in range(math.floor(N/2)):
                if rot_matrix[i][j:j+N][k] != rot_matrix[i][j:j+N][-k-1]:
                    check2 = False
                    continue
            if check2:
                cnt += 1
            


    print(f'#{t+1} {cnt}')