# BOJ_4673_셀프_넘버

nums = [i for i in range(10000)]

for j in range(10000):
    temp = j

    for k in range(len(str(j))):
        temp += int((str(j))[k])

    if temp in nums:
        nums.remove(temp)

for num in nums:
    print(num)
