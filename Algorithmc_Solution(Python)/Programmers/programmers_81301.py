
# ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

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
for char in confused_str:
    
    print(char)

    if ord(char) >= 48 and ord(char) <= 57: 
        result.append(char)
    else:
        while(cnt == 0):
            for i in range(10):
                if list_A_to_num[i] in confused_str:
                    key = list_A_to_num[i]
                    result.append(dict_A_to_num[key])
            cnt += 1
        i = 0

print(result)
