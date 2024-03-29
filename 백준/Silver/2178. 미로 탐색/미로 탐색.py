from collections import deque
N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

# p_print(maze)

x , y = 0, 0
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        temp = queue.popleft() 
        for i in range(4):
            nx = temp[0] + dx[i] 
            ny = temp[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[temp[0]][temp[1]] + 1
                queue.append((nx,ny))

bfs(x, y)
print(maze[N-1][M-1])