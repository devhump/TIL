a,b,c = map(int, input().split())

big_num = a if a < b else b

# big_num = big_num if big_num < c else c
# print(big_num)

print(big_num if big_num < c else c)

## 한줄로도 가능
# print((a if a < b else b) if (a if a < b else b) < c else c)