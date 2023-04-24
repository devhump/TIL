# BOJ_2178 미로 탐색 

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

#sys.stdin = open('BOJ_2178_input.txt', 'r')

graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0,0)])

# 우 좌 하 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

# BFS
while queue:
    x, y = queue.popleft()
	
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M: # 범위 확인
            if graph[nx][ny] == 1: # 경로 확인
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # value 자체를 이동 횟수로 사용

print(graph[N-1][M-1])

