# SWEA_2068 최대수 구하기

T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    
    res = 0
    for num in nums:
        if num % 2 != 0:
            res += num

    print(f'#{t+1} {res}')
