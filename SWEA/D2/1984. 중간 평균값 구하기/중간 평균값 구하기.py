T = int(input())

for t in range(T):
    temp = list(map(int, input().split()))

    temp.sort()
    temp = temp[1:9]
    
    print(f'#{t+1} {round(sum(temp)/8)}')