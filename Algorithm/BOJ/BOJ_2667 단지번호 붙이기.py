from collections import deque, Counter
from functools import reduce

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))
# @ a = [list(map(int,list(input()))) for _ in range(n)]
# @ 이렇게 한 줄로도 입력 가능!

group =[[0]*N for _ in range(N)]

def bfs(a, b, cnt):
    queue = deque([(a, b)])
    group[a][b] = cnt

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1 and group[nx][ny] == 0:
                    queue.append((nx, ny))
                    group[nx][ny] = cnt

cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

# p_print(group)
# [0, 1, 1, 0, 2, 0, 0]
# [0, 1, 1, 0, 2, 0, 2]
# [1, 1, 1, 0, 2, 0, 2]
# [0, 0, 0, 0, 2, 2, 2]
# [0, 3, 0, 0, 0, 0, 0]
# [0, 3, 3, 3, 3, 3, 0]
# [0, 3, 3, 3, 0, 0, 0]

print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기 
ans = reduce(lambda x,y : x+y, group) 
# [0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 0]

# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# [1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]

# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
# [7, 8, 9]

print('\n'.join(map(str,ans))) # ! 모르는 문법도 아닌데, 이렇게 쓰이니 신구하구만!