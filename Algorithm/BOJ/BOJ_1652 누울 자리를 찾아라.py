# BOJ_1652. 누울 자리를 찾아라
# ! 또 어떻게든 테케 답은 냈는데, 틀렸엉...ㅠㅠ

import sys
sys.stdin = open("BOJ_1652_input.txt", "r")


from pprint import pprint

# import sys 
# input = sys.stdin.readline

num = int(input())

con_li = []

# 입력 받기
for i in range(num):
    con_li.append(input())

check = False
# * N by N 이므로
# num = len(con_li[0])
cnt = 0

for k in range(num):
    for j in range(1, num):
        # print(f"{k+1}번째 줄")
        if con_li[k][j] == '.' and con_li[k][j-1] == '.':
            check = True
        else: 
            if check == True:
                cnt += 1
                # print("카운트 했당")
            check = False

    # X가 없다면 → 카운트 안되는 경우 
    if con_li[k].find("X") == -1:
        cnt += 1


rotated_li = [[0] * num for _ in range(num)]

for i in range(num):
    for j in range(num):
        rotated_li[i][j] = con_li[j][num-i-1]

# pprint(rotated_li)

check2 = False
# * N by N 이므로
# num = len(con_li[0])
cnt2 = 0
for k in range(num):
    for j in range(1, num):
        # print(f"{k+1}번째 줄")
        if rotated_li[k][j] == '.' and rotated_li[k][j-1] == '.':
            check2 = True
        else: 
            if check2 == True:
                cnt2 += 1
                # print("카운트 했당")
            check2 = False

    # X가 없다면 → 카운트 안되는 경우 
    if rotated_li[k].count("X") == 0:
        cnt2 += 1


print(cnt, cnt2)
