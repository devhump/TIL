from collections import deque

T = 10 

for t in range(10):
    N = int(input())
    encode = list(map(int, input().split()))
    queue = deque(encode)

    # print(queue)

    num = 1
    while True: 
        temp = queue.popleft()
        temp -= num
        if temp <= 0:
            queue.append(0)
            break
        queue.append(temp)
        num += 1

        if num > 5:
            num = 1

    print(f"#{t+1}", end=" ")
    print(*queue)