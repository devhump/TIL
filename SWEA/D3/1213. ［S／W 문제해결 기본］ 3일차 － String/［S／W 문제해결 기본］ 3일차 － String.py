T = 10

for _ in range(T):
    N = int(input())
    word = input()
    find_str = input()

    cnt = 0
    while True:

        if find_str.find(word) == -1:
            break
        else:
            find_str = find_str.replace(word, "", 1)
            cnt += 1

    print(f'#{N} {cnt}')