---
tags: [markdown, syntax, KDT]
---

- 옵시디언 특화 문법 👉  [[markdown for Obsidian]]
- 자주 쓰는 수식 기호 👉  [[LaTeX]]

```ad-note

- [[#intro|intro]]
	- [[#intro#마크다운 특징|마크다운 특징]]
	- [[#intro#개요|개요]]
- [[#1. Heading (제목) - 소제목|1. Heading (제목) - 소제목]]
	- [[#intro#1-1) 방법1. `#` 이용하기|1-1) 방법1. `#` 이용하기]]
	- [[#intro#1-2) 방법2. 등호(=)나 대시(-) 이용하기|1-2) 방법2. 등호(=)나 대시(-) 이용하기]]
- [[#2. 목록(list)|2. 목록(list)]]
- [[#2. 목록(list)#2-1) 순서가 없는 리스트: - (hypen), *(asterisk), +(plus)|2-1) 순서가 없는 리스트: - (hypen), *(asterisk), +(plus)]]
- [[#2. 목록(list)#2-2)  순서가 있는 리스트|2-2)  순서가 있는 리스트]]
- [[#3. Fenced code block|3. Fenced code block]]
- [[#4. inline code block|4. inline code block]]
- [[#5. 링크 넣은 문자열|5. 링크 넣은 문자열]]
- [[#6. 이미지 삽입|6. 이미지 삽입]]
	- [[#2-2)  순서가 있는 리스트#6-1. 이미지 삽입 방법1.|6-1. 이미지 삽입 방법1.]]
	- [[#2-2)  순서가 있는 리스트#6-1. 이미지 삽입 방법2.|6-1. 이미지 삽입 방법2.]]
- [[#7. 기타 세부적인 내용|7. 기타 세부적인 내용]]
	- [[#7. 기타 세부적인 내용#7-1. 인용문(BlockQuote)|7-1. 인용문(BlockQuote)]]
	- [[#7. 기타 세부적인 내용#7-2. 표(table)|7-2. 표(table)]]
	- [[#7. 기타 세부적인 내용#7-3. 텍스트(text) 강조|7-3. 텍스트(text) 강조]]
	- [[#7. 기타 세부적인 내용#7-4. markdown 에서의 HTML 활용|7-4. markdown 에서의 HTML 활용]]
	- [[#7. 기타 세부적인 내용#7-5. 각주 넣기 (footnote)|7-5. 각주 넣기 (footnote)]]
	- [[#7. 기타 세부적인 내용#7-6. 할 일 목록 만들기|7-6. 할 일 목록 만들기]]
	- [[#7. 기타 세부적인 내용#7-7. about Escape sequence in markdown|7-7. about Escape sequence in markdown]]
- [[#8. 그 외|8. 그 외]]
	- [[#8. 그 외#8-1. 마크다운 관련 자료|8-1. 마크다운 관련 자료]]
	- [[#8. 그 외#8-2. 개발자에게 문서 작성이란?|8-2. 개발자에게 문서 작성이란?]]
		- [[#8-2. 개발자에게 문서 작성이란?#[Typora](https://typora.io/)|[Typora](https://typora.io/)]]
```


### intro
#### 마크다운 특징
  - 워드프로세서(한글/ MS word)는 다양한 서식과 구조를 지원하며, 문서에 즉각적으로 반영

  - 마크다운은 가능한 읽을 수 있도록 최소한의 문법으로 구조화 (make it as readable as possible)

  - `Github` 등의 사이트에서는 파일명이 `README.md` 인 것을 모두 보여줌
    - 오픈소스의 공식 문서를 작성하거나 개인 프로젝트의 프로젝트 소개서로 활용

    - 혹은 모든 페이지에 `README.md`를 넣어 문서를 바로 볼 수 있도록 활용

  - 다양한 기술블로그에서는 정적사이트 생성기(Static site generator)
    - Jerkyll, Gastby, Hugo, Hexo 등을 통해 작성된 마크다운을 HTML, CSS, JS 파일 등으로 변환하고
    - Github pages 기능을 통해 호스팅(외부 공개)

  - 다양한 개발 환경 뿐만 아니라 일반 SW에서도 많이 사용되고 있음
    - Jupyter notebook에서는 별도의 마크다운 셀이 있어, 데이터 분석 등을 하는 과정해서 프로젝트 내용과 분석 결과를 정리함 
    - Notion과 같은 메모/노트 필기 SW에서도 기본 문법으로 마크다운을 채택


#### 개요

  - [**Markdown**](http://whatismarkdown.com/)은 텍스트 기반의 마크업언어. 
  - 간결하고, 용량이 적어 보관이 용이함. 
  - 주의📌띄어쓰기 잘 하기!
  - [Typora](https://typora.io/) : 마크다운 전용 에디터(편집기)


---

## 1. Heading (제목) - 소제목

- `#` 의 개수에 따라 h1~h6까지 표현 가능하다.
- 문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되서는 안됨


#### 1-1) 방법1. `#` 이용하기 
```
[[개발]] 언어 분석 보고서

	##서론 

		###배경

		###목표

	##본론

		###객체지향언어

	##결론

		###python
```

#### 1-2) 방법2. 등호(=)나 대시(-) 이용하기
```markdown

밑에 등호(=)를 연속으로 표시하면, 제목1이 된다
================================

밑에 대시(-)를 연속으로 표시하면, 제목2가 된다.
----------------------------------------------
```

---

## 2. 목록(list)

### 	2-1) 순서가 없는 리스트: - (hypen), *(asterisk), +(plus)

`- 또는 * 또는 +`

*목록 활용시 단계를  tab / shift+tab 으로 조절*

- 사과 (bullet point)
- 바나나
  - 미니 바나나
    - Dole 버내나
- 딸기
- ...

- 💡 가독성을 위해서 다른 마크다운 문법에도 많이 쓰이는 `*` 보다는 `+` 나 `-` 를 활용하자.
- 💡 또, 소스 코드 상으로 볼 때의 가독성을 위해서라도 +와 -를 섞어 쓰는게 더 좋다.
```
+ 계층을 나눈 순서가 없는 리스트
	- 아래 계층
+ 위 계층
```
​			

### 	2-2)  순서가 있는 리스트

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

- ` ` ` (backtick) 기호 3개를 활용하여 작성한다.

  ```
	```python

 ```
- 특정 언어를 명시하면 Syntax highlighting이 적용된다. 
```

  ```python
  ## python의 경우
  print("hello")
  
  if True:
      print('f')
  [[주석]]
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



```
HTML에서는

<code>특정 코드</code> 

처럼 사용을 한다.
```

 

---

## 5. 링크 넣은 문자열

- 특정 파일들 포함하여 연결 시킬 수도 있음

```markdown
[하고싶은 문구](URL)
```

또는

```
문장 중간에 링크를 넣고 싶을 때, [네이버로 이동][별칭] 이렇게 설정 할 수도 있다. 단, ✔옵시디언에서는 불가

[별칭]: https://www.naver.com

```

---

## 6. 이미지 삽입

#### 6-1. 이미지 삽입 방법1.

![](assets/ccobuk.jpg)
```
![문자열](이미지 URL)
```



#### 6-1. 이미지 삽입 방법2.

- 원하는 이미지를 마우스로 drag & drop

​	***✔이때, 이미지는 상대경로로 설정할 것*** 

- 절대경로(c드라이브 - 등등)

- 상대경로(`마크다운.asset` 폴더 같이 공유)

---
## 7. 기타 세부적인 내용

### 7-1. 인용문(BlockQuote)

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

### 7-2. 표(table)
- 아래와 같은 형식으로 작성한다. 
- 이때, `:`을 사용하여 좌/우측/가운데 정렬이 가능하다
	- 좌측 정렬 `:---`
	- 우측 정렬 `---:
	- 가운데 정렬 `:---:`
- 
```
|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

```

- (타이포라 기능을 적극 활용하자.)
	- 본문 > 표 > 표 삽입 (ctrl + t)

```
|  헤드1   | 2    | 3    |
| :--- | :---: | ---: |
| 내용1    |  2   | 3    |
| 내용2    |  2   | 3    |

```

| 헤드1 |  2  |   3 |
|:----- |:---:| ---:|
| 내용1 |  2  |   3 |
| 내용2 |  2  |   3 |
| 내용3 |  2  |   3 |

- HTML 방식으로도 작성이 가능하다.

```html
<table>
	<thead>
		<tr>
			<th>헤드1</th>
			<th>헤드2</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>내용1</td>
			<td>내용2</td>
		</tr> 
		<tr> 
			<td>내용3</td> 
			<td>내용4</td> 
		</tr> 
	</tbody> 
</table>
```

<table> <thead> <tr> <th>헤드1</th> <th>헤드2</th> </tr> </thead> <tbody> <tr> <td>내용1</td> <td>내용2</td> </tr> <tr> <td>내용3</td> <td>내용4</td> </tr> </tbody> </table>

---

### 7-3. 텍스트(text) 강조

- **굵게** : ` **`처럼 띄어쓰기가 없어야 함

  `ctrl+B` 도 가능

  ```
  **bold text**
  __bold text__
  ```

  

- *기울림(이태릭체)* `*기울임*``

  `ctrl+i` 도 가능

  ```
  *italic text*
  _italic text_
  ```

  

- ~~취소선~~(Strikethrough) `~~취소선~~`

- 수평선(Horizontal divider) `---` 또는 `***` 또는 `___`

  ```
  ---
  ***
  ___ (underscores *3)
  ```

- ==강조== `(==)`
```
==강조할 텍스트==
```
  
- 밑줄 <U>밑줄</U>
```
<U>밑줄 표시할 내용</U>
```
---

- 굵게 기울임 `***문자***` 	ex) ***안녕***

- 그 외 여러 강조 표시 
```
<kbd>1. hello</kbd>
<a>2. hello</a>
<code>3. hello</code>
<mark>4. hello</mark>
```
<kbd>1. hello</kbd>
<a>2. hello</a>
<code>3. hello</code>
<mark>4. hello</mark>


---

### 7-4. markdown 에서의 HTML 활용

- 문단 내 줄바꿈 `<br>`

문단 내에서 <br> 을 쓰면 줄 바꿈이 가능 합니다.

```
문단 내에서 <br> 을 쓰면 줄 바꿈이 가능 합니다.
```

- 화살표 토글
 
```
<details>
    <summary>7월</summary>1일 <br> 2일 <br> 3일
</details>
```

- <details>
      <summary>7월</summary>1일 <br> 2일 <br> 3일
  </details>


### 7-5. 각주 넣기 (footnote)

- 문서 중간에 `[^별칭]` 기호를 넣고, 문서 마지막에 `[^별칭]:` 성명을 추가하면된다.
- 문서 중간에 [^별칭] 기호를 넣고, 문서 마지막에 [^별칭]: 성명을 추가하면된다
- 이때 별칭은 **중복이 있으면 안 된다.**

```md
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: meaningful!

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: meaningful!

[^bignote]: Here's one with multiple paragraphs and code.


### 7-6. 할 일 목록 만들기
```
- [ ] 대시(-) 뒤와 대괄호([]) 사이에 공백이 있어야 한다. 
- [X] X 표시를 해주면 완료한 목록이 된다.
- [O] 편집기에 따라, X 대신 아무 문자를 넣어도 작동하는 경우도 있다.
	- case by case
```

- [ ] 목록만들기1
- [X] 목록만들기2
- [O] 목록 만들기3

```
- [ ] 목록만들기1
- [X] 목록만들기2
- [O] 목록 만들기3
```


### 7-7. about Escape sequence in markdown

1. 코드 블럭 표현하기
````
```python
print("이렇게 하면 코드블록을 표현할 수 있다.")
```
````

2. 백틱(backtick) 기호 표현
- ``List`1``
- `` ` ``


---

## 8. 그 외 

### 8-1. 마크다운 관련 자료

- [GitHub Flavored Markdown]([GitHub Flavored Markdown Spec](https://github.github.com/gfm/))
- [기본 쓰기 및 서식 지정 구문 - GitHub Docs](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Cheat Sheet | Markdown Guide](https://www.markdownguide.org/cheat-sheet/)
- https://gist.github.com/ihoneymon/652be052a0727ad59601



### 8-2. 개발자에게 문서 작성이란?

- 백엔드 개발자를 꿈꾸는 학생 개발자들에게 (https://d2.naver.com/news/3435170) 
  - 레벨 2 개발자 : ‘자신이 경험한 사용법을 문서화해서 팀 내에 전파할 수 있음’

- Google Technical Writing (https://developers.google.com/tech-writing)
  - Every engineer is also a write

- Technical writing conference (https://engineering.linecorp.com/ko/blog/write-the-docs-prague-2018-recap/ )
  - Clova 기술 문서 작성 및 관리 업



#### [Typora](https://typora.io/)

- 기존 텍스트 에디터(예- visual studio code), IDE 뿐만 아니라 마크다운 전용 에디터를 활용하여 문서를 작성할 수 있음
- Typora는 문법을 작성하면 바로 일반적으로 보이는 모습으로 변하여 처음 작성

- **Typora 이미지 관련 TIP**
  - 이미지는 아래의 설정을 해두면 마크다운 파일이 있는 위치에 md-images 폴더를 만들고, 가능한 이미지들을 모두 복사하여 상대경로로 표현함
    - 상대 경로 예시: ./md-images/untitle.png
    - 절대 경로 예시: C:/HPHK/Desktop/TIL/untitle.pn