# BOJ_2693 N번째 큰 수 

T = int(input())

for t in range(T):
    temp = list(map(int, input().split()))

    temp.sort()

    print(temp[-3])
