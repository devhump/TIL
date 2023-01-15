# BOJ_2170 선 긋기 / 그리디

import sys
import heapq

sys.stdin = open("BOJ_2170_input.txt", "r")
input = sys.stdin.readline


n = int(input())
data = []

for i in range(n):
    data.append(tuple(map(int, input().split())))

data.sort()

full_line = []
heapq.heappush(full_line, data[0][0])  # start point
heapq.heappush(full_line, data[0][1])  # end point

for j in range(1, n):
    # print(full_line)
    if data[j][0] <= full_line[1]:
        # heapq.heappop(full_line[1])
        heapq.heappush(full_line, data[j][1])
    else:
        continue

print(full_line[-1] - full_line[0] + 1)
