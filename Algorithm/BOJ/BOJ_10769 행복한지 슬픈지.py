# BOJ_10769 행복한지 슬픈지

import sys
sys.stdin = open('BOJ_10769_input.txt', 'r')

msg = input()

# ! replace를 활용하려면 반환값을 저장해야한다! 
msg = msg.replace(":-)", "+")
msg = msg.replace(":-(", "-")


# print(msg)
a = msg.count("+")
b = msg.count("-")

if a > b:
    print("happy")
elif a < b:
    print("sad")
elif a == 0 and b == 0:
    print("none")
elif a == b:
    print("unsure")
