
T = 10

for t in range(T):
    N = int(input())

    brackets = list(input())

    temp = []
    for i in range(N):
        temp.append(brackets[i])

        if N % 2 != 0:
            flag = False
            break

        if len(temp) >= 2:
            if temp[-2] == "(" and temp[-1] == ")":
                temp.pop()
                temp.pop()
            elif temp[-2] == "<" and temp[-1] == ">":
                temp.pop()
                temp.pop()
            elif temp[-2] == "[" and temp[-1] == "]":
                temp.pop()
                temp.pop()
            elif temp[-2] == "{" and temp[-1] == "}":
                temp.pop()
                temp.pop()

    # print(brackets)
    if len(temp) == 0:
        flag = True
    else:
        flag = False

    if flag:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
