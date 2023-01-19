
alp_list = input()

alp_dic = {}
for char in alp_list:

    temp = ord(char)
    if temp >= 97:
        temp -= 32

    if chr(temp) in alp_dic:
        alp_dic[chr(temp)] += 1
    else:
        alp_dic[chr(temp)] = 1

alp_dic2li = sorted(alp_dic.items(), key=lambda x: x[1])

if len(alp_dic) == 1:
    print(chr(temp))
elif alp_dic2li[-1][1] == alp_dic2li[-2][1]:
    print("?")
else:
    print(alp_dic2li[-1][0])
