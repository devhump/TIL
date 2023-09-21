---
title : MDN_HTML 
aliases : []
tags : [web, MDN]
---

### CSS 기초
- Cascading Style Sheets
- 웹페이지를 꾸미려고 작성하는 코드.
- 웹 개발시 주의 사항 (파일/폴더 이름 명명)

```ad-note
1. 모든 문자는 소문자로 작성할 것 
2. 폴더 & 파일 이름에 공백을 주지 말 것
3. 하이픈을 사용할 것 ues `-` not `_` (underscore)
	- 구글 검색 엔진에서 `_`는 문자 띄어쓰기로 인식하지 않음
    
```

```css
/* style.css 파일 내용 */

p {
  color: red;
}
```

```html
<!-- 아래 문장을 head 사이에 끼워둠-->

<link href="styles/style.css" rel="stylesheet" type="text/css">
```



### CSS 내부 요소
- 전체 구조는 rule set 또는 rule 이라고 표현
- **선택자(selector)**
	- rule set의 맨 앞에 있는 HTML 요소 이름. 
	- 이것은 꾸밀 요소(들)을 선택합니다. (위 예에서는 `p` 요소)

- **선언**
	- `color: red`와 같은 단일 규칙. 여러분이 꾸미기 원하는 요소의 속성을 명시
- **속성(property)**
	- 주어진 HTML 요소를 꾸밀 수 있는 방법입니다. (위 예에서, `color`는 p 요소의 속성입니다.)
- **속성 값**
	- 속성의 오른쪽에, 콜론 뒤에, 주어진 속성을 위한 많은 가능한 결과중 하나를 선택하기 위해 속성 값을 갖습니다.

- rule set 작성 요령
	- 각각의 rule set (셀렉터로 구분) 은 반드시 (`{}`) 로 감싸져야 합니다.
	- 각각의 선언 안에, 각 속성을 해당 값과 구분하기 위해 콜론 (:)을 사용해야만 합니다.
	- 각각의 rule set 안에, 각 선언을 그 다음 선언으로부터 구분하기 위해 세미콜론 (;)을 사용해야만 합니다.

```css
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}

/* 콤마로(,) 여러 선택자 선택 가능 */
p,li,h1 {
  color: red;
}
```


| 선택자 이름                                       | 선택하는 것                                                  | 예시                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 요소 선택자 (때때로 태그 또는 타입 선택자라 불림) | 특정 타입의 모든 HTML 요소.                                  | `p` `<p> 를 선택`                                            |
| 아이디 선택자                                     | 특정 아이디를 가진 페이지의 요소 (주어진 HTML 페이지에서, 아이디당 딱 하나의 요소만 허용됩니다). | `#my-id` `<p id="my-id">` 또는 `<a id="my-id">` 를 선택      |
| 클래스 선택자                                     | 특정 클래스를 가진 페이지의 요소 (한 페이지에 클래스가 여러번 나타날 수 있습니다). | `.my-class` `<p class="my-class">` 와 `<a class="my-class">` 를 선택 |
| 속성 선택자                                       | 특정 속성을 갖는 페이지의 요소.                              | `img[src]` `<img src="myimage.png">` 를 선택하지만 `<img> `는 선택 안함 |
| 수도(Pseudo) 클래스 선택자                        | 특정 요소이지만 특정 상태에 있을 때만, 예를 들면, hover over 상태일 때. | `a:hover` `<a>` 를 선택하지만, 마우스 포인터가 링크위에 있을 때만 선택함 |


```css
html {
  font-size: 10px; /* px 은 'pixels' 를 의미합니다: 기본 글자 크기는 현재 10 pixels 높이입니다. */
  font-family: placeholder: 구글 폰트로부터 여러분이 얻은 마지막 결과가 있어야합니다.
}

h1 {
  font-size: 60px;
  text-align: center; /* 가운데 정렬  */
}

p, li {
  font-size: 16px;
  line-height: 2; /* 줄의 높이 */
  letter-spacing: 1px; /* 자간 설정 */
}

```

- `padding` : 컨텐트 주위의 공간 (예, 문단 글자의 주위)
- `border`: padding 의 바깥쪽에 놓인 실선
- `margin`: 요소의 바깥쪽을 둘러싼 공간
- `width`: (한 요소의 너비)
- `background-color`: 요소의 콘텐츠와 padding 의 배경 색
- `color`: 한 요소의 콘텐츠 색 (일반적으로 글자색)
- `text-shadow`: 한 요소 안의 글자에 그림자를 적용
- `display`: 요소의 표시 형식을 설정합니다 (이것에 대해선 아직 걱정하지마세요)

- 페이지 색 바꾸기
  ```css
    html {
      background-color: #00539F;
    }
    ```

- 예시코드
  ```css
  body {
    width: 600px; /* 너비 고정 */
    margin: 0 auto; /* 첫번째 요소는 상하단, 두번째는 좌우. auto는 좌우 같게*/
    background-color: #FF9500; /* 배경색 설정 */
    padding: 0 20px 20px 20px; /* 상단 우측 하단 좌측 (12시부터 시계방향)*/
    border: 5px solid black; /* 경계 표시 */
  }
  ```

  ```css
  /* 세로방향 | 가로방향 */
  margin: 5% auto; /**/
  
  /* 위 | 가로방향 | 아래 */
  margin: 1em auto 2em;
  
  /* 위 | 오른쪽 | 아래 | 왼쪽 */
  margin: 2px 1em 0 auto;
  ```

- `<length>` 여백의 크기로 고정값 사용.
- `<em>, <rem>` : px, pt 와 달리 상대적인 단위로 쓰임. 
	- `em`은 요소의 font-size 값에, `rem`은 root 즉, html 요소의 font-size 값에 영향을 받음
- `<percentage>`여백의 크기로 [컨테이닝 블록](https://developer.mozilla.org/ko/docs/Web/CSS/Containing_block) 너비의 백분율 사용.
- `<auto>` 브라우저가 적절한 여백 크기를 선택. 예를 들어 요소를 중앙 정렬하고 싶을 때 사용할 수 있습니다.


---
- [출처: CSS 기초 (MWD)](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [(MWD) CSS-margin 자세한 설명](https://developer.mozilla.org/ko/docs/Web/CSS/margin#values)