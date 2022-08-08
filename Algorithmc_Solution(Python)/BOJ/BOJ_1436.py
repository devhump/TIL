# BOJ_1436. 영화감독 숌

idx = int(input())

# idx = 187
idx -= 1
title_666 = []

for num in range(665, 2666800): #10000번째 수 == 2666799
    
    if "666" in str(num):
        title_666.append(num)

# print(len(title_666)) # 11100
print((title_666[idx]))

# cnt = 1
# while (title_666):
#     print(cnt, title_666.pop(0))
#     cnt += 1