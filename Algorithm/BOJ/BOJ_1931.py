# BOJ_1931 회의실 배정 / 그리디

import sys

sys.stdin = open("BOJ_1931_input.txt", "r")
# import sys

input = sys.stdin.readline

total_cnt = int(input())

meeting_list = []
for i in range(total_cnt):

    meeting_list.append(tuple(map(int, input().split())))

cnt_list = []
for j in range(total_cnt):

    end = meeting_list[j][1]

    temp_list = meeting_list[j + 1 :]

    cnt = 0
    for k in range(len(temp_list)):

        if temp_list[k][0] < end:
            continue
        else:
            print(temp_list[k])
            end = temp_list[k][1]
            cnt += 1

    cnt_list.append(cnt)

print(max(cnt_list) + 1)
