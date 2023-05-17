T = int(input())

for t in range(T):
    N = int(input())
    temp = list(map(int, input().split()))

    temp.sort()

    print(f'#{t+1}', end=" ")
    for i in range(N):
        print(temp[i], end=" ")
    print()