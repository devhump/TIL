# programmers_81301 숫자 문자열과 영단어
# ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# ! tc는 다 맞지만, 시간초과 및 런타임 에러 나오는 코드

list_num = [
    "zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine"]

dict_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def solution(s):
    
    list_s = list(s)
    s2 = ""
    j = 0
    while list_s:
        if 48 <= ord(list_s[0]) <= 57:
            s2 += str(list_s[0])
            list_s.pop(0)
            j += 1
        else:
            for nums in list_num:
                if  nums in s[j:]:
                    n = s[j:j+len(nums)]
                    s2 += str(dict_num[n])
                    del list_s[:len(nums)]
                    j += len(nums)
                    break

    answer = s2
    return answer

print(solution("2three45sixseven"))
