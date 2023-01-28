# BOJ_1463 1로 만들기 / DP


num = int(input())

temp = 1
temp_num = 1

if num == 3:
    print("1")
elif num == 2:
    print("1")
elif num == 1:
    print("0")
else:
    while num <= temp_num:
        temp_num = temp_num**temp
