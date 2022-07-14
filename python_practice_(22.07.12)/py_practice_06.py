
# > 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# **max() 함수 사용 금지**
#
# ### Input
# numbers = [0, 20, 100]
# ### Output
# 100
#######################################################

# numbers = [0, 20, 100, 50, -60, 50, 100] # 100
#numbers = [0, 1, 0] # 1
numbers = [-10, -100, -30] # -10 

#numbers = [0, 20, 100]
#print(type(numbers))

memory_max = 0
#memory_final = 0

for i in numbers:
    print(f"i값{i}")
    if memory_max <= i:
        memory_max = i
    # print(f"내부값{memory_final}")
    

print(memory_max)

## 음수 케이스 예외 처리 필요