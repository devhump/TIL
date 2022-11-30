# SQL



#####  22.08.16

## Database

- 데이터베이스는 **체계화된 데이터**의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합.
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로
  그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 즉, **몇 개의 자료 파일을 조직적으로 통합**하여
  **자료 항목의 중복을 없애고 자료를 구조화하여 기억**시켜 놓은 자료의 집합체



### Database 구성의 장점

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성 (물리적 / 논리적)
- 데이터 표준화
- 데이터 보안 유지



## RGB

- 관계형 데이터베이스 (RDB, Relational Database)
- 	서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
- 	키와 값(key-value)들의 간단한 관계를 표 형태(relation-table)로 정리한 DB
- | 고유 번호 | 이름   | 주소       | 나이 |
  | --------- | ------ | ---------- | ---- |
  | 1         | 희동이 | 쌍문동 1동 | 9    |
  | 2         | 둘리   | 쌍문동 2동 | 15   |
  | 3         | 도우너 | 쌍문동 3동 | 15   |

  

### 스키마 (schema)

- 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것

- | column  | datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | address | TEXT     |
  | age     | INT      |



### 테이블(table)

- 열(칼럼, 필드)과 행(레코드, 값)의 모델을 사용해 조직된 데이터 요소들의 집합

- schema ▶ table

  - | id   | name   | address    | age  |
    | ---- | ------ | ---------- | ---- |
    | 1    | 희동이 | 쌍문동 1동 | 9    |
    | 2    | 둘리   | 쌍문동 2동 | 15   |
    | 3    | 도우너 | 쌍문동 3동 | 15   |

1. 열(column) **: 각 열에 고유한 데이터 형식 지정**

​		▶ id, name, address, age

2. 행(row) : 실제 데이터가 저장되는 형태

   ▶ 1, 홍길동, 제주, 20 

   ▶ 위 표에는 3명의 정보(레코드)가 저장되어 있음

3. 기본키(Primary Key): 각 행(레코드)의 고유 값

   - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨

     ▶ 위 표에서는 `id` 가 Primary key의 역할을 하고 있음 (ex) 학번, 주민번호, 사번, 군번 등등의 고유값)

     

### 관계형 데이터베이스 관리 시스템(RDBMS)

- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미함
- ex) MySQL, SQLite, PostgreSQL, ORACLE, MS SQL Server



## SQLite

- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스

- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용

- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

  ▶ ***파일 형태의 DB***



### SQLite Data Type

```sqlite
1. NULL
2. INTEGER
	- 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
3. REAL
	- 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
	- 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)
```

- SQLite Type Affinity

  - 특정 칼럼에 저장하도록 권장하는 데이터 타입

  - | Resulting Affinity | Example Typenames <br />From The CREATE TABLE Statement      |
    | :----------------: | :----------------------------------------------------------- |
    |      INTEGER       | INT<br/>INTEGER<br/>TINYINT<br/>SMALLINT<br/>MEDIUMINT<br/>BIGINT<br/>UNSIGNED BIG INT<br/>INT2<br/>INT8 |
    |        TEXT        | CHARACTER(20)<br/>VARCHAR(255)<br/>VARYING CHARACTER(255)<br/>NCHAR(55)<br/>NATIVE CHARACTER(70)<br/>NVARCHAR(100)<br/>TEXT<br/>CLOB |
    |        BLOB        | BLOB<br/>(no datatype specified)                             |
    |        REAL        | REAL<br/>DOUBLE<br/>DOUBLE PRECISION<br/>FLOAT               |
    |      NUMERIC       | NUMERIC<br/>DECIMAL(10,5)<br/>BOOLEAN<br/>DATE<br/>DATETIME  |

    

### SQL (Structured Query Language)
- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리
- |                                                              |                                                              |                                              |
  | :----------------------------------------------------------: | :----------------------------------------------------------: | -------------------------------------------- |
  |  DDL - 데이터 정의 언어<br/>(Data Definition Language)<br/>  | 관계형 데이터베이스 구조(테이블, 스키마)를<br/>정의하기 위한 명령어<br/> | CREATE<br/>DROP<br/>ALTER<br/>               |
  | DML - 데이터 조작 언어<br/>(Data Manipulation Language)<br/> | 데이터를 저장, 조회, 수정, 삭제 등을<br/>하기 위한 명령어<br/> | INSERT<br/>SELECT<br/>UPDATE<br/>DELETE<br/> |
  |   DCL - 데이터 제어 언어<br/>(Data Control Language)<br/>    | 데이터베이스 사용자의 권한 제어를 위해<br/>사용하는 명령어<br/> | GRANT<br/>REVOKE<br/>COMMIT<br/>ROLLBACK     |

  

