# BOJ_7568 덩치(me)

## 입력 파츠
import sys
sys.stdin = open("BOJ_7568_input.txt", "r")

case_num = int(input())

kgcm_list = []

for i in range(case_num):
    kgcm_list.append(list(map(int, input().split())))

## 키와 몸무게를 각각 리스트로 나눔
kg_ls = []
cm_ls = []
for i in range(case_num):
    kg_ls.append(kgcm_list[i][0])
    cm_ls.append(kgcm_list[i][1])

kg_ls.sort(reverse=True) # 키와 몸무게 리스트를 각각 정렬
cm_ls.sort(reverse=True)

# print(kg_ls, cm_ls)


checklist = [False] * case_num
checklist2 = []
for i in range(case_num): # 정렬된 내용을 기준으로 각각 순위를 매김
    kgcm_list[i][0] = kg_ls.index(kgcm_list[i][0]) + 1
    kgcm_list[i][1] = cm_ls.index(kgcm_list[i][1]) + 1

    if kgcm_list[i][0] == kgcm_list[i][1]: # 키-몸무게 등수가 같다면
        checklist[i] = True # 체크리스트에 True로 표시
    else:
        # 체크리스트2에는 키-몸무게 등수가 같지 않은 순번 기록
        checklist2.append(kgcm_list[i][0]) 
        checklist2.append(kgcm_list[i][1])

# print(kgcm_list)

checklist2 = list(set(checklist2)) # 중복되는 숫자 처리
checklist2.sort()


for i in range(case_num):

    if (kgcm_list[i][0] in range(checklist2[0], checklist2[-1]+1)) or (kgcm_list[i][1] in range(checklist2[0], checklist2[-1]+1)):
        checklist[i] = False

    if (checklist[i] == True):
        print(kgcm_list[i][0], end=" ")
    else:
        print(checklist2[0], end=" ") 
