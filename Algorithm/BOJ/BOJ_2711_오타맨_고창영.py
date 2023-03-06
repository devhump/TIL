# BOJ_2711 오타맨 고창영

tc = int(input())

for t in range(tc):
    pos, word = input().split()
    pos = int(pos)

    temp = [word[: pos - 1], word[pos:]]
    print("".join(temp))
