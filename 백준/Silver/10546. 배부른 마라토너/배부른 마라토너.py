
num = int(input())

mara_dict = {}

for i in range(num):
    temp = input()
    if mara_dict.get(temp, 0) != 0:
        mara_dict[temp] += 1
    else:
        mara_dict[temp] = 1


for j in range(num-1):
    temp2 = input()
    
    mara_dict[temp2] -= 1 

for k, v in mara_dict.items():
    if v == 1:
        print(k)