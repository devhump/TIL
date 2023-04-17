# BOJ_4949 균형잡힌 세상

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