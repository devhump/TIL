# 문제 05.
# > 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# **sum(), len()  함수 사용 금지**
 
# ### Input
# numbers = [3, 10, 20]
# ### Output
# 11

numbers = [3, 10, 20]

sum_for_average = 0
average_result = 0

for i in numbers:
    sum_for_average += i

average_result = sum_for_average/3

print(average_result)