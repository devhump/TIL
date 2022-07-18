#######################################
# while 문 활용
#######################################

# # 변수 입력
# n = int(input())

# cnt = 1
# cnt_sum = 0

# while (cnt <= n):
#     cnt_sum += cnt #합을 누적
#     cnt += 1 # 1부터 숫자+1

# print(cnt_sum)


#######################################
# for 문 활용
#######################################

# 변수 입력
n = int(input())

cnt_sum = 0

for i in range(n+1):
    cnt_sum += i
 
print(cnt_sum)
