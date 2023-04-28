msg = input()

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
