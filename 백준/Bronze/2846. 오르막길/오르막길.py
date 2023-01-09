climb_len = int(input())
climb_list = list(map(int, input().split()))


temp_low, temp_high, temp_heigth = 0, 0, 0
continue_bool = False
max_height = 0
for i in range(climb_len):

    if i == 0:
        continue

    if (continue_bool == True) and (climb_list[i - 1] < climb_list[i]):
        temp_high = climb_list[i]
        temp_heigth = temp_high - temp_low
        continue_bool = True

        if max_height <= temp_heigth:
            max_height = temp_heigth

        continue

    if (continue_bool == False) and climb_list[i - 1] < climb_list[i]:
        temp_low = climb_list[i - 1]
        temp_high = climb_list[i]
        temp_heigth = temp_high - temp_low
        continue_bool = True
    else:
        continue_bool = False

    if max_height <= temp_heigth:
        max_height = temp_heigth

print(max_height)
