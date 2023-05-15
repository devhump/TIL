T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    
    if N < M:
        max_sum = 0
        for i in range(M-N+1):
            temp_sum = 0
            for j in range(N):
                temp_sum += N_list[j] * M_list[i+j]
            # print(temp_sum)
            if temp_sum > max_sum:
                max_sum = temp_sum
    elif N > M:
        max_sum = 0
        for i in range(N-M+1):
            temp_sum = 0
            for j in range(M):
                temp_sum += N_list[j+i] * M_list[j]

            if temp_sum > max_sum:
                max_sum = temp_sum
    elif N == M:
            max_sum = 0
            for j in range(N):
                max_sum += N_list[j] * M_list[j]

    print(f'#{t+1} {max_sum}')