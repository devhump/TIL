# BOJ_2667 단지번호 붙이기_C

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 각 단지마다 집의 개수
cnt = 0
ans = []

# 방문체크용
dist = [[False] * n for _ in range(n)]


def dfs(x, y):
    # 집 개수 증가 & 방문체크
    global cnt
    cnt += 1
    dist[x][y] = True

    # 인접한 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and dist[nx][ny] == False:
                dfs(nx, ny)



# 모든 정점을 확인해서 시작점이 될 수 있는지 확인. 시작점 가능하면 dfs 탐색 ㄱ
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and dist[i][j] == False:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))