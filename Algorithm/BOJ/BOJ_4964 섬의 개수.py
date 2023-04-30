# BOJ_4964 섬의 개수
import sys
sys.stdin = open('BOJ_4963_input.txt', 'r')
from collections import deque

def bfs(x, y):
    island[x][y] = 0 
    # !방문한 좌표는 지도에서 0을 지워버리는 식으로 조건을 통과한다.
    queue = deque([(x,y)])
    # * queue = deque()
    # * queue.append([x,y]) 이렇게 많이들 쓰는 듯
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1: # todo 1일 경우(==이동할 수 있는 경우)
                island[nx][ny] = 0 # todo 방문한 좌표는 0으로 처리
                queue.append([nx, ny]) # todo 다음 이동 좌표 큐에 넣기


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