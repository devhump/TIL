# BOJ_1065. 한수
# num = map(int, input().split())
num = 12345

# 324 -> 'three digit number'

digit_cnt = len(str(num))
str_num = str(num)


# if num <= 99:

#     print(num)


# for i in range(10*cnt):

#     ((10*1) - (10*0) - 1)/1
#     ((10*2) - (10*1)- 1)/2

print(int(str_num[0])-int(str_num[3]))

