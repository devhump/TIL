T = 10

for t in range(T):

    N = int(input())
    boxes = list(map(int, input().split()))

    boxes.sort()

    for i in range(N):
        boxes[-1] -= 1
        boxes[0] += 1

        boxes.sort()

    print(f'#{t+1} {boxes[-1]-boxes[0]}')