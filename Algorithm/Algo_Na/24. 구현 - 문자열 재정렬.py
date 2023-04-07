# 24. 구현 - 문자열 재정렬

# data = input()
# data = "AJKDLSI412K4JSJ9D"
data = "K1KA5CB7"

data_li = []
for i in range(len(data)):
    data_li.append(data[i])

num_sum = 0 
for d in data_li:
    if ord(d) in range(48,59):
        num_sum += int(d)
        data_li.remove(d)


for d in data_li:
    if ord(d) in range(48,59):
        num_sum += int(d)
        data_li.remove(d)

data_li.sort()

print(''.join(data_li)+str(num_sum))
