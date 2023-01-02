
# import sys
# sys.stdin = open("BOJ_9012_input.txt")

# T = int(input())


# for i in range(T):
#     PS_list = list(input())

#     # print(PS_list)
#     cnt = 0
#     for j in PS_list:

#         if j == "(":             #단순 개수를 비교하는 코드
#             cnt += 1
#         elif j == ")":
#             cnt -= 1

#     if cnt == 0:
#         print("YES")
#     else:
#         print("NO")


import sys
sys.stdin = open("BOJ_9012_input.txt")

T = int(input())


for i in range(T):
    PS_list = list(input())

    stack_list = [] #비어 있는 스택 리스트 선언

    # print(PS_list)
    # cnt = 0
    for j in range(len(PS_list)):

        # if len(PS_list) % 2 != 0: # 괄호의 개수가 짝수 인지 확인 -> 오답처리
        #     stack_list.append(1)
        #     break

        if PS_list.count("(") != PS_list.count(")"): #테케에서 (((( 같은 케이스가 나옴
            stack_list.append(1) # 두 괄호 쌍의 개수가 같지 않으면 out
            break

        if PS_list[0] == ")":
            stack_list.append(1) #시작이 ) 라면 바로 out
            break

        if PS_list[j] == "(":             
            stack_list.append("(")
        
        
        if len(stack_list) > 0: #스택에 내용이 없다 -> 오류코드 (not VPS) 
            if PS_list[j] == ")": 
                stack_list.pop()

    if len(stack_list) == 0: #stack이 비어있다 == 잘 처리 되었다
        print("YES") # VPS일 경우
    else:
        print("NO") # 아닐 경우
