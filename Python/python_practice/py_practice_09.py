# 문제 09. 득표수 구하기 
# 주어진 리스트가 반장 선거 투표 결과일 때 
# 이영희의 총 득표수를 출력하시오.

students = ['이영희', '김철수', '이영희', 
'조민지', '김철수', '조민지', '이영희', '이영희']


# students = map(str, input().split())

def who_is_Cap(students):

    cnt = 0         
    # local 변수 설정
    # indent 확실히!

    for name in students:

        if (name == '이영희'):  
            cnt += 1
    
    return cnt

print(who_is_Cap(students))

