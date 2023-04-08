a, b = input().split()

a = int(a)
b = int(b)
# print(a, type(a))
num_list = []

for i in range(1, 46):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[a-1:b]))
