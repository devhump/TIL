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
heapq.heappush(full_line, [data[0][0], data[0][1]])

A = 1
for j in range(1, n):

    k = 0
    a = len(full_line)
    while True:
        if full_line[k][1] >= data[j][0]:
            heapq.heappush(full_line[k], data[j][1])
            break
        else:
            if (k + 1) == a:
                heapq.heappush(full_line, [data[j][0], data[j][1]])
                break
            else:
                k += 1

result = 0
for i in range(len(full_line)):
    result += full_line[i][-1] - full_line[i][0]

print(result)
