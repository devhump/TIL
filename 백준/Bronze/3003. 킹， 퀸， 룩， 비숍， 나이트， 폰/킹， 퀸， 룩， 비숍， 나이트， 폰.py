chess = (1, 1, 2, 2, 2, 8)

dh_li = list(map(int, input().split()))

for i in range(6):
    print((chess[i]-dh_li[i]), end=" ")