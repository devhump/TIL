N = int(input())
user_dict = {}
cnt = 0
for i in range(N):
    temp = input()
    if temp == "ENTER":
        user_dict = {}
        continue

    if user_dict.get(temp, 0):
        user_dict[temp] += 1
    else:
        user_dict[temp] = 1
        cnt += 1

print(cnt)