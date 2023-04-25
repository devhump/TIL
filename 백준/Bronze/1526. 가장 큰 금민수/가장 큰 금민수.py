N = int(input())
# N = 474747 

cnt = 0
while True:

    if cnt == len(str(N)):
        break

    cnt = 0
    for char in str(N):
        if char == "4" or char == "7":
            pass 
            cnt += 1
        else:
            N -= 1
            continue

print(N)