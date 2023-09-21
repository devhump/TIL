### 예제 03. 풀이

```bash
TypeError
unsupported operand type(s) for +: 'int' and 'str'
```

- `sum` 에는 `int` 형 혹은 `str` 형이 와야함

```python
# 수정된 코드
numbers = input().split()

sum_numbers = 0

for i in numbers:
    i = int(i)
    sum_numbers += i
# str이 저장된 list numbers를 
# int형 으로 바꿔주면서 각 값을
# sum_numbers 에 저장    
    
print(sum_numbers)
```

---

### 예제 04. 풀이

```python
words = list(map(int, input().split()))
# map 은 두개 이상의 인자 필요
print(words)
```

- 숫자를 입력 받아 단순 출력 하는 것, `int` 형 ▶ `str` 형으로

```py
# 수정된 코드
words = list(map(str, input().split()))
print(words)
```



---

### 예제 05. 풀이

- 오류코드

```python
number = 22020718
print(len(number))
# int 형은 len의 인자가 될 수 없음!
```

- `len()` 

  `len(s)`은 객체의 길이 (항목 수)를 돌려줍니다. 인자는 시퀀스 (문자열, 바이트열, 튜플, 리스트 또는 range 같은) 또는 컬렉션 (딕셔너리, 집합 또는 불변 집합 같은) 일 수 있습니다. [파이썬 자습서-내장함수](https://docs.python.org/ko/3/library/functions.html#len)
  
- 수정 코드

```python
number = str(22020718) 
# 숫자 개수를 단순 출력이라 str형변환으로 해결
print(len(number))
```



---

### 예제 06. 풀이

- 오류코드

  ```python
  N = 10
  answer = ( ) 
  # 빈 튜플을 선언
  for number in range(N + 1):
      answer.append(number * 2)
  
  print(answer)
  ```

  -  튜플은 값의 변경(추가) 불가! ▶ 리스트로 변경!

- 수정코드

  ```python
  N = 10
  answer = [ ]
  # 비어있는 리스트로 변경
  for number in range(N + 1):
      answer.append(number * 2)
  
  print(answer)
  ```



---

### 예제 07. 풀이

- 오류코드

  - ```python
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 총합 55
    
    total = 0
    count = 0
    
    for number in number_list:
        total += number
    count += 1 
    # indent 실수로 1회만 실행
    
    print(total // count)
    # 나머지 버리고 몫만 나타냄
    ```

- 수정코드

  - ```python
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 총합 55
    
    total = 0
    count = 0
    
    for number in number_list:
        total += number
    	count += 1 
    # cnt 반복 실행 -> 결과:10
    
    print(total / count)
    # 결과 5.5 (float)
    ```

    

---

### 예제 08. 풀이

- 오류코드

  - ```python
    word = "HappyHacking"
    
    count = 0
    
    for char in word:
        if char == "a" or "e" or "i" or "o" or "u":
            # char == "a" 의 값과는 별개로, 나머지 값들이 항상 True
            count += 1
    
    print(count)
    ```

    - 코딩에서는 `0`, 또는 `False` 를 제외한 나머지 값(정수, 문자열 등)은 `True`를 의미
    - 결과적으로 `T/F or True` 와 같은 형태가 되어, 무조건 실행

- 수정코드

  - ```python
    word = "HappyHacking"
    
    count = 0
    
    for char in word:
        if char == "a" or char == "e" or char == "i" or char ==  "o" or char ==  "u": 
            #이게 제대로된 코드
            count += 1
    
    print(count)
    ```



---

### 예제 09. 풀이

- 오류코드

  - ```python
    from pprint import pprint
    
    fruits = [
        "Soursop",
        "Grapefruit",
        "Apricot",
        "Juniper berry",
        "Feijoa",
        "Blackcurrant",
        "Cantaloupe",
        "Salal berry",
    ]
    
    fruit_count = {}
    
    for fruit in fruits:
        if fruit not in fruit_count:
            fruit_count = {fruit: 1}
            # 이코드가 실행 될 때 마다 초기화
        else:
            fruit_count[fruit] += 1
    
    pprint(fruit_count)
    ```

- 수정코드

  - ```python
    from pprint import pprint
    
    fruits = [
        "Soursop",
        "Grapefruit",
        "Apricot",
        "Juniper berry",
        "Feijoa",
        "Blackcurrant",
        "Cantaloupe",
        "Salal berry",
    ]
    
    fruit_count = {}
    
    for fruit in fruits:
        if fruit not in fruit_count:
            fruit_count[fruit] = 1 #이 부분을 수정
        else:
            fruit_count[fruit] += 1
    
    pprint(fruit_count)
    ```

    - 처음보는 과일이 나오면 val 값을 1로 해서 딕셔너리에 **추가** `{'과일명' : 1}`



---

### 예제 10. 풀이

- 오류코드

  - ```python
    number_list = [1, 23, 9, 6, 91, 59, 29]
    max = max(number_list) # 2. but 실제로는 이 줄이 문제
    
    number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
    max2 = max(number_list2) # 1. 오류는 여기서 발생
    
    if max > max2:
        print("첫 번째 리스트의 최댓값이 더 큽니다.")
    
    elif max < max2:
        print("두 번째 리스트의 최댓값이 더 큽니다.")
    
    else:
        print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
    ```

    - ```bash
      예외가 발생했습니다. TypeError
      'int' object is not callable
      ```

  - 첫번째 `max` 에서 변수명에 예약어를 사용 ▶ 이때는 문제 없으나, 

  - 두번째 `max2` 선언 시, `max()` 호출시 충돌 발생 (📌 이미 변수명으로 사용되는 중...)

- 수정코드

  - ```python
    
    number_list = [1, 23, 9, 6, 91, 59, 29]
    max_num1 = max(number_list)
    # 예약어 max -> max_num로 변수명 변경
    
    number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
    max_num2 = max(number_list2)
    # 예약어 max -> max_num로 변수명 변경
    
    if max_num1 > max_num2:
        print("첫 번째 리스트의 최댓값이 더 큽니다.")
    
    elif max_num1 < max_num2:
        print("두 번째 리스트의 최댓값이 더 큽니다.")
    
    else:
        print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
    ```

    

---

### 예제 11. 풀이

- 오류 코드

  - ```python
    from pprint import pprint
    
    def movie_info(movie, genres):
        genres_names = []
        genre_ids = movie["genre_ids"]
        for genre_id in genre_ids:
            for genre in genres:
                if genre_id == genre["id"]:
                    genre_name = genre["name"]
                    genres_names.append(genre_name)
    
        new_movie_info = {
            "genre_names": genres_names,
            "id": movie["id"],
            "overview": movie["overview"],
            "title": movie["title"],
            "vote_average": movie["vote_average"],
        } 
    
    if __name__ == "__main__":
        movie = {
            "adult": False,
            "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
            "genre_ids": [18, 80],
            "id": 278,
            "original_language": "en",
            "original_title": "The Shawshank Redemption",
            "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
            "popularity": 67.931,
            "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
            "release_date": "1995-01-28",
            "title": "쇼생크 탈출",
            "video": False,
            "vote_average": 8.7,
            "vote_count": 18040,
        }
    
        genres_list = [
            {"id": 28, "name": "Action"},
            {"id": 12, "name": "Adventure"},
            {"id": 16, "name": "Animation"},
            {"id": 35, "name": "Comedy"},
            {"id": 80, "name": "Crime"},
            {"id": 99, "name": "Documentary"},
            {"id": 18, "name": "Drama"},
            {"id": 10751, "name": "Family"},
            {"id": 14, "name": "Fantasy"},
            {"id": 36, "name": "History"},
            {"id": 27, "name": "Horror"},
            {"id": 10402, "name": "Music"},
            {"id": 9648, "name": "Mystery"},
            {"id": 10749, "name": "Romance"},
            {"id": 878, "name": "Science Fiction"},
            {"id": 10770, "name": "TV Movie"},
            {"id": 53, "name": "Thriller"},
            {"id": 10752, "name": "War"},
            {"id": 37, "name": "Western"},
        ]
    
        pprint(movie_info(movie, genres_list))
    ```

    - `def movie_info(movie, genres)` 에서 실컷 작업하고, 반환 값이 없다. ▶ `retrun` 값 추가 

- 수정코드

  - ```python
    def movie_info(movie, genres):
        genres_names = []
        genre_ids = movie["genre_ids"]
        for genre_id in genre_ids:
            for genre in genres:
                if genre_id == genre["id"]:
                    genre_name = genre["name"]
                    genres_names.append(genre_name)
    
        new_movie_info = {
            "genre_names": genres_names,
            "id": movie["id"],
            "overview": movie["overview"],
            "title": movie["title"],
            "vote_average": movie["vote_average"],
        } 
        	return new_movie_info # 이부분만 추가하면됨 (indent 주의!)
    ```



---

