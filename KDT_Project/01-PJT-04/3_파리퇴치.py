import sys
from pprint import pprint

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for t in range(T):
    M, N = map(int, input().split())

    fly_array = []
    for i in range(M):
        fly_array.append(list(map(int, input().split())))

    # pprint(fly_array)

    result = 0
    max_sum = []
    for k in range(M-N):
        for idx in range(N):
            for j in range(N):
                print(f"i,j: {idx},{j}")
                result += fly_array[i][j]
        max_sum.append(result)

    print(max(max_sum))

