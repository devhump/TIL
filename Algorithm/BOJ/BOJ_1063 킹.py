# BOJ_1063 킹
# print(ord("0"), ord("1"), ord("9")) # 48 49 57
# print(ord("A"), ord("a")) # 65 97

from collections import deque
import sys
sys.stdin = open('BOJ_1063_input.txt', 'r')

# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def p_print(list):
    for row in list:
        print(row)

chess = [[0] * 8 for _ in range(8)]

king, stone, n = map(str, input().split())

queue = deque()
for _ in range(int(n)):
    queue.append(input())

k_x = int(chr(ord(king[0])-17))-1
k_y = (int(king[1])-1) % 8
s_x = int(chr(ord(stone[0])-17))-1
s_y = (int(stone[1])-1) % 8

chess[k_x][k_y] = 'k'
chess[int(chr(ord(stone[0])-17))][int(stone[1])-1] = 's'

p_print(chess)
print("===========")
while queue:
    temp = queue.popleft()

    if temp == "R":
        i = 3
    elif temp == "L":
        i = 2
    elif temp == "B":
        i = 1
    elif temp == "T":
        i = 0
    elif temp == "RT":
        i = -2
    elif temp == "LT":
        i = -4
    elif temp == "RB":
        i = -1
    elif temp == "LB":
        i = -3

    nx = k_x + dx[i]
    ny = k_y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8 and chess[nx][ny] == 0:
        chess[nx][ny] = 'k'
        chess[k_x][k_y] = 0
        k_x, k_y = nx, ny
    elif 0 <= nx < 8 and 0 <= ny < 8 and chess[nx][ny] == 's':
        nsx = s_x + dx[i]
        nsy = s_y + dy[i]

        if 0 <= nsx < 8 and 0 <= nsy < 8:
            chess[nsx][nsy] = 's'
            chess[s_x][s_y] = 'k'
            chess[k_x][k_y] = 0
            s_x, s_y = nsx, nsy
            k_x, k_y = s_x, s_y
    
    p_print(chess)
    print()
print(chr((k_x+66))+str(k_y+1))
print(chr((s_x+66))+str(s_y+1))


