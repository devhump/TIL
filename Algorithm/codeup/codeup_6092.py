cnt = int(input())

call_list = list(map(int, input().split()))

result = []
for i in range(1, 24):
    result.append(call_list.count(i))

print(*result)