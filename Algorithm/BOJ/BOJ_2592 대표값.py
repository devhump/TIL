# BOJ_2592 대표값

import sys
sys.stdin = open("BOJ_2592_input.txt")

n = 10

num_li = []
cnt_dict = {}
for i in range(n):

    temp = int(input())
    num_li.append(temp)

    if cnt_dict.get(temp, 0):
        cnt_dict[temp] += 1
    else:
        cnt_dict[temp] = 1

# print(cnt_dict)
cnt_dict = list(cnt_dict.items())
cnt_dict.sort(key = lambda x : (x[1]))


print(int(sum(num_li)//10))
print(cnt_dict[-1][0])