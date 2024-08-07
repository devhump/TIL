# HPHK 문제 07. 최솟값 구하기

# > 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# **min() 함수 사용 금지**

# ### Input
numbers = [0, 20, 100]
# ### Output
# 0

# test case
numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100

min_num = numbers[0]


for num in numbers:
    if num < min_num:
        min_num = num

print(min_num)