T = int(input())

for t in range(T):
    n, word = input().split()

    for char in word:
        for i in range(int(n)):
            print(char, end="")
    print()