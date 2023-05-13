

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque([(a, b)])

    matrix[a][b] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft() # @ 이렇게 한번에 뽑기가 가능하군!

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    queue.append((nx,ny))
                    matrix[nx][ny] = 0
                    cnt += 1
    if cnt != 0:
        ans.append(cnt)
                    
N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

ans = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            bfs(i,j)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])