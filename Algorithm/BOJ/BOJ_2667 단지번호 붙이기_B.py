# BOJ_2667 단지번호 붙이기_B

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    queue = deque([(x, y)])

    while queue:
        temp = queue.pop()

        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = cnt
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                else:
                    visited[nx][ny] = True
N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))

visited = [[False]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            bfs(i,j, cnt)

# def p_print(list):
#     for row in list:
#         print(row)

# p_print(matrix)

res = []
for i in range(N):
    res.extend(matrix[i])

apt_cnt = max(res)
ans = []
for i in range(1, apt_cnt+1):
    ans.append(res.count(i))
ans.sort()
print(apt_cnt)
for i in range(apt_cnt):
    print(ans[i])
