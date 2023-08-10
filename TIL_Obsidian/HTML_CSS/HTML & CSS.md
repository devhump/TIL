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


### 웹레이아웃의 기초 : div를 이용한 네모네모 박스 디자인

#### 네모 박스 디자인에 많이 사용하는 CSS 속성

```css
.box {
  margin: 20px;
  padding: 30px;
  background-color: burlywood;
  width: 500px;
  height: 350px;
  border-radius: 15px;
  border: 1px solid black;
  margin-left: auto;
  margin-right: auto;
  color: white;
  text-align: center;
}
```

| 속성명        | 효과                                  |
| ------------- | ------------------------------------- |
| margin        | 바깥 여백                             |
| padding       | 안쪽 여백                             |
| border        | 테두리 (차례로 두께, 선의 종류, 색상) |
| border-radius | 테두리 둥글게 처리                    |

- `<div>` 영역을 가운데 정렬하기 위해서 `display : block; margin-left : auto; margin-right : auto` 를 사용 하면 된다.
	-  이때, `<div>` 태그는 자체적으로 `display : block` 속성을 가지고 있으므로 생략할 수 있다.  

```ad-tip
- 모든 스타일 및 속성을 외울 수는 없다. 주로 사용하는 내용들 위주로 익혀두고, 나머지는 필요할 때 찾아가며 공부하면 된다!
```


#### margin과 padding을 원하는 방향에만 줄 수 있습니다.
```css
.box {
  margin-top : 20px;
  padding-left : 30px; 
}
```
- 옵션으로 `top, left, bottom, right` 이 있고, **지정하지 않을 경우 사방면에 모두 적용**된다.
-  margin은 음수도 가능하다. 예) -20px
- `margin : 5px 6px 7px 8px;` 와 같이 띄어쓰기를 이용해 ***상 우 하 좌*** 순 (위에서 부터 시계방향) 으로 한번에 적용이 가능하다. 

#### display : block이 내장되어있는 div박스
```css
.box {
  display : block;
}
```
- `div, p, h1, li` 등의 태그는 `display : block` 속성을 주지 않아도 기본적으로 내장되어 있다.
	- 👉 그래서 `p태그나 div태그`를 그냥 사용하면 **한 행을 전부 차지**하게 됩니다.
- 참고로 display 속성에서는 `display : inline, inline-block, flex` 등이 있고, 상황에 따라 해당 속성을 부여할 수 있다. 

#### 스타일의 상속 
```html
<div>
	<p> Hello, world ! <p>
</div>
```

- 위 코드에서 `<div>` 태그(부모태그)에 스타일을 지정해도, `<p>` 태그(자식 태그)에 상속(inherit)이 되는 경우가 있다.
- 상속되는 속성의 예시로는 `font-size, color, font-family, text-align` 등이 있다.

![CSS 상속](../KDT/Web/02.%20CSS.md#CSS%20상속)


```ad-todo
- 오늘 만든 박스에 우측하단 그림자를 넣어보십시오.
```

```css
.box {
  box-shadow: 15px 10px 5px grey;
}
```

```css
{
	box-shadow: offset-x | offset-y | blur-radius | spread-radius | color
}
```

| 옵션          | 효과                                                                        |
| ------------- | --------------------------------------------------------------------------- |
| offset-x      | 그림자의 수평위치를 설정합니다. <br>요소로부터 떨어진 거리를 나타냅니다.    |
| offset-y      | 그림자의 수직위치를 설정합니다. <br>요소로부터 떨어진 거리를 나타냅니다.    |
| blur-radius   | 그림자 테두리에 흐려지는 효과를 부여합니다. <br>클수록 테두리가 흐려집니다. |
| spread-radius | 그림자의 크기를 설정합니다. <br>클수록 그림자의 크기가 커집니다.            |
| color         | 그림자의 색상을 설정합니다. <br>chrome 기준으로 기본값은 black입니다.       |

![](assets/HTML%20&%20CSS-2.png)


### 레이아웃 만들기 1 : 호환성 좋은 float
#### 요소를 공중에 띄워 왼쪽/오른쪽 정렬하는 float 속성

```html
<div>
  <div class="left-box"></div>
  <div class="right-box"></div>
</div>
```

```css
.left-box {
  width : 100px; 
  height : 100px;
  float : left;
}
.right-box {
  width : 100px; 
  height : 100px;
  float : left;
}
```

- 위의 코드는 박스 두개를 만들어 각각 왼쪽으로 정렬시킵니다.
- 하지만 float를 쓰면 요소를 붕 띄우다보니 그 다음에 오는 HTML 요소들이 제자리를 찾지 못합니다.

```ad-tip
- (참고) float 속성으로 가로정렬할 땐 영상처럼 float 박스들을 싸매는 하나의 큰 div 박스를 만들고 폭을 지정해주는게 좋다. → 그래야 모바일에서 안 흘러넘침
```

![](assets/HTML%20&%20CSS-3.png)


#### float를 쓰고 나면 항상 clear 속성이 필요합니다.

![](assets/HTML%20&%20CSS-4.png)


```html
<div>
  <div class="left-box"></div>
  <div class="right-box"></div>
  <div class="footer"></div>
</div>
```

```css
.footer {
  clear : both
}
```

- `clear` 속성을 사용하면 float 다음에 오는 박스들이 제자리를 찾게 됩니다. (까먹지 말기!)
- 참고로 `float : none` 이것도 추가해주는게 나중에 생길 버그예방차원에서도 더 좋다.

#### 상대적인 크기 단위인 퍼센트 단위
```css
.box {
  width : 80%
}
```
- 이 경우 **내 부모 태그**의 width에 비해 80% 만큼 차지하게 됩니다.
	- (부모태그는 나를 감싸고 있는 태그를 뜻합니다.)