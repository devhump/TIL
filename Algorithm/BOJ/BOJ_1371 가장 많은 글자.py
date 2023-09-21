# BOJ_1371 가장 많은 글자

import sys
sys.stdin = open('BOJ_1371_input.txt', 'r')

temp = ""
while True:
    try:
        temp += input().rstrip()
    except EOFError:
        break
temp = list(temp)

alpha_dict = {}
for char in temp:
    if char == ' ':
        pass
    else:
        if alpha_dict.get(char, 0):
            alpha_dict[char] += 1
        else:
            alpha_dict[char] = 1

temp_li = []
for k, v in alpha_dict.items():
    temp_li.append((k, v))

# print(temp_li)
temp_li.sort(key =  lambda x : -x[1])
# print(temp_li)
max_num = temp_li[0][1]

res = []
for i in range(len(temp_li)):
    if temp_li[i][1] == max_num:
        res.append(temp_li[i][0])
# print(res)
res.sort()
# print(res)
ans = ""
for j in range(len(res)):
    ans += res[j]

print(ans)
