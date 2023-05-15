# BOJ_2468 안전 영역
# todo 코드는 자꾸 보니까 눈에 익는데,
# todo 자꾸 bfs랑 dfs랑 헷갈리는 것 같다. 

import sys
sys.stdin = open('BOJ_2468_input.txt', 'r')

from collections import deque

def p_print(list):
    for row in list:
        print(row)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
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


# @ 입력 파트
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

# @ 최대 높이를 구한다
max_height = 0
for i in range(N):
    temp = max(matrix[i])
    if temp > max_height:
        max_height = temp

max_cnt = 0 # @ 최대 안전 지역 개수를 저장하는 변수
for i in range(max_height):    

    # @ 한번씩 돌릴 때 마다, 낮은 지역 부터 침수 시킨다. == 0
    for j in range(N):
        for k in range(N):
            if matrix[j][k] == i:
                matrix[j][k] = 0

    visited = [[False] * N for _ in range(N)]
    
    # @ 매 회차 단계별 침수를 가정하고, 안전지역 개수를 카운팅한다.
    cnt = 0
    for i2 in range(N):
        for j2 in range(N):
            if not visited[i2][j2] and matrix[i2][j2] != 0:
                bfs(i2, j2) 
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)