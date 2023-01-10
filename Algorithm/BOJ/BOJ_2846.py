# BOJ_2846

climb_len = int(input())
climb_list = list(map(int, input().split()))


temp_low, temp_high, temp_height = 0, 0, 0
continue_bool = False  # 상승중인지(오르막인지) 여부를 Bool 변수로 체크
max_height = 0
for i in range(climb_len):

    # 이전 수와의 비교이기에 index가 0 일때 pass
    if i == 0:
        continue

    # 연속 상승중 일 결우
    if (continue_bool == True) and (climb_list[i - 1] < climb_list[i]):
        temp_high = climb_list[i]
        temp_height = temp_high - temp_low
        continue_bool = True

        if max_height <= temp_height:
            max_height = temp_height

        continue

    # 아닐경우 (최초 상승중일 경우)
    if (continue_bool == False) and climb_list[i - 1] < climb_list[i]:
        temp_low = climb_list[i - 1]
        temp_high = climb_list[i]
        temp_height = temp_high - temp_low
        continue_bool = True
    else:
        continue_bool = False

    # 변화폭이 최대치이면 갱신
    if max_height <= temp_height:
        max_height = temp_height

print(max_height)
