# BOJ_20001 고무오리 디버깅
# ! 틀린 코드 
# ? 맞는거 같은데 왜 틀렸다고 하지...

import sys
sys.stdin = open("BOJ_20001_input.txt", "r")

# import sys 
# input = sys.stdin.readline

start = input()

stack = []

while True:
    
    temp = input()
    if "고무오리 디버깅 끝" == temp:
        break

    if temp == "문제":
        stack.append("문제")
    elif temp == "고무오리":
        if stack:
            if stack[-1] == "문제":
                stack.pop(-1)
        else:
            stack.append("문제")
            stack.append("문제")

if len(stack) > 1:
    print("힝구")
else:
    print("고무오리야 사랑해")