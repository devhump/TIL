cnt = int(input())
call = list(map(int, input().split()))

# cnt = 10
# call = [10, 4, 2, 3, 6, 6, 7, 9, 8, 5]

# call.sort()
# print(call[0])


min_num = call[0]
for i in range(cnt):
	
	if min_num > call[i]:
		min_num = call[i]

print(min_num)