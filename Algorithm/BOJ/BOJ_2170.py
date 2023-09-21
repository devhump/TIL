# BOJ_2170 선 긋기 / 그리디

import sys

sys.stdin = open("BOJ_2170_input.txt", "r")
input = sys.stdin.readline


n = int(input())
data = []

for i in range(n):
    data.append(tuple(map(int, input().split())))

data.sort()

start = data[0][0]
end = data[0][1]

result = 0
for j in range(1, n):

    if data[j][0] <= end and data[j][1] <= end:
        continue
    elif data[j][0] <= end:
        end = data[j][1]
    elif data[j][0] > end:
        result += end - start
        start = data[j][0]
        end = data[j][1]

result += end - start

print(result)

# 원래 힙큐 써서 풀려고 했는데, 계속 시간 초과가 떠서
# 결국 구글링을 했는데, 훨씬 더 간단하게 풀 수 있더라...
