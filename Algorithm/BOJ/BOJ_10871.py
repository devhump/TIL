# import sys

# sys.stdin = open("BOJ_10871_input.txt", 'r')

time, limit = map(int, input().split())

num_list = list(map(int, input().split()))

# print(num_list, len(num_list))

for i in range(time):

    if num_list[i] < limit:
        print(num_list[i], end=' ')