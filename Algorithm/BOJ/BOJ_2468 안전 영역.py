# BOJ_2468 안전 영역

import sys
sys.stdin = open('BOJ_2468_input.txt', 'r')

def p_print(list):
    for row in list:
        print(row)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    stack = [(a, b)]
    visited[a][b] = True
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not matrix[nx][ny]:
                visited[nx][ny] = True
                stack.append([nx,ny])

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for i in range(N):
    temp = max(matrix[i])
    if temp > max_height:
        max_height = temp

# print(max_height)

max_cnt = 0
for i in range(1, max_height):    

    for j in range(N):
        for k in range(N):
            if matrix[j][k] == i:
                matrix[j][k] = 0

    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i2 in range(N):
        for j2 in range(N):
            if matrix[i2][j2] == 0:
                visited[i2][j2] = True
            else:
                dfs(i2, j2) 
                cnt += 1
    print(f'{i}번째 cnt: {cnt}')

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)