# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
# 인스턴트 생성
director = Director()
director.name = '봉준호'
director.debut = "1993-01-01"
director.country = "KOR"
director.save()

Director.objects.create(name='김한민', debut=datetime.date(1999,1,1), country="kor")
Director.objects.create(name='최동훈', debut=datetime.date(2004,1,1), country="kor")
Director.objects.create(name='이정재', debut=datetime.date(2022,1,1), country="kor")
Director.objects.create(name='이경규', debut=datetime.date(1992,1,1), country="kor")
Director.objects.create(name='한재림', debut=datetime.date(2005,1,1), country="kor")
Director.objects.create(name='Joseph Kosinski', debut=datetime.date(1999,1,1), country="kor")
Director.objects.create(name='김철수', debut=datetime.date(2022,1,1), country="kor")
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
a = Genre.objects.get(id=1)
a.title = "액션"
a.save()

# 기존 아이디 값 조회 후 값 삭제 (Delete)
a = Genre.objects.get(id=3)
a.delete()

Genre.objects.create(id=2, title="드라마")
Genre.objects.create(id=3,title="사극")
Genre.objects.create(id=4,title="범죄")
Genre.objects.create(id=5,title="스릴러")
Genre.objects.create(id=6,title="SF")
Genre.objects.create(id=7,title="무협")
Genre.objects.create(id=8,title="첩보")
Genre.objects.create(id=9,title="재난")
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director = Director.objects.all()

for elem in director:
    print(elem.name, elem.debut, elem.country)
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
a = Director.objects.get(id=1)
print(a.name, a.debut, a.country)
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
a = Director.objects.get(country="USA")
print(a.name, a.debut, a.country)
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
현재 Director 테이블에 저장된 data들 중, 
국적이 'USA'인 data가 없다. 

-> table에 저장된 data 중 없는 조건으로
 검색을 하니까 맞는 쿼리가 없다고 나온다. 
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
a = Director.objects.get(name="Joseph Kosinski")
a.country = "USA"
a.save()

print(a.name, a.debut, a.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
a = Director.objects.get(country="KOR")
print(a.name, a.debut, a.country)
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
> 

```
쿼리를 보냈는데, 테이블에 같은 조건('KOR')을 가진 데이터들이 많아서.
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
A = Director.objects.filter(country='KOR')

for result in A:
    print(result.name, result.debut, result.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get은 하나의 단일값(객체)를 받아오지만, 
filter는 해당 조건에 해당하는 여러 값들을 하나의 객체 리스트로 받아 온다.
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
A = Director.objects.get(name="김철수")
A.delete()
```