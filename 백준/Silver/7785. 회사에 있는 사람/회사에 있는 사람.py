num = int(input())

inwork = {}
for i in range(num):
    temp = []
    temp = list(map(str, input().split()))
    inwork[temp[0]] = temp[1]

result = []
for item in inwork.items():
    if item[1] == "enter":
        result.append(item[0])

result.sort(reverse=True)
for i in range(len(result)):
    print(result[i])
