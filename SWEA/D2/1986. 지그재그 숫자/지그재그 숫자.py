T = int(input())

for t in range(T):
    num = int(input())

    temp = 0
    for i in range(1, num+1):

        if i % 2 == 0:
            temp -= i
        else:
            temp += i

    print(f'#{t+1} {temp}')