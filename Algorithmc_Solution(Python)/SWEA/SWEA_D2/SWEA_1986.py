import sys
sys.stdin = open("SWEA_1986_input.txt", "r")

T = int(input())
sum_result = 0 
cnt = 0

for i in range(1,T+1):
    cnt += 1

    if i == 1:
        sum_result = 1
    elif i % 2 == 0:
        sum_result -= i
    elif i % 2 != 0:
        sum_result += i
    
    print(f"#{cnt} {sum_result}")


# 출력값 예시
#     #9 5
#     #10 -5