### SQL Keywords - Data Maipulation Language

- INSERT : 새로운 데이터 삽입(추가)
- SELECT : 저장되어있는 데이터 조회
- UPDATE : 저장되어있는 데이터 갱신
- DELETE : 저장되어있는 데이터 삭제



## Hello, world in SQL

### DB 생성하기

```sqlite
$ sqlite3 DB_name.sqlite3
--동일한 이름의 DB가 있으면, 해당 DB 접속, 
-- 없으면 DB 생성 

splite> .database
```

▶ 이때 ` .  ` 는 sqlite에서 활용되는 명령어



- CSV 파일을 table로 만들기

- ```sql
  -- 생성
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples
  
  -- 생성 확인 및 접근
  sqlite> .tables
  examples
  ```

### SELECT

- ```sq
  sqlite> SELECT * FROM examples;
  1, "둘리", 24, "서울 쌍문동"
  ```

  ▶ **SELECT 문은 특정 테이블의 레코드(행) 정보를 반환 !** 

  - 터미널 view 변경하기

  - ```sqlite
    sqlite> SELECT * FROM examples;
    1, "둘리", 24, "서울 쌍문동"
    
    sqlite> .headers on
    sqlite> SELECT * FROM examples;
    id, name, age, address
    sqlite> .mode column
    sqlite> SELECT * FROM examples;
    id name age address
    -- ---- --- -------
    1  둘리  24  서울 쌍문동 
    
    
    ```

- 테이블 생성 및 삭제 statement

  - `CREATE TABLE`
    - 데이터베이스에서 테이블 생성
  - `DROP TABLE`
    - 데이터베이스에서 테이블 제거



### CREATE

- ```sql
  sqlite> CREATE TAble classmates(
  	id INTEGER PRIMARY KEY,
  	name TEXT
  	);
  
  sqlite> .tables
  classmates examples
  
  sqlite> .schema classmates
  CREATE TAble classmates(
  	id INTEGER PRIMARY KEY,
  	name TEXT
      );
  
  ```

### DROP

- ```sqlite
  sqlite> DROP TABLE classmates;
  sqlite> .tables
  examples
  ```

- 필드 제약 조건

- ```sql
  • NOT NULL : NULL 값 입력 금지
  • UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  • PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  • FOREIGN KEY : 외래키. 다른 테이블의 Key
  • CHECK : 조건으로 설정된 값만 입력 허용
  • DEFAULT : 기본 설정 값
  ```

- ```sqlite
  CREATE TABLE students(
  	id INTEGER PRIMARY KEY, -- 고유 키값
  	name TEXT NOT NULL, 	-- 비어둘 수 없고
  	age INTEGER DEFAULT 1 CHECK (0 < age) -- age 값이 0인지 확인, 기본값은 1 
  ```



### CRUD

1. CREATE

   - INSERT

     - insert a single row into a table

     - ```sql
       -- 테이블에 단일 행 삽입
       INSERT INTO 테이블_이름 (칼럼1, 칼럼2) VALUES (값1, 값2);
       
       -- 테이블에 정의된 모든 칼럼에 맞춰 순서대로 입력
       INSERT INTO 테이블_이름 VALUES (값1, 값2);
       
       ```

     - ```sql
       INSERT INTO classmates (name, age) VALUES ('둘리', 15);
       INSERT INTO classmates VALUES ('도우너', 15, '쌍문동');
       
       -- 확인 키워드
       SELECT * FROM classmates;
       
       -- 한번에 여러 데이터 값 입력하기
       INSERT INTO classmates VALUES
       ('도우너', 15, '쌍문동 1가')
       ('마이클', 15, '쌍문동 2가')
       ('고길동', 15, '쌍문동 3가')
       ('희동이', 9, '쌍문동 3가')
       ('둘리 엄마', 15, '얼음 별');
       
       
       ```

     - **rowid** : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼

2. SELECT ◀ READ
   - query data from a table
   - 테이블에서 데이터를 조회
