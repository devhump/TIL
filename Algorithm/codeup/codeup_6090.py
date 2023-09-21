a, m, d, n = map(int, input().split())
# a, m, d, n = 1, -2, 1, 8

for i in range(n-1):
    a *= m
    a += d

print(a)