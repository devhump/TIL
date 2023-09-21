# BOJ_4949 균형잡힌 세상

import sys
sys.stdin = open("BOJ_4949_input.txt", "r")

# import sys 
# input = sys.stdin.readline

while True:
    stack = []
    temp_str = input()

    if temp_str == '.':
        break

    for char in temp_str:
        if char == "(":
            stack.append("(")
        elif char == "[":
            stack.append("[")
        elif char == ")":
            # ! 이 부분에서 계속 에러가 났다.
            # if len(stack) > 0:
            #     if stack[-1] == "(":
            #         stack.pop()
            # * 2중 if문일 때는 계속 틀리다가, 
            # * 두 개의 조건을 한번에 체크하게 하니까 바로 성공
            if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
            else:
                stack.append(")")
        elif char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
            else:
                stack.append("]")
        
    # print(stack)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")