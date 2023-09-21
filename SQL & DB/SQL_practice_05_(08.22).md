### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql

SELECT *
FROM playlist_track AS A
ORDER BY PlaylistId DESC
LIMIT 5;

-- PlaylistId  TrackId
-- ----------  -------
-- 18          597
-- 17          3290
-- 17          2096
-- 17          2095
-- 17          2094

```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
-- SELECT * FROM tracks LIMIT 5;

SELECT *
FROM tracks AS B
ORDER BY TrackId ASC
LIMIT 5;

--      TrackId = 1
--         Name = For Those About To Rock (We Salute You)
--      AlbumId = 1
--  MediaTypeId = 1
--      GenreId = 1
--     Composer = Angus Young, Malcolm Young, Brian Johnson
-- Milliseconds = 343719
--        Bytes = 11170334
--    UnitPrice = 0.99
           -- ...

```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql

SELECT A.PlaylistId, B.Name
FROM playlist_track AS A INNER JOIN tracks AS B
    ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 10;

-- PlaylistId  Name
-- ----------  -----------------------
-- 18          Now's The Time
-- 17          The Zoo
-- 17          Flying High Again
-- 17          Crazy Train
-- 17          I Don't Know
-- 17          Looks That Kill
-- 17          Live To Win
-- 17          Ace Of Spades
-- 17          Creeping Death
-- 17          For Whom The Bell Tolls

```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.PlaylistId, B.Name
FROM playlist_track AS A LEFT JOIN tracks AS B
    ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC
LIMIT 5;

-- PlaylistId  Name
-- ----------  ------------------------
-- 10          Women's Appreciation
-- 10          White Rabbit
-- 10          Whatever the Case May Be
-- 10          What Kate Did
-- 10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql

SELECT COUNT(*)
FROM tracks INNER JOIN artists
    ON tracks.composer = artists.Name;

-- COUNT(*)
-- --------
-- 402   

```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql

SELECT COUNT(*)
FROM tracks LEFT JOIN artists
    ON tracks.Composer = artists.Name;

-- COUNT(*)
-- --------
-- 3503

```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
두 테이블의 `JOIN`은 상호 테이블의 특정부분만 출력하는 것을 뜻하는데, 
이때 출력 기준을 어디에 두냐에 따라 출력값이 다르다. 

즉, INNER 의 경우는 두 테이블 모두에 동일한 값(id, PK)이 있는 행만 출력을 하고, 
LEFT 의 경우는 기준이 되는 좌측 테이블의 값을 전부 출력한다. 

```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;

-- InvoiceLineId  InvoiceId
-- -------------  ---------
-- 1              1
-- 2              1
-- 3              2
-- 4              2
-- 5              2

```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql

SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;

-- InvoiceId  CustomerId
-- ---------  ----------
-- 1          2
-- 2          4
-- 3          8
-- 4          14
-- 5          23

```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceLineId, B.InvoiceId 
FROM invoice_items AS A INNER JOIN invoices AS B
 ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC
LIMIT 5;

-- InvoiceLineId  InvoiceId
-- -------------  ---------
-- 2240           412
-- 2226           411
-- 2227           411
-- 2228           411
-- 2229           411

```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT InvoiceID, CustomerId
FROM invoices
ORDER BY InvoiceId DESC
LIMIT 5;

-- InvoiceId  CustomerId
-- ---------  ----------
-- 412        58
-- 411        44
-- 410        35
-- 409        29
-- 408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT B.InvoiceLineId, A.InvoiceId, A.CustomerId
FROM Invoices AS A, invoice_items AS B
    ON A.InvoiceId = B.InvoiceId
ORDER BY A.InvoiceId DESC
LIMIT 5;

-- InvoiceLineId  InvoiceId  CustomerId
-- -------------  ---------  ----------
-- 2240           412        58
-- 2226           411        44
-- 2227           411        44
-- 2228           411        44
-- 2229           411        44

```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql

SELECT CustomerId, COUNT(*)
FROM invoice_items AS A LEFT JOIN invoices AS B
    ON A.InvoiceId = B.InvoiceId
GROUP BY B.CustomerId
ORDER BY B.CustomerId ASC
LIMIT 5;

-- CustomerId  COUNT(*)
-- ----------  --------
-- 1           38
-- 2           38
-- 3           38
-- 4           38
-- 5           38


```
