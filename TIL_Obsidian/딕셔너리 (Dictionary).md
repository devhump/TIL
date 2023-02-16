```
1. 해시테이블
2. 딕셔너리 기본 문법
3. 딕셔너리 메서드
```

### 1. 해시 테이블
- 파이썬에는 딕셔너리(dict) 자료구조가 내장 되어 있다. 
- ***Non-sequence & Key-Value***

```python

{
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}
```

➡️ Key는 immutable (변경 불가능)

- **Key : Value** 가 저장되는 원리가 무엇일까?
- 일단 리스트를 이용해 **Key: Value**를 저장해보자.

# 🔥 도표


- 딕셔너리는 **해시 테이블(Hash Table)** 을 이용하여 Key: value 를 저장



- 해시 함수: 임의 길이의 데이터를 고정 실이의 데리터로 매핑하는 함수 
- 해시 : 해시 함수를 통해 얻어진 값
- 파이썬의 딕셔너리(Dictionary)는 해시 함수와 해시 테이블을 이용하여 삽입, 삭제, 수정, 조회 ***연산의 속도가 리스트보다 빠르다.***


### 2. 딕셔너리 기본 문법

- 기본적인 딕셔너리 사용법(선언)
- 변수 = { key1: value1, key2: value2 ...}
```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a)
>>> {"name": "kyle","gender": "male","address": "Seoul"
}
``` 


- 기본적인 딕셔너리 사용법(**삽입/수정**)
- 딕셔너리[key] = value
- 내부에 해당 key가 없으면 삽입, 있으면 수정

```python
# 삽입
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

a["job"] = "coach"

print(a)
>>> {"name": "kyle","gender": "male","address": "Seoul", "job": "coach"}

#################################################

# 수정
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

a["name"] = "Justin"

print(a)
>>> {"name": "Justin","gender": "male","address": "Seoul"}
``` 

- 기본적인 딕셔너리 사용법 (**삭제**)
- 딕셔너리.pop(key)
	- 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 keyError 발생
```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

gender = a.pop("gender")

print(a)
print(gender)
>>> {"name": "kyle","address": "Seoul"}
>>> male
```

```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

phone = a.pop("phone")

print(a)
print(phone)

```
- 에러발생
- ![](assets/Pasted%20image%2020230216184112.png) 

- 기본적인 딕셔너리 사용법 (**삭제**)
- 딕셔너리.pop(key, default)
- 두 번째 인자로 default값(기본값)을 지정하여 KeyError 방지 가능

```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

phone = a.pop("phone", "010-1234-5678")

print(a)
print(phone)
>>> {"name": "kyle","gender": "male","address": "Seoul"}
>>> 010-1234-5678
```

- 기본적인 딕셔너리 사용법 (**조회**)
- key에 해당하는 value 반환

- `딕셔너리[Key]` 또는 `딕셔너리.get(key)`
```python
# 딕셔너리[Key]

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a["name"])
>>> Kyle

#################################

# 딕셔너리.get(key)

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.get("name"))
>>> Kyle
```


- 기본적인 딕셔너리 사용법 (**조회**)
- `딕셔너리[key]`
```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a["phone"])
```

- 에러발생
	- ![](assets/Pasted%20image%2020230216184957.png)

- `딕셔너리.get(key,default)`
```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.get("phone"))
>>> none

##################################

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.get("phone", "없음"))
>>> 없음
```


- 딕셔너리 기본 문법 정리
| 선언 | 변수 = { Key: value1, key2: value2... } |
| --- | --- |
| 삽입 | 딕셔너리[key] = value |
| 삭제 | 딕셔너리.pop(key, default) |
| 조회 | 딕셔너리[key] 또는 딕셔너리.get(key, default) |


### 3. 딕셔너리 메서드
```
1) .keys()
2) .values()
3) .items()
```

#### 1) .keys()
- 딕셔너리의 **Key 목록**이 담긴 dict_keys 객체 반환

```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.keys())
>>> dict_keys(['name', 'gender', 'address'])

##################################

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

for key in a.keys():
	print(key)
>>> name
gender
address

##################################

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

for key in a:
	print(key)
>>> name
gender
address
```

- 2) .values()
- 딕셔너리의 **value 목록**이 담긴 dict_values 객체 반환
```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.values())
>>> dict_values(['kyle', 'male', 'Seoul'])

##############################################

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

for value in a.values():
	print(value)

>>>Kyle
male
Seoul
```


- .items()
	- 딕셔너리의 **(key, value) 쌍 목록**이 담긴 dict_items 객체 반환

```python
a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

print(a.items())
>>> dict_items([('name', 'kyle'),('gender', 'male'),('address','Seoul')])


a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

for item in a.items():
	print(item)
>>>('name', 'kyle')
('gender', 'male')
('address','Seoul')

a = {
	 "name" : "kyle",
	 "gender" : "male",
	 "address" : "Seoul",
}

for key, value in a.items():
	print(key, value)
>>> name Kyle
gender male
address Seoul
```


- 딕셔너리 활용 연습 (JUNGOL)
	- [# 945 : 기타 자료형 - 자가진단 5](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4372&sca=pyd0)
	- [# 946 : 기타 자료형 - 자가진단 6](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4373&sca=pyd0)
	- [# 953 : 기타 자료형 - 형성평가 6](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4380&sca=pyd0)
	- 