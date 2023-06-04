# SWEA_1220 [S/W 문제해결 기본] 5일차 - Magnetic
#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('SWEA_1220_input.txt', 'r')

T = 10 

for t in range(10):
    N = int(input()) # 100 고정
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 좌로 90도 회전
    rot_matrix = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            rot_matrix[i][j] = matrix[j][100-1-i]

    # @ 각 줄의 0 모두 삭제
    for i in range(100):
        cnt = rot_matrix[i].count(0)
        for j in range(cnt):
            rot_matrix[i].remove(0)

    # @ N, S극 인근 상극 삭제
    for i in range(100):
        while True:
            if rot_matrix[i][0] == 2:
                rot_matrix[i].pop(0)
            else: 
                break
        
        while True:
            if rot_matrix[i][-1] == 1:
                rot_matrix[i].pop()
            else:
                break

    # @ 1, 2 연속선 상에 달라지는 것 카운트
    res = 0
    for i in range(100):
        cnt = 1
        for j in range(1, len(rot_matrix[i])):
            if rot_matrix[i][j-1] != rot_matrix[i][j]:
                cnt += 1

        res += cnt
            
    print(f'#{t+1} {int(res/2)}')