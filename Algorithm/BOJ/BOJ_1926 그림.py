# BOJ_1926 그림

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('BOJ_1926_input.txt', 'r')

from collections import deque

def bfs(x, y):
    queue = deque([(x,y)])    
    matrix[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0 # ! 이게 포인트...
                queue.append((nx,ny))
                cnt += 1 
                # * 여기서 1이 연속된 수치, 
                # *즉 가장 큰 너비의 그림 넓이를 구한다.
    return cnt # ! 포인트2

# @ 입력 파트
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# @ 실행파트
paint = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            paint.append(bfs(i,j)) # * 여기서 매 그림의 넓이를 빈 리스트에 넣는다.

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))

