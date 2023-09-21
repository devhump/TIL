# BOJ_23253 자료구조는 정말 최고야. 구글링

# * 보고는 벙 쪘다. 
# * 나는 계속 전부 다 받아서 해결하려고 생각했는데, 
# * 각자 스택에서만 오름차순으로 뺄 수 있는지 확인하면 되는 거였다;;

import sys
sys.stdin = open("BOJ_23253_input.txt", "r")
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
