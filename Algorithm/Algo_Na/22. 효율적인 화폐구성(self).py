# 22. 효율적인 화폐구성 ver.self

N, K = map(int, input().split())

cash_li = []
for i in range(N):
    cash_li.append(int(input()))

cash_li.sort()

cnt = 0
while K > 0:

    if K < cash_li[0]:
        break

    if K >= cash_li[-1]:
        K -= cash_li[-1]
        cnt += 1
    else:
        cash_li.pop()

if K < 0 or K < cash_li[0]:
    print(-1)
else:
    print(cnt)
