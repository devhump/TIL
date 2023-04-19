n = int(input())

for i in range(n):
    str_A = list(map(str, input().split()))

    for j in range(len(str_A)):
        print(str_A[j][::-1], end=" ")
    print()
    