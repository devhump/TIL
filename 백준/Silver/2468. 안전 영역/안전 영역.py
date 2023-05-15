from collections import deque

def p_print(list):
    for row in list:
        print(row)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if matrix[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for i in range(N):
    temp = max(matrix[i])
    if temp > max_height:
        max_height = temp

# print(max_height)

max_cnt = 0
for i in range(max_height):    

    for j in range(N):
        for k in range(N):
            if matrix[j][k] == i:
                matrix[j][k] = 0

    # p_print(matrix)
    # print()
    visited = [[False] * N for _ in range(N)]
    # p_print(visited)
    # print()
    
    cnt = 0
    for i2 in range(N):
        for j2 in range(N):
            if not visited[i2][j2] and matrix[i2][j2] != 0:
                dfs(i2, j2) 
                cnt += 1

    # print(f'{i}번째 cnt: {cnt}')

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)