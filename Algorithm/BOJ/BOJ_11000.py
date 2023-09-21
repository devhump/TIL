# BOJ_11000 강의실 배정 / 그리디

import sys
import heapq

sys.stdin = open("BOJ_11000_input.txt", "r")

input = sys.stdin.readline


n = int(input())
class_list = []

for i in range(n):
    class_list.append(tuple(map(int, input().split())))

class_list.sort()

room = []
heapq.heappush(room, class_list[0][1])

for j in range(1, n):
    print(room)
    if class_list[j][0] < room[0]:
        heapq.heappush(room, class_list[j][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, class_list[j][1])

print(room)
print(len(room))
