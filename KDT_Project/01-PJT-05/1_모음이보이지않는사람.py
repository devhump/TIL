import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

vowel = "aeiouAEIOU"

for t in range(T):
    
    str_input = (input())

    i = 0
    new_str = ""
    for char in str_input:
        if char not in vowel:
            new_str += char
            # str_input.replace(char,"_") # 이게 왜 안 되지..???
    # print(str_input)
    print(f"#{t+1} {new_str}")