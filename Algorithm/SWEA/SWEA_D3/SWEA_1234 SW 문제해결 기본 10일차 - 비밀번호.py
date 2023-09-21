# SWEA_1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# @ 답이 나온 것 같은데, 왜 자꾸 오류가 나서 살펴보니 
# @ 8번 테케에서 1123123123 이 나왔다. 
# @ 왜 저게 안 먹힐까 고민하다가 그냥 같은 반복문 한번 더  돌려서 해결
# ! 근데 구글링해보니 스택으로 푸는 문제 라고... 


import sys
sys.stdin = open('SWEA_1234_input.txt', 'r')

T = 10

for t in range(T):
    len_num, num_code = input().split()

    len_num = int(len_num)

    i = 0
    while True:
        if num_code[i] == num_code[i+1]:
            num_code = num_code[:i] + num_code[i+2:]
            i = 0
        i += 1

        if i == (len(num_code)-1):
            break

    i = 0
    while True:
        if num_code[i] == num_code[i+1]:
            num_code = num_code[:i] + num_code[i+2:]
            i = 0
        i += 1

        if i == (len(num_code)-1):
            break

    print(f'#{t+1} {int(num_code)}')


# for tc in range(1,11):
#     N = list(map(str,input().split()))
#     password = list(N[1]) # 비밀번호를 list 형태로 받아주기
#     real_password = []

#     for p in password:    # 비밀번호를 순차적으로 하나씩 꺼내기
#         if real_password and p == real_password[-1]: # 새 리스트가 비어있지 않고, 마지막 값이 p와 같다면
#             real_password.pop()                      # 가장 최근에 들어온 값과 짝이 맞으므로 pop
#         else :
#             real_password.append(p)                  # 새 리스트가 비어있거나, 마지막 값이 p와 같지 않다면 추가

#     print(f'#{tc}',''.join(real_password))
