import sys
sys.stdin = open("SWEA_1989_input.txt", "r")

T = int(input())

for i in range(T):

    a = input()
    b = a[::-1]

    if a == b:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")