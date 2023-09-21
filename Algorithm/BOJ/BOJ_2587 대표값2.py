# BOJ_2587 대표값2

num_li = []
for _ in range(5):
    num_li.append(int(input()))

num_li.sort()

print(int((sum(num_li))/5))
print(num_li[2])