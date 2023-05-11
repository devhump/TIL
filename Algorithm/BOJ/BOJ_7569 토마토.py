# BOJ_7569 토마토

import sys
sys.stdin = open('BOJ_7569_input.txt', 'r')

M, N, H = map(int, input().split())

matrix = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        matrix[i].append(list(map(int, input().split())))

print(matrix)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0
for i in range(4):
    
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < M and 0 <= ny < N and matrix[x][y] == 1:
        matrix[nx][ny] = 1
        

