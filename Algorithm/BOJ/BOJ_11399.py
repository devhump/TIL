# BOJ_11399 ATM / 그리디

cnt = int(input())

time_list = list(map(int, input().split()))

time_list.sort()

temp = 0
total = 0
for num in time_list:
    temp += num
    total += temp

print(total)
