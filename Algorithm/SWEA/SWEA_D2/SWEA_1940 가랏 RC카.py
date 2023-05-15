# SWEA_1940 가랏 RC카
#1 3
#2 4
#3 15
#4 27
#5 38
#6 44
#7 240
#8 91
#9 48
#10 111

import sys
sys.stdin = open('SWEA_1940_input.txt', 'r')

T = int(input())

for t in range(T):

    dist = 0   
    n = int(input())
    speed = 0
    for i in range(n):
        cmd = list(map(int, input().split()))

        if len(cmd) == 2:
            if cmd[0] == 1: # 가속이면
                dist += speed + cmd[1] # 현재거리 구하고
                speed += cmd[1] # 속도 조정
            elif cmd[0] == 2: # 감속이면
                temp_spd = speed - cmd[1]
                if temp_spd <= 0:
                    temp_spd = 0
                dist += temp_spd # 현재거리 구하고
                speed -= cmd[1] # 속도조정
                if speed <= 0:
                    speed = 0
        else: # 속도 유지면
            dist += speed

    print(f'#{t+1} {dist}')