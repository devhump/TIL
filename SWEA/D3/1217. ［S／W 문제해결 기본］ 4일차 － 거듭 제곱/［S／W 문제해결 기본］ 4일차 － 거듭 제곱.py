def pow_multiple(a,b, res):
    if b > 0:
        res *= a
        res = pow_multiple(a, b-1, res)
    return res

T = 10

for t in range(T):
    N = int(input())


    a, b = map(int, input().split())
    res = 1
    print(f'#{N} {pow_multiple(a, b, res)}')