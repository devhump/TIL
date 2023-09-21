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
    
    s2 = ""
    j = 0
    for i in range(len(s)):

        if j > 0:
            j -= 1
            continue
        if 48 <= ord(s[i]) <= 57:
            s2 += str(s[i])
        else:
            for nums in list_num:
                if nums in s[i:]:
                    n = s[i:i+len(nums)]
                    s2 += str(dict_num[n])
                    j += len(nums) -1
                    break

    answer = s2
    return answer

print(solution("123"))
