
# ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

from collections import deque 

list_A_to_num = [
    "zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine"]

dict_A_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# print(list_A_to_num)

confused_str = "one4seveneight"

result = []

cnt = 0
cnt_2 = 0
cnt_3 = 0
# for char in confused_str:
    

for char in confused_str:

    for i in range(10):
        if list_A_to_num[i] in confused_str:
            idx = len(list_A_to_num[i])
            # key = list_A_to_num[i]
            result.append(list_A_to_num[i])
            while idx:
                list(confused_str).pop(0)
                idx -= 1
            # cnt += 1   

    if ord(char) >= 48 and ord(char) <= 57: 
        cnt_2 += 1
        print(f"if {cnt_2}회 실행")
        result.append(int(char))
   
print(result)
