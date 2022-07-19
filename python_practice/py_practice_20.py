num = 347
cnt = 0

#자릿수를 알기위한 코드
while (num > (10**cnt)):
    cnt += 1
num_len = cnt 

total_sum = 0

while(num_len >= 0):
    cnt_2 = 0 # while문 1번 실행 될 때 초기화

    #각 자리수의 10의 제곱을 제함.
    while (num > (10**num_len) or num == 1):  
        # 이때 num가 1일 경우 그냥 종료가 되서, 조건 추가
        num -= (10**num_len)
        cnt_2 += 1 
    
    total_sum += cnt_2 #각 자리수의 합
    num_len -= 1
    
print(total_sum)    







