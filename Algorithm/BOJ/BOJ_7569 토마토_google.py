# BOJ_7569 토마토_google

import sys
sys.stdin = open('BOJ_7569_input.txt', 'r')

# import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 익은 토마토를 큐에 넣음
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k, 0))

# 방향지시자 ⇒ 상, 하, 좌, 우, 위,아래
df = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while queue:
    f, x, y, days = queue.popleft()

    # 인접위치 토마토 확인
    for i in range(6):
        nf = f + df[i]
        nx = x + dx[i]
        ny = y + dy[i]
        ndays = days + 1

        if 0 <= nx < n and 0 <= ny < m and 0 <= nf < h:
            # 안 익은 토마토일 경우 익힘 처리 후 큐에 삽입
            if box[nf][nx][ny] == 0:
                box[nf][nx][ny] = 1
                queue.append((nf, nx, ny, ndays))

# 익지 않은 토마토가 있을 경우 결과값 -1로 변경
for i in range(h):
    for j in range(n):
        if box[i][j].count(0) > 0:
            days = -1
            break

print(days)