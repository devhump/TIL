num_cnt = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort()

total_sum = 0
for i in range(num_cnt):
    total_sum += A_list[i] * B_list[i]

print(total_sum)