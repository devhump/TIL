# BOJ_1526 가장 큰 금민수

from itertools import permutations

# N = int(input())
N = 100

N_len = len(str(N))

result = []
for i in range(N_len, -1, -1):
    cnt1 = 0
    cnt2 = 0
    temp = []   
    temp2 = []

    print(f"i, N_len {i} {N_len}")

    while cnt1 < i:
        temp.append(4)
        temp2.append(7)
        cnt1 += 1

    while cnt2 < N_len - i:
        temp.append(7)
        temp2.append(4)
        cnt2 += 1

    result = list(set(permutations(temp, i))) # 모든 순열 구하기
    result2  = list(set(permutations(temp2, i)))
    result3 = result + result2
    print(result3)