# BOJ_10818

num_cnt = int(input())

num_list = list(map(int, input().split()))


num_max = num_list[0]
num_min = num_list[0]

for i in num_list:

	if num_max <= i:
		num_max = i

	if num_min >= i:
		num_min = i

print(num_min, num_max)
