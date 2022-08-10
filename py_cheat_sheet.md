### 삭제

- del 

  - `del` 은 메서드가 아니라 ***예약어이다.*** (ex) `if` `for` `or` `and`)
  - `del list(a)`
  - `del list[3:5]`

  ```python
  int_list = [1, 2, 3, 4, 5, 6, 7]
  str_list = ['가','나','다','라','마']
  
  del int_list[0]  # 한개의 요소를 삭제
  print(int_list)
  [2, 3, 4, 5, 6, 7]
  
  del str_list[3:]  # 여러개의 요소를 삭제
  print(str_list)
  ['가', '나', '다']
  ```



- remove()

  - 하나의 값만 삭제하는 메서드
  - `variable.remove()`

  ```python
  numbers = [1, 2, 2, 3, 3, 3]  
  # 숫자가 중복된 리스트
  numbers.remove(3)
  print(numbers)
  >>> [1, 2, 2, 3, 3]  # '첫번째 숫자3' 삭제
  
  # 여러개의 인자값 삭제 (반복문 이용)
  numbers = [1, 2, 2, 3, 3, 3]
  for _ in numbers :
      numbers.remove(3)
  print(numbers)
  >>> [1, 2, 2]  # 숫자 3이 전부 삭제
  ```

  

## 문자열 (string)

### 교체