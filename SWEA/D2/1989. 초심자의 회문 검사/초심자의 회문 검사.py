
import math 
T = int(input())

for t in range(T):
    word = input()
    
    check = True
    for i in range(math.floor(len(word)/2)):
        if word[i] == word[-i-1]:
            pass
        else:
            check = False

    if check:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')