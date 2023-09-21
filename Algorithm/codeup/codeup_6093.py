cnt = int(input())
# cnt = 10

call = list(map(int, input().split()))

for i in range(1, cnt+1):
    print(call[-i], end=' ')
