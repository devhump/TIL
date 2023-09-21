# # 문제 21. 숫자 뒤집기
# > 주어진 숫자를 뒤집은 결과를 출력하시오.
# - 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# ### Input
# 1234
# ### Output
# 4321

# 20번 풀이 활용

num = 3947
cnt = 0

#자릿수를 알기위한 코드
while (num > (10**cnt)):
    cnt += 1
num_len = cnt 

num_list = [] #각 자릿수 값을 저장할 빈 리스트

while(num_len >= 0):
    cnt_2 = 0 # while문 1번 실행 될 때 초기화

    #각 자리수의 10의 제곱을 제함.
    while (num > (10**num_len) or num == 1):  
        # 이때 num가 1일 경우 그냥 종료가 되서, 조건 추가
        num -= (10**num_len)
        cnt_2 += 1 
    
    num_list.append(cnt_2) #각 자릿수 값을 리스트에 저장
    num_len -= 1

num_len2 = cnt #자릿수값 재입력

for i in range(1,num_len2+1):
    print(num_list[-i],end='')    







