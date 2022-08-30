# 문제 08. 두번째로 큰 수 구하기
# > 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# **max() 함수 사용 금지**

# ### Input
# numbers = [0, 20, 100]
# ### Output
# 20

# test case
numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30

max_num_1 = float("-inf")
max_num_2 = float("-inf")

for num in numbers:

    if max_num_1 <= num:
        max_num_1 = num
    else:
        if max_num_2 < num and max_num_1 != num:
            max_num_2 = num
        
print(max_num_1, max_num_2)
