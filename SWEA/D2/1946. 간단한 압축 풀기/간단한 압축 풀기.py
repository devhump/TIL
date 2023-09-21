T = int(input())

for t in range(T):
    
    ans = ""
    N = int(input())

    for i in range(N):

        char, cnt = input().split()

        for j in range(int(cnt)):
            ans += char

    print(f"#{t+1}")
    while ans:
        if len(ans) > 10:
            print(ans[:10])
            ans = ans.replace(ans[:10], "", 1)
        else:
            print(ans)
            ans = ans.replace(ans[:len(ans)], "", 1)