first = input().split("-")

for i in range(len(first)):

    if "+" in first[i]:
        second = map(int, first[i].split("+"))
        first[i] = sum(second)
    else:
        first[i] = int(first[i])

    if i == 0:
        result = first[i]
    else:
        result -= first[i]

print(result)