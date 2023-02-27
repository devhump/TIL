# 22. 개미전사

# N = int(input())
# storages = map(int, input().split())

N = 4
storages = [1, 3, 1, 5]
check = [0] * N

total_sum = sum(storages)
avg = total_sum / N

for i in range(N):
    if storages[i] > avg:
        check[i] = 1

if check.count(1) <= (N / 2) + 1:
    for j in range(len(check) - 1):
        if check[j] == check[j + 1]:
            if storages[j] >= storages[j + 1]:
                check[j + 1] = 0
            else:
                check[j] = 0

result = 0
for i in range(N):
    if check[i] == 1:
        result += storages[i]

print(result)
