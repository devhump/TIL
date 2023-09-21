# BOJ_2178 미로 탐색 

from collections import deque
import sys

from pprint import pprint

sys.stdin = open('BOJ_2178_input.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())


graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

for i in range(N):
    print(graph[i])
    
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
                print(queue)
                graph[nx][ny] = graph[x][y] + 1 # value 자체를 이동 횟수로 사용

for i in range(N):
    print(graph[i])

print(graph[N-1][M-1])

