# BOJ_13567 로봇

import sys
sys.stdin = open('BOJ_13567_input.txt', 'r')

M, n = map(int, input().split())

# todo 이번 델타탐색의 순서는 상-우-하-좌 순서로
# todo 상에서 부터 시계방향으로 배치했다. 
# todo 이유는 문제에서 좌로 90도, 우로 90도를 구현하기 위해
# dxy_al = ["up", "right", "down", "left"]
dxy_mat = [(-1, 0), (0, 1), (1, 0), (0,-1)]
dxy_idx = 2 # * 최초 방향은 아래로 
x, y = 0, 0 # * 최초 출발지점은 0,0으로
check = True # * 로봇이 매트릭스를 벗어나는지 여부 (기본은 정상, True)

for _ in range(n):
    cmd, cnt = input().split()

    if check == False:
        break

    if cmd == "TURN":
        if int(cnt) == 0:
            dxy_idx += -1 
        elif int(cnt) == 1:
            dxy_idx -= -1

        if dxy_idx < 0: 
            dxy_idx += 4 # * 이동 인덱스가 음수가 될 경우
        elif 4 <= dxy_idx: 
            dxy_idx %= 4 # * 이동 인덱스가 3을 초과할 경우
    elif cmd == "MOVE":
        for i in range(int(cnt)):
            
            nx = x + dxy_mat[dxy_idx][0]
            ny = y + dxy_mat[dxy_idx][1]

            if 0 <= nx <= M and 0 <= ny < M: # * 매트릭스 좌표를 벗어난다면
                x = nx
                y = ny
            else:
                check = False # * 올바른 명령어 줄이 아님
                break
    
if check:
    print(x, y)
else:
    print(-1)