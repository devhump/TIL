# BOJ_7568 덩치 


import sys
sys.stdin = open("BOJ_7568_input.txt", "r")

case_num = int(input())

kgcm_list = []

for i in range(case_num):
    kgcm_list.append(list(map(int, input().split())))


kg_ls = []
cm_ls = []
for i in range(case_num):
    kg_ls.append(kgcm_list[i][0])
    cm_ls.append(kgcm_list[i][1])

kg_ls.sort()
cm_ls.sort()

# print(kg_ls, cm_ls)


checklist = [False] * case_num
checklist2 = []
for i in range(case_num):
    kgcm_list[i][0] = kg_ls.index(kgcm_list[i][0]) + 1
    kgcm_list[i][1] = cm_ls.index(kgcm_list[i][1]) + 1

    if kgcm_list[i][0] == kgcm_list[i][1]                                             :
        checklist[i] = True
    else:
        checklist2.append(kgcm_list[i][0])
        checklist2.append(kgcm_list[i][1])

checklist2.sort()

for i in range(case_num):

    if (kgcm_list[i][0] in range(checklist2[0], checklist2[-1]+1)) or (kgcm_list[i][1] in range(checklist2[0], checklist2[-1]+1)):
        if kgcm_list[i][0] < kgcm_list[i][1]:
            print(kgcm_list[i][0], end=" ")
        else:
            print(kgcm_list[i][1], end=" ")
    else:
        print(kgcm_list[i][1], end=" ")

# print(kgcm_list)
# print(checklist)
# print(checklist2)
