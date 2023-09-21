# BOJ_1292 쉽게 푸는 문제

# result = 0
# for i in range(45):
#     result += (i+1)

# print(result)

a, b = input().split()

a = int(a)
b = int(b)
# print(a, type(a))
num_list = []

for i in range(1, 46):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[a-1:b]))
