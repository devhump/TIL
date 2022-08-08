# BOJ_2390. 일곱 난쟁이

import sys
sys.stdin = open("BOJ_2309_input.txt")

# dwarf_9 = [20, 7, 23, 19, 10, 15, 25, 8, 13]

n = 9

dwarf_9 = []
for i in range(n):
    dwarf_9.append(int(input())) 

total_sum = sum(dwarf_9)

spy = []
for i in range(n-1):
    for j in range(i+1, n):
        result = total_sum - (dwarf_9[i] + dwarf_9[j])

        if result == 100:
            spy.append(dwarf_9[i])
            spy.append(dwarf_9[j])
            
# print(spy)

dwarf_9.remove(spy[0])
dwarf_9.remove(spy[1])

# 진짜를 찾았다!
dwarf_7 = sorted(dwarf_9)

while (dwarf_7):
    print(dwarf_7.pop(0))
