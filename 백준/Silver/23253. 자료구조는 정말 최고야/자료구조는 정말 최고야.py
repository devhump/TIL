N, M = map(int, input().split())
check = True
for _ in range(M):
    cnt = int(input())
    books = list(map(int, input().split()))

    if check:
        while len(books) > 0:
            temp = books.pop()
            if books:
                if temp > books[-1]:
                    check = False
                    break
    else:
        break
        
if check:
    print('Yes')
else:
    print('No')