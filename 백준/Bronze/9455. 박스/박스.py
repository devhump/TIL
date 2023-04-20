for _ in range(int(input())):
    m, n = map(int, input().split())
    b = []
    # * 하나의 리스트로 받아서 
    for i in range(m):
        l = list(map(int, input().split()))
        b.insert(0, l)
    arr = []
    # * 여기서 회전된 배열을 만든다. 
    for j in range(n):
        tmp = []
        for k in range(m):
            tmp.append(b[k][j])
        arr.append(tmp)
    cnt = 0
    for a in arr:
        t = 0
        for idx, num in enumerate(a):
            if num == 1:
                cnt += idx - t
                t += 1
    print(cnt)