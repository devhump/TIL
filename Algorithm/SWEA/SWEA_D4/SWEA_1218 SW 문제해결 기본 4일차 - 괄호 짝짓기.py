# SWEA_1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
#1 0
#2 0
#3 1
#4 1
#5 1
#6 0
#7 0
#8 1
#9 0
#10 1



import sys
sys.stdin = open('SWEA_1218_input.txt', 'r')

T = 10

for t in range(T):
    N = int(input())

    brackets = list(input())

    temp = []
    for i in range(N):
        temp.append(brackets[i])

        if N % 2 != 0:
            flag = False
            break

        if len(temp) >= 2:
            if temp[-2] == "(" and temp[-1] == ")":
                temp.pop()
                temp.pop()
            elif temp[-2] == "<" and temp[-1] == ">":
                temp.pop()
                temp.pop()
            elif temp[-2] == "[" and temp[-1] == "]":
                temp.pop()
                temp.pop()
            elif temp[-2] == "{" and temp[-1] == "}":
                temp.pop()
                temp.pop()

    # print(brackets)
    if len(temp) == 0:
        flag = True
    else:
        flag = False

    if flag:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
