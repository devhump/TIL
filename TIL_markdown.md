# 마크다운

---

- [**Markdown**](http://whatismarkdown.com/)은 텍스트 기반의 마크업언어. 

- 간결하고, 용량이 적어 보관이 용이함. 

- 주의📌띄어쓰기 잘 하기!
- [Typora](https://typora.io/) : 마크다운 에디터(편집기)

- 목차
  1. Heading (제목) - 소제목
  2. 목록(list)
  3. Fenced code block
  4. inline code block
  5. 링크걸기
  6. 이미지 삽입
  7. 기타 : 인용문, 표(typora), 텍스트

---

## 1. Heading (제목) - 소제목

#의 개수에 따라 h1~h6까지 표현 가능하다. 

```
#개발 언어 분석 보고서

	##서론 

		###배경

		###목표

	##본론

		###객체지향언어

	##결론

		###python
```

---

## 2. 목록(list)

### 	1) 순서가 없는 리스트: - (hypen), *(asterisk), +(plus)

`- 또는 * 또는 +`

*목록 활용시 단계를  tab / shift+tab 으로 조절*

- 사과 (bullet point)
- 바나나
  - 미니 바나나
    - Dole 버내나
- 딸기
- ...

​			

### 	2)  순서가 있는 리스트

* `숫자.`를 쓰고 엔터쳐서 넘어가면 다음 순번이 자동으로 라벨링

  

* 아침에 일어나서 KDT 교육 듣기

  1. 세수하고 양치
  2. 산책
  3. Syllaverse 홈페이지 접속
     1. 로그인
     2. 대시보드 확인유튜브 라이브에 접속

  4. 유튜브 라이브에 인사를 남긴다.
     1. (있으면) 설문조사를 한다.


---

## 3. Fenced code block

- `(backtick) 기호 3개를 활용하여 작성한다.

  ```
  ```python

- 특정 언어를 명시하면 Syntax highlighting이 적용된다. 

  ```python
  ## python의 경우
  print("hello")
  
  if True:
      print('f')
  #주석
  ```

  ```html
  <!-- html의 경우 -->
  print('hello')
  
  <h1>
      제목
  </h1>
  ```

  

---

## 4. inline code block

- 특정 코드 양옆에 `(backtick) 사용   

```markdown
`특정 코드`
```

ex)

`print` 는 파이썬에서 출력하는 함수이다. 

---

## 5. 링크 넣은 문자열

```markdown
[하고싶은 문구](유알엘)
```

ex)

- [실라버스 링크](www.notion.com)



---

## 6. 이미지 삽입

#### 방법1.

- ![문자열](TIL_markdown.assets/BonoBono.jpg)

```markdown
![문자열](이미지 URL)
```



#### 방법2.

- 원하는 이미지를 마우스로 drag & drop

​	***✔이때, 이미지는 상대경로로 설정할 것*** 

- 절대경로(c드라이브 - 등등)

- 상대경로(`마크다운.asset` 폴더 같이 공유)

---

## 7-1. 인용문(BlockQuote)

- ` >를 사용 `

> life is short, you need python

```markdown
> life is short, you need python
```

- 중첩가능

  > quoute 1
  >
  > > quoute 2
  > >
  > > > quoute 3

```markdown
quoute 1

> quoute 2
>
> > quoute 3
```

- 다른 마크다운 요소 포함 가능

  > this is example
  >
  > - test
  >
  >   ```
  >   code
  >   ```

---

## 7-2. 표(table)

(타이포라 기능을 적극 활용하자.)



- 본문 > 표 > 표 삽입 (ctrl + t)

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

---

## 7-3. 텍스트(text)

- **굵게** : ` **` 띄어쓰기가 없어야 함

  `ctrl+B` 도 가능

- *기울림(이태릭체)* `*기울임*``

  `ctrl+i` 도 가능

- ~~취소선~~ `~~취소선~~`

- 수평선 `---` 또는 `***`

---

- 굵게 기울임 `***문자***` 	ex) ***안녕***



---

## 7-4. markdown 에서의 HTML 활용

```
<details>
    <summary>7월</summary>1일 <br> 2일 <br> 3일
</details>
```

- <details>
      <summary>7월</summary>1일 <br> 2일 <br> 3일
  </details>

---

## Reference

- https://gist.github.com/ihoneymon/652be052a0727ad59601