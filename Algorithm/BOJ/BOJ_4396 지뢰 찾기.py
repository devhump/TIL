# BOJ_4396 지뢰 찾기

from pprint import pprint

import sys
sys.stdin = open("BOJ_4396_input.txt", "r")


n = int(input())

mine_map = [list(input()) for _ in range(n)]
open_map = [list(input()) for _ in range(n)]

mat3 = [[0] * n for _ in range(n)]

# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하 순서
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
cnt = 0
mine_check = False # ! 지뢰가 터졌는지 체크한다.
for x in range(n):
    for y in range(n):
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mine_map[nx][ny] == "*":
                    mat3[x][y] += 1 # 8방향 델타 탐색 중 지뢰가 있으면 카운트
                
            if mine_map[x][y] == "*" and open_map[x][y] == "x": # todo 열린 칸에서 지뢰가 있으면
                mine_check = True

# pprint(mine_map)
# pprint(open_map)
# pprint(mat3)
    
if mine_check: # todo 지뢰가 터졌을 때
    for i in range(n):
        for j in range(n):
            if mine_map[i][j] == "*":
                print("*", end="")
            elif mine_map[i][j] == "." and open_map[i][j] == "x":
                print(mat3[i][j], end="")
            else:
                print('.', end="")
        print()
else: # 아닐때
    for i in range(n):
        for j in range(n):
            if open_map[i][j] == "x":
                print(mat3[i][j], end="")
            else:
                print('.', end="")
        print()
