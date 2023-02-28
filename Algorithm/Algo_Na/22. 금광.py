# 22. 금광 / DP
import sys

sys.stdin = open("22_Q4_input.txt", "r")

T = int(input())  # T 테스트 케이스

for j in range(T):
    N, M = map(int, input().split())  # N x M 행렬
    temp_li = list(map(int, input().split()))

    dp = [0] * 4
    for i in range(M):
        dp[i] = max(temp_li[i], temp_li[i + (M)], temp_li[i + (2 * M)])

    print(dp)
    print(sum(dp))
