from collections import deque

T = 10

for t in range(T):
    N = int(input())
    encode = list(map(int, input().split()))
    cmd_N = int(input())
    cmd_str = list(input().split())
    queue = deque(cmd_str)

    for i in range(cmd_N):
        
        a = queue.popleft()

        if a == "I":
            idx = queue.popleft()
            cnt = queue.popleft()

            for k in range(int(cnt)):
                temp = queue.popleft()
                encode.insert(int(idx)+k, int(temp))

    print(f'#{t+1}', end=" ")
    print(*encode[:10])