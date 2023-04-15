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
            if len(stack) > 0:
                if stack[-1] == "(":
                    stack.pop(-1)
            else:
                stack.append(")")
        elif char == "]":
            if len(stack) > 0:
                if stack[-1] == "[":
                    stack.pop(-1)
            else:
                stack.append("]")
        
    # print(stack)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")