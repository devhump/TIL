- 📌no_name

```python
# a, b = map(int, input().split())

a, b = 3, 7

soo10_list = []
result = 0
for i in range(100):
    for j in range(i):
        soo10_list.append(i) 
        # 여기가 포인트인 것 같다.
        # j 반복문 내라서 j에만 국한 되지 말고, 
        # i,j 혹은 그 외의 변수도 사용 가능!


for x in range(a-1, b):
    result = soo10_list[x] + result

print(result)
```



```python
# 덩치

T = int(input())
people = []

for i in range(T):
    weight, height = map(int, input().split())
    people.append((weight, height))
#print(people)

rank = [0] * T
for i in people:
    for j in people:
        if i[0] > j[0] and i[1] > j[1]:
            rank[people.index(j)] += 1

for i in rank:
    print(i+1, end=" ")
```



```python
num_list = []

for i in range(4):
    num_list += [i] * i
print(num_list)

sta_num, end_num = map(int, input().split())
# sta, end = 999, 1000
sum_num = 0

for i in range(sta_num - 1, end_num):
    sum_num += num_list[i]
print(sum_num)
```

---

### 22/08/01

```python
from collections import deque

T = int(input())

for _ in range(T):

    word = input()

    
    chek_list1 = deque(word)
    list_gyal = []
    # print(chek_list1)
    for i in list(chek_list1):
        if i == "(":
            list_gyal.append(i)
        elif i == ")":
            list_gyal.append(i)
            
        if list_gyal.count("(") < list_gyal.count(")"):
            print("NO")
            break

    if list_gyal.count("(") == list_gyal.count(")"):
        print("YES")
    elif list_gyal.count("(") > list_gyal.count(")"):
        print("NO")
```

```python

from collections import deque

N = int(input())

card_list = []
card_list = deque(card_list)    # deque로 형 변환
for i in range(1, N+1):
    card_list.append(i)
# print(card_list.popleft())
return_list = []
# return_list = card_list[0]

return_list.append(card_list.popleft())
for j in list(card_list)[1:]:
    card_list.append(card_list.popleft())
    return_list.append(card_list.popleft())
    

print(*return_list, *list(card_list), end=" ")
```

- 📌언패킹(unpacking)

```python
a = [1, 2, 3, 4]

print(a)
print(*a) # 내부에 있는 요소들을 언패킹 해서 보여줌 
>>>
# [1, 2, 3, 4]
# 1 2 3 4
```



### 22/08/03

```python
from pprint import pprint

import sys

sys.stdin = open('2167.txt')

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
#pprint(matrix)

k = int(input())
point = [list(map(int, input().split())) for i in range(k)]
#pprint(point)

for k in range(k):
    sum = 0
    for i in range((point[k][0] - 1), (point[k][2])):
        for j in range((point[k][1] - 1), (point[k][3])):
            sum += matrix[i][j]
    print(sum)
```



- 01-PJT-03

```python
# 모의고사1 (7/29) - 암호문1
# 강사님 풀이


"""
11
449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205 
7
I 1 5 400905 139831 966064 336948 119288 
I 8 6 436704 702451 762737 557561 810021 771706 
I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 
I 13 4 237017 301569 243869 252994 
I 3 4 408347 618608 822798 370982 
I 8 2 424216 356268 
I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976 
"""

# ctrl + d
# 원본암호문 = [449047,855428,425117,532416,358612,929816,313459,311433,472478,589139,568205]

import sys
sys.stdin = open("exam_07_input.txt")

T = 10

for t in range(1, T+1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()
    # print(command_list)
    # ['I', '1', '5', '400905', ...,  
    # 'I', '8', '6', '436704', ..., 
    # 'I', '3', '8'..., ]

    # i의 초기화
    i = 0
    
    # while문 (반복문)
    while i < len(command_list):
        command = command_list[i]

        # print(f"command_list[{i}] {command_list[i]}")
        # command_list[0] I
        # command_list[1] 1
        # command_list[2] 5
        # command_list[3] 400905

        # print(command)
        if command == "I": # 이렇게 접근도 가능하구나, wow...
            # x,y,숫자리스트 s 구해야한다.
            x = int(command_list[i+1])
            y = int(command_list[i+2])
            # print(type(y))
            number_list = command_list[i+3 : i+3+y]

            # insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            # 역순으로 삽입한다.
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))

        # 0 + 1 -> 1
        i = i + 1
    

    # print(origin_list[:10])
    print(f"#{t}",*origin_list[:10]) #언팩킹 완전 힙함!
```



- 📌no_name

  ```python
  import sys
  sys.stdin = open("test_input.txt")
  
  #test_input.txt
  """
  1 2 3 4 5
  """
  
  student = [*map(int, input().split())]
  print(student, student[0], type(student), type(student[0]))
  # [1, 2, 3, 4, 5] 1 <class 'list'> <class 'int'>
  
  student = list(map(int, input().split()))
  print(student, student[0], type(student), type(student[0]))
  # [1, 2, 3, 4, 5] 1 <class 'list'> <class 'int'>
  
  ## 두 구문은 기능적으로 동일
  ```

- 분해합

  ```python
  a,b = (input().split())
  a = int(a)
  b = int(b)
  
  from math import gcd
  
  GCD = gcd(a, b)
  LCM = a * b // GCD
  
  print(GCD)
  print(LCM)
  ```


---

### 22/08/08

- BOJ_1543 📌

  ```python
  # amazing method_1
  N = input()
  F = input()
  print(N.count(F))
  
  # amazing method_2
  print(input().count(input()))
  
  ```
  
  
