# BOJ_11170 0의 개수

for _ in range(int(input())):
    N, M = map(int, input().split())

    res = 0
    for i in range(N, M+1):
        temp = list(str(i))
        res += temp.count("0")
    
    print(res)

