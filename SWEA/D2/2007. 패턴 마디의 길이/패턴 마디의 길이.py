
T = int(input())

for t in range(T):
    word_str = input()

    for i in range(1, 11):
        if word_str[0:i+1] == word_str[i+1:(2*i)+2]:
            res = len(word_str[0:i+1])
            # print(word_str[0:i+1])
            break

    print(f'#{t+1} {res}')
