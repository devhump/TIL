# BOJ_2897 몬스터 트럭
# ! 틀린 코드

import sys
sys.stdin = open('BOJ_2897_input.txt', 'r')

R, C = map(int, input().split())

matrix = []
for _ in range(R):
    matrix.append(list(input()))

# # 본인, 우, 우하, 하
dx = [0, 0, 1, 1]
dy = [0, 1, 1, 0]
cnt = 0
# 결과의 종류가 5개 이므로
mon = [0, 0, 0, 0, 0]
for x in range(R-1):
    for y in range(C-1):
        print(matrix[x][y])
        cnt = 0 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if matrix[x][y] == "#":
                cnt = 0
                break
    
            if matrix[nx][ny] == '#':
                cnt = 0 
                break


            if 0 <= nx < R-1 and 0 <= ny < C-1 and matrix[nx][ny] != '#':


                if matrix[nx][ny] == 'X':
                    cnt += 1
                
        if cnt == 1:
            mon[1] += 1
        elif cnt == 2:
            mon[2] += 1
        elif cnt == 3:
            mon[3] += 1
        elif cnt == 4:
            mon[4] += 1    

print(mon)
