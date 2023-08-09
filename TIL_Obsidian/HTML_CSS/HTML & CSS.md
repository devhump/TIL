---
tag: [CodingApple/HTML_CSS, HTML, CSS]
---

#### 관련 문서
```dataview
list from #HTML or #CSS or #CodingApple/HTML_CSS  
SORT file.name ASC
```
#### intro
- 에디터 추천 👉 [Brackets 에디터](https://brackets.io/)
	- `ctrl` + `space` 자동완성 단축키
- HTML : Hypertext Markup Language
	- 이때, 마크업 언어는 **자료의 구조를 표현하기 위한 언어**

##### HTML 파일 기본 템플릿
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

- HTML 문서는 확장자가 `.html`로 끝나도록 저장
- 모든 HTML 문서는 위의(👆) 코드를 가지고 있어야 HTML 파일로 인식합니다.
- `<head>` 내부엔 사이트 생성에 필요한 인코딩형식, 사이트제목, 필요한 CSS나 JS파일 등이 들어갈 수 있으며<br>`<body>` 내부엔 실제 웹사이트에서 보여줄 글, 그림 등을 적어주시면 됩니다.


### 태그의 종류
```html
<p>글 본문</p>

<h1>글 제목</h1>

<img src="이미지 경로">

<a href="">링크</a>

<button>버튼</button>
<ul>
	<li>리스트</li>
</ul>
<ol>
	<li>리스트</li>
</ol>
```

1. 기본적으로 태그는 여는 태그, 닫는 태그로 구성된다. 
	- `<img>` 태그와 같이 예외도 존재한다.
2. 특정 태그는 속성을 가진다.
	- `href="이동할 링크"` , `src="파일 경로"`
3. 태그 내부에 태그의 중복이 가능하다.
4. HTML은 마크업 언어 이기 때문에 되도록 자료의 구조를 쉽게 파악할 수 있도록 **용도에 맞는 태그를 사용하는 것이 좋다** → ***웹 표준에 부합*** 

![텍스트 요소](../KDT/Web/01.%20Happy%20Web.md#텍스트%20요소)

![그룹 컨텐츠](../KDT/Web/01.%20Happy%20Web.md#그룹%20컨텐츠)

```ad-question
- Q. 이미지를 누르면 구글로 이동하게 하려면?
	```html
	<a href="http://naver.com">
	  <img src="">
	</a>
	```
```

```ad-question
- Q. 글자 일부를 누르면 구글로 이동하는 방법?
	```html
	  <p>글자 중에서 <a href="http://google.com"> 이걸 누르면 이동 </a></p>
	```
```


### 기본적인 웹페이지 스타일링
#### 간단한 스타일 넣는 법
```html
<p style="font-size : 20px; color : red"> 글자 </p>
```
- 거의 모든 태그는 `style=""` 이라는 속성을 열 수 있습니다.
- 거기 안에 `스타일이름 : 스타일값;` 형식으로 스타일을 넣으면 됩니다.
- 여러개를 넣고 싶다면 뒤에 쭉 나열해주시면 됩니다.
	- 세미콜론 까먹으면 안됩니다.

#### 자주 사용하는 글자 스타일들
```css
font-size : 20px;
font-family : 'gulim';
color : black;
letter-spacing : -1px;
text-align : center;
font-weight : 600;
```

#### 이미지 정렬과 폭 조정
```css
display : block;
margin-left : auto;
margin-right : auto;
width : 150px;
```

- 이미지는 width 많이 사용합니다. `px` 혹은 `%` 이런 단위로 폭을 조정가능합니다. 
	- 이때, `%` 는 부모 태그에 비례한다.
- 👉 이미지를 가운데 정렬하고 싶으면 `display : block; margin-left : auto, margin-right : auto` 를 기입해주면 됩니다. 

#### 텍스트의 일부만 스타일을 변경하고 싶을 때
```html
<p>안녕하세요 저는 <span style="color : red;">뛰어난</span> 개발자입니다.</p>
```
- `<span>` 이라는 태그로 감싼 뒤에 스타일을 주면 됩니다. 
	- `<span>` 태그?
		- 👉 가끔 글자 일부를 싸매고 싶을 때 사용하는 큰 의미없는 태그입니다. 
- 굵은 글씨 표현을 위해선 `<strong>` 태그도 사용가능하다. 


```ad-todo
- **Q. 숙제**
	- 내 프로필 페이지 만들어서 꾸며보기
	```html
	<img src="lion.png" style="display: block; margin-left: auto; margin-right: auto">
	<h3 style="text-align: center; font-size: 30px">Ramy</h3>
	<p style="text-align: center"><strong style="color: blueviolet"> Full-stack 개발자</strong>를 지향합니다.</p>
	```
```

![](assets/HTML%20&%20CSS.png)


### CSS 파일 만들고 첨부하는 법
1. 확장자가 `.css`로 끝나는 css 파일을 만든다.
2. html 문서에 해당 파일을 첨부한다.
```html
<link href="css파일경로" rel="stylesheet">
```

#### CSS 파일 내용 분리시키기
1. 적절한 css selector (css 선택자) 를 사용해 css 내용을 선언한다. 
```css
/* CSS 파일 */
.profile { 
  width : 200px;
  display : block;
  margin : auto;
}
```

2. 해당 변수를 적용할 태그에 입력해 준다 (예시는 클래스의 경우)
```html
// HTML 파일

<img src="lion.png" class="profile">
```

```ad-tip
- **Brakets 에디터 특징**
![](assets/HTML%20&%20CSS-1.png)
- 해당 css class 위에 커서를 놓고, `ctrl` + `e` 누르면 해당 내용 토글됨
```

#### CSS selector의 종류
```css
/*클래스*/
.profile { 
	font-size : 20px 
}  


/*아이디*/
#special { 
	font-size : 30px 
} 

/*태그*/
p { 
	font-size : 16px 
} 
```
- 클래스 selector는 `.클래스명{ }` 이렇게 적을 수 있고 모든 `class="클래스명"`을 가진 요소에 스타일을 적용가능합니다.
- 아이디 selector는 `#아이디명 { }` 이렇게 적을 수 있고 모든 `id="아이디명"` 속성을 가진 요소에 스타일을 적용가능합니다.
- 태그 selector는 `p { 스타일~~ }` 이렇게 적을 수 있고 `모든 <p> 태그`에 스타일을 적용가능합니다.

- 하나의 내용에 여러개의 CSS가 중복될 경우, 적용되는 스타일은 **셀렉터의 우선 순위에 따라** 결정된다.
	- 👉 `style=""` (html 문서내 직접 기입) > `#id` > `.class` > `tag` 

![CSS 적용 우선순위 (cascading order)](../KDT/Web/02.%20CSS.md#CSS%20적용%20우선순위%20(cascading%20order))

