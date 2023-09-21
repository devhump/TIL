#BOJ_10773

T = int(input())

num_list = [0]

for i in range(T):
    num = int(input())

    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))