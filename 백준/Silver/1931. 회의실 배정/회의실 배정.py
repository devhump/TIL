import sys
from pprint import pprint

# sys.stdin = open("BOJ_1931_input.txt", "r")


N = int(sys.stdin.readline())

time = [[0] * 2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key=lambda x: (x[1], x[0]))

# pprint(time)

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
