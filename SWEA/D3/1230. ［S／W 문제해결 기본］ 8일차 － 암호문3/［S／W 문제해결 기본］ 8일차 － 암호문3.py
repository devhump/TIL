from collections import deque


T = 10

for t in range(T):
    N = int(input())
    encode = list(map(int, input().split()))
    cmd_N = int(input())
    cmd_str = list(input().split())
    queue = deque(cmd_str)

    for i in range(cmd_N):
        
        cmd = queue.popleft()

        if cmd == "I":
            idx = queue.popleft()
            cnt = queue.popleft()

            for k in range(int(cnt)):
                temp = queue.popleft()
                encode.insert(int(idx)+k, int(temp))

        if cmd == "D":
            idx = queue.popleft()
            cnt = queue.popleft()

            for k in range(int(cnt)):
                del encode[int(idx)]


        if cmd == "A":
            cnt = queue.popleft()

            for k in range(int(cnt)):
                temp = queue.popleft()
                encode.append(int(temp))

    print(f'#{t+1}', end=" ")
    print(*encode[:10])