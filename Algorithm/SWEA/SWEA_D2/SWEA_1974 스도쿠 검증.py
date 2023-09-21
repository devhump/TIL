# SWEA_1974 스도쿠 검증 

import sys
sys.stdin = open('SWEA_1974_input.txt', 'r')

T = int(input())

for t in range(T):
    # 입력 파트
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    check = True

    # 가로 줄 확인
    for i in range(9):
        if sum(sudoku[i]) == 45:
            pass
        else:
            check = False
    
    # 세로 줄 확인
    for i in range(9):
        temp = 0
        for j in range(9):
            temp += sudoku[j][i]
        if temp == 45:
            pass
        else:
            check = False
            break

    # 3 by 3 씩 작은 내부 사각형 확인
    for i in range(3):
        temp, temp1, temp2, temp3 = 0, 0, 0, 0
        for j in range(3):
            for k in range(3):
                temp += sudoku[j][k]
                temp1 += sudoku[j+(3*i)][k]
                temp2 += sudoku[j][k+(3*i)]
                temp3 += sudoku[j+(3*i)][k+(3*i)]
        if temp == 45 and temp1 == 45 and temp2== 45 and temp3 == 45:
            pass
        else:
            check = False
            break

    if check:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
    