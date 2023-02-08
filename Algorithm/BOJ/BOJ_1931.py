# BOJ_1931 회의실 배정 / 그리디

import sys
import heapq

sys.stdin = open("BOJ_1931_input.txt", "r")
# import sys

input = sys.stdin.readline

total_cnt = int(input())

meeting_list = []
for i in range(total_cnt):

    meeting_list.append(tuple(map(int, input().split())))


print(meeting_list)

meeting_list.sort(reverse=True)

#meeting_list.sort(key=lambda meeting: meeting_list[1])

print(meeting_list)
