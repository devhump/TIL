FBI_check = False
for t in range(5):
    FBI_str = input()

    if "FBI" in FBI_str:
        print(t+1, end=" ")
        FBI_check = True

if not FBI_check:
    print("HE GOT AWAY!")