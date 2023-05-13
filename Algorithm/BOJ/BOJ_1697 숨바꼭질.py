# BOJ_1697 숨바꼭질

# N, K = map(int, input().split())
N, K = 5, 17


cnt = 0
while True:
    if abs(K - (N * 2)) > N:
        N *= 2 
        cnt += 1
    else:
        if((N - 1) * 2) > K:
            N = N - 1 
            cnt += 1
        elif ((N + 1) * 2) > K:
            N = N + 1
            cnt += 1

    if N == K:
        break

print(cnt)