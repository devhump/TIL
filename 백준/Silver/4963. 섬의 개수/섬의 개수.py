import sys
from collections import deque

def bfs(x, y):
    island[x][y] = 0
    queue = deque([(x,y)])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append([nx, ny])


# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    w, h = map(int, input().split())
    # 종료조건      
    if w == 0 and h == 0:
        break

    island = []
    for i in range(h):
        island.append(list(map(int, input().split())))

    visited = [[False]*w for _ in range(h)]

    cnt = 0 
    for x in range(h):
        for y in range(w):
            if island[x][y] == 1:
                bfs(x, y)
                cnt += 1
                
    print(cnt)