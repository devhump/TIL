
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
                matrix[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt

# @ 입력 파트
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

paint = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            paint.append(bfs(i,j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))

