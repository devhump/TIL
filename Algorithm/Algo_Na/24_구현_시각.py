# 24. 구현 - 시각

h = int(input())
m, s = 0, 0

cnt = 0

for k in range(h+1):
    k += 1

    m = 0
    for i in range(60):
        m += 1

        s = 0
        for j in range(60):
            s += 1

            if '3' in str(k)+str(m)+str(s):
                cnt += 1

print(cnt)