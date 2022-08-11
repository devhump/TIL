# BOJ_17388. 와글와글 숭고한

S, K, H = map(int, input().split())

if (S + K + H) >= 100:
    print("OK")
else:
    lowest_Univ = min(S, K, H)

    if lowest_Univ == S:
        print("Soongsil")
    elif lowest_Univ == K:
        print("Korea")
    elif lowest_Univ == H:
        print("Hanyang")

