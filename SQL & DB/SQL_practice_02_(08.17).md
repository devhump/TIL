# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age),MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;
```

```
MAX(height)  MIN(height)  MAX(weight)  MIN(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE height >= 160 and height <= 170;
```

```
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 and waist LIKE '_%' ORDER BY waist DESC LIMIT 5;

SELECT waist FROM healthcare WHERE is_drinking = 1 and waist != '' ORDER BY waist DESC LIMIT 5;
```

```sql
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;
```

```
COUNT(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
```

```
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight*10000/	(height*height) >= 30;
```

```
COUNT(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight*10000/(height*height) FROM healthcare WHERE smoking = 3 ORDER BY weight*10000/(height*height) DESC LIMIT 5;

SELECT id, weight*10000/(height*height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 
```

```
id      weight*10000/(height*height)
------  ----------------------------
231431  50
934714  49
722707  48
947281  47
948801  47

id      BMI
------  ---
231431  50
934714  49
722707  48
947281  47
948801  47
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
-- 시도별 총흡연인구수(내림차순, 상위 5지역)

SELECT sido, COUNT(smoking)
FROM healthcare
WHERE smoking <> ""
GROUP BY sido
ORDER BY COUNT(smoking) DESC
LIMIT 5;

-- SELECT DISTINCT sido FROM healthcare ORDER BY sido DESC;
```

```
sido  COUNT(smoking)
----  --------------
41    247180
11    166142
26    69022
48    68514
28    58338
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
-- 시도별 총흡연인구수(오름차순, 상위 5지역)

SELECT sido, COUNT(is_drinking)
FROM healthcare
WHERE is_drinking <> ""
GROUP BY sido
ORDER BY COUNT(is_drinking) ASC
LIMIT 5;
```

```
sido  COUNT(is_drinking)
----  ------------------
41    247268
11    166174
26    69024
48    68521
28    58344
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
-- 양쪽 시력이 둘 다 0.5 이하인 사람들의 수(내림차순, 시도별)

SELECT sido, COUNT (*) FROM healthcare 
WHERE va_left <= 0.5 AND va_right <= 0.5 AND va_left <> "" AND va_right <> ""
GROUP BY sido
ORDER BY COUNT(*) DESC
LIMIT 5;

```

```
sido  COUNT (*)
----  ---------
41    18613
11    15477
48    5545
26    5380
47    5002
```