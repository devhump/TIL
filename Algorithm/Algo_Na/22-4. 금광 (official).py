# 22-4. 금광 (official)

from pprint import pprint

# test case 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # DP를 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
        # 0, 1, 2, 3, 4, 5, 6, ... 11 (index 상)
        # 위 코드를 통해 1차원 리스트 -> 2차원 리스트로 변환

    # dp 진행 (bottom-up)
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0  # 인덱스 벗어나면 0으로 처리
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0  # 인덱스 벗어나면 0으로 처리
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
        # 마지막 열의 수를 행마다 반복하면서 최대값으로 갱신
    print(result)

    pprint(dp)
