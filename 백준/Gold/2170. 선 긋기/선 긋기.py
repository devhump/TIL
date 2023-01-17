import sys

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
