# 암호문 문제는 워낙 어려워서 다른 분들도 많이 힘들어한 문제입니다. 
# split(' I ')로 명령문을 나눈 것 만으로도
# 정말 잘 접근했다고 말씀드리고 싶습니다.

# 수업시간에 리뷰를 조금 하셨지만 
# 꼭 직접 다시 코드를 구현해보는 것도 좋은 방법입니다. 

# 두 가지 단계로 나누어서 문제를 풀어볼 수 있는데, 
# 가장 먼저 여러개의 명령어가 한꺼번에 입력될 때 
# 원하는 I, x, y, s 의 형태로 잘 나누어야 합니다. 
# 문자열의 split()과 배열의 인덱싱을 적절히 활용하시는 문제입니다.

# 다음으로는 해당 명령어를 잘 수행하는 가에 대한 문제입니다. 
# x번째 위치에 적절히 s를 넣을 수 있는 지에 대한 부분입니다. 
# 리스트의 insert 메소드를 적절히 활용하시는 문제입니다. 
# 접근법을 설명드렸지만 여전히 어려운 문제입니다. 

# 구현에 어려움을 느끼시면 좌절하지 마시고 
# 8월 1일(월) 수업의 코드리뷰를 확인하시면 좋을 것 같습니다.


import sys
sys.stdin = open("exam_07_input.txt")

T = 10
case_num = 0

for i in range(T):
    case_num += 1

    A = int(input())
    list_A = input().split()
    B = int(input())
    list_B = input().split("I ")

    new_list_B = []

    # 최초의 " "(공백 없애주기)
    for i in range(1, len(list_B)):
        new_list_B.append(list_B[i])
    
    # 인덱스 접근을 위해 공백 기준으로 잘라주기 
    for i in range(len(new_list_B)):
        new_list_B[i] = new_list_B[i].split()

    # 추후 조작을 위해 리스트 모든 요소를 int형 변환
    for i in range(len(new_list_B)):
        for j in range(len(new_list_B[i])):
            new_list_B[i][j] = int(new_list_B[i][j])
        
    # print(new_list_B[1][0], type(new_list_B[1][0]))


    for i in range(B):
        temp = new_list_B[i][0] #insert 인덱스값
        # print(f"temp: {temp}")
        cnt = 0
        for j in range(len(new_list_B[i])-2):
            list_A.insert(temp+cnt, new_list_B[i][2+cnt]) # list
            cnt += 1 # 최초 idx 인덱스 값 n 이후, n+1, n+2... 가 되어야 함         
    # print(list_A)

    #출력파트
    print(f"#{case_num} ", end='')
    for i in range(10):
        print(list_A[i], end=' ')
    print("")