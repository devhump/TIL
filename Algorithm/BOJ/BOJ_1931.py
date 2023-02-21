# BOJ_1931 회의실 배정 / 그리디

import sys
from operator import itemgetter

sys.stdin = open("BOJ_1931_input.txt", "r")


N = int(input())

time = []
for i in range(N):

    time.append(tuple(map(int, input().split())))

time.sort(key=itemgetter(1, 0))

# pprint(time)

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
