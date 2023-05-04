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

k_x = (int(chr(ord(king[0])-17))%8)
k_y = (int(king[1])) -1
s_x = (int(chr(ord(stone[0])-17))%8)
s_y = (int(stone[1])) -1

chess[k_x][k_y] = 'k'
chess[s_x][s_y] = 's'


p_print(chess)

rot_chess = [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        rot_chess[i][j] = chess[j][8-i-1]

for i in range(8):
    for j in range(8):
        if rot_chess[i][j] == 'k':
            chess[k_x][k_y] == 0
            k_x, k_y = i, j
        if rot_chess[i][j] == 's':
            chess[s_x][s_y] == 0
            s_x, s_y = i, j

print([k_x,k_y], [s_x,s_y])
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

    if 0 <= nx < 8 and 0 <= ny < 8 and rot_chess[nx][ny] == 0:
        rot_chess[nx][ny] = 'k'
        rot_chess[k_x][k_y] = 0
        k_x, k_y = nx, ny
    elif 0 <= nx < 8 and 0 <= ny < 8 and rot_chess[nx][ny] == 's':
        nsx = s_x + dx[i]
        nsy = s_y + dy[i]

        if 0 <= nsx < 8 and 0 <= nsy < 8:
            rot_chess[nsx][nsy] = 's'
            rot_chess[s_x][s_y] = 'k'
            rot_chess[k_x][k_y] = 0
            s_x, s_y = nsx, nsy
            k_x, k_y = s_x, s_y
    
    p_print(rot_chess)
    print()
print(chr((k_x+65))+str(k_y+1))
print(chr((s_x+65))+str(s_y+1))


