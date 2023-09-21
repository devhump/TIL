# BOJ_2615 오목

import sys
sys.stdin = open("BOJ_2615_input.txt", "r")

from pprint import pprint

n = 19

Baduck = [input().split() for _ in range(n)]


for i in range(n):
    for j in range(n):
        print(Baduck[i][j], end=" ")
    print()

# 각각 승부결과, 최초 위치, 최장 길이
bk_li = [False, [0,0], 0]
wht_li = [False, [0,0], 0]

bk_li_2 = [[],[],[],[]] # 각각 상하/ 좌우/ 좌상-우하/ 우상-좌하
wht_li_2 = [[],[],[],[]]

# # 상, 좌, 좌상, 우상, 좌하, 우하 순서
dx = [-1, 0,-1, 1]
dy = [0, -1,-1, -1]

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if i == 0: # 상하 일 때
                    if Baduck[nx][ny] == 1 and Baduck[x][y] == 1:
                        bk_li[1] = [nx, ny]
                        bk_li[2] += 1
                        bk_li_2[0] = bk_li
                    elif Baduck[nx][ny] == 2 and Baduck[x][y] == 2:
                        wht_li[1] = [nx, ny]
                        wht_li[2] += 1
                        wht_li_2[0] = bk_li
                if i == 1: # 좌우 일 때
                    if Baduck[nx][ny] == 1 and Baduck[x][y] == 1:
                        bk_li[1] = [nx, ny]
                        bk_li[2] += 1
                        bk_li_2[1] = bk_li
                    elif Baduck[nx][ny] == 2 and Baduck[x][y] == 2:
                        wht_li[1] = [nx, ny]
                        wht_li[2] += 1
                        wht_li_2[1] = bk_li
                if i == 2: # 좌상-우하
                    if Baduck[nx][ny] == 1 and Baduck[x][y] == 1:
                        print("실행2")
                        bk_li[1] = [nx, ny]
                        bk_li[2] += 1
                        bk_li_2[2] = bk_li
                    elif Baduck[nx][ny] and Baduck[x][y] == 2:
                        print("실행3")
                        wht_li[1] = [nx, ny]
                        wht_li[2] += 1
                        wht_li_2[2] = bk_li
                if i == 3: # 우상-좌하
                    if Baduck[nx][ny] == 1 and Baduck[x][y] == 1:
                        bk_li[1] = [nx, ny]
                        bk_li[2] += 1
                        bk_li_2[3] = bk_li
                    elif Baduck[nx][ny] == 2 and Baduck[x][y] == 2:
                        wht_li[1] = [nx, ny]
                        wht_li[2] += 1
                        wht_li_2[3] = bk_li

print(bk_li_2)
print(wht_li_2)