
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