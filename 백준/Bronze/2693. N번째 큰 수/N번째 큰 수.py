T = int(input())

for t in range(T):
    temp = list(map(int, input().split()))

    temp.sort()

    print(temp[-3])