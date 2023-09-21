# BOJ_1453 피시방 알바

n = int(input())
    
temp_li = list(map(int, input().split()))

pc_dict = {}
cnt = 0
for i in range(n):
    tem = temp_li.pop()    
    if pc_dict.get(tem, 0):
        pc_dict[tem] += 1
    else:
        pc_dict[tem] = 1

res = 0
for k, v in pc_dict.items():
    res += (v - 1)

print(res) 