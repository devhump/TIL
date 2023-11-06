---
tag: [CodingApple/JS, JS]
---

#### 참고문서
##### KDT/ Web
``` dataview
list FROM "KDT/Web"
SORT file.name ASC
```

##### Modern JS
```dataview
list from #ModernJavaScript 
SORT file.name ASC
```
##### CodingApple/ JS
```dataview
list from #CodingApple/JS 
SORT file.name ASC
```

## JS 입문
```ad-note
- [[#동적 UI 만드는 스텝 (Alert 박스 만들기)|동적 UI 만드는 스텝 (Alert 박스 만들기)]]
- [[#자바스크립트 function 문법 사용법|자바스크립트 function 문법 사용법]]
- [[#function의 파라미터 문법|function의 파라미터 문법]]
- [[#자바스크립트 이벤트리스너|자바스크립트 이벤트리스너]]
- [[#서브메뉴 만들어보기와 classList 다루기|서브메뉴 만들어보기와 classList 다루기]]
- [[#jQuery 사용법 간단정리|jQuery 사용법 간단정리]]
- [[#모달창만들기와 간단한 애니메이션|모달창만들기와 간단한 애니메이션]]
- [[#공백검사 숙제와 else if 문법|공백검사 숙제와 else if 문법]]
- [[#input, change 이벤트와 and, or 연산자|input, change 이벤트와 and, or 연산자]]
- [[#if/else, function 실력향상 과제|if/else, function 실력향상 과제]]
- [[#변수문법과 Dark mode 버튼만들기|변수문법과 Dark mode 버튼만들기]]
- [[#변수 심화학습시간 & 저번시간 숙제|변수 심화학습시간 & 저번시간 숙제]]
- [[#변수, 사칙연산 실력향상 과제|변수, 사칙연산 실력향상 과제]]
```


#### intro
- 자바스크립트는 **"html 조작과 변경"** 을 담당하는 언어

```html
<h1 id="hello">안녕하세요</h1>

<script>
  document.getElementById('hello').innerHTML = '안녕';
</script> 
```
- 👉 _웹문서의 id="hello"인거 찾아서 그거의 내부 HTML에 '안녕' 집어넣어라_

- `.getElementById()` : 셀렉터 → html 요소를 찾기 위해 사용
- `.innerHTML / .style / .color` :  메소드(또는 함수) → html 요소의 어떤 속성을 변경할지 결정하기 위해 사용

```ad-todo
- 자바스크립트를 이용해서 글자의 크기를 바꿔보기 
	```js
	document.getElementById('hi').style.fontSize = '16px';
	```
```


### 동적 UI 만드는 스텝 (Alert 박스 만들기)

#### 기본적인 UI 법칙
1. HTML CSS 로 미리 UI 디자인을 해놓고 필요하면 평소엔 숨김
2. 버튼을 누르거나할 경우 UI를 보여달라고 자바스크립트 코드짬

#### step 1. Alert UI 디자인부터 하기
- 작업 폴더에 `main.css` 파일을 만들고, html 내 `<head>`에 링크를 걸어 첨부한다.
	- `<link href="main.css" rel="stylesheet">`

```html
<div class="alert-box">알림창임</div>
```

```css
.alert-box {
  background-color: skyblue;
  padding: 20px;
  color: white;
  border-radius: 5px;
  display: none;
} 
```
- 👉 보이게 하고 싶으면 `display: block`으로 바꾸면 된다.
	- `visibility: hidden` 도 가능

#### step 2. 버튼 누르면 Alert UI 보여주기
```html
<button onclick="자바스크립트코드"> 버튼</button>
```

- 기능 추가를 위해서는 이런 방식으로 만들 수 있는데, 결과물은 아래와 같다. 👇 

```html
<button onclick="document.getElementById('alert').style.display = 'block';">버튼</button>
```

```ad-todo
- 알림창 닫기버튼과 해당 기능 만들어 오기
	```html
	<div class="alert-box" id="alert">
	    <p>알림창임</p>
	    <button onclick="document.getElementById('alert').style.display = 'none';">닫기</button>
	</div>
	<button onclick="document.getElementById('alert').style.display = 'block';">버튼</button>
	```
```


### 자바스크립트 function 문법 사용법

#### 자바스크립트 function 문법
- 사용하는 이유
	1. 길고 복잡한 코드를 짧고 간결하게 축약해서 사용하기 위해
	2. 특정 기능을 다음에도 쓰기 위해 모듈화해놓는 문법

```js
function 자유롭게작명(){
  축약하고 싶은 긴 코드
}
```

#### Alert 여는 코드 function으로 축약해보기
```html
<button onclick="알림창열기()">알림창 여는 버튼</button>

<script>
  function 알림창열기(){
    document.getElementById('alert').style.display = 'block';
  }
</script>
```
- 👉 함수 이름 작명시에는 **1. 영어 소문자로 시작, 2. camelCase** 사용 

```ad-tip
1. 자바스크립트는 (`<script>` 부분) html 문서 하단에 위치한다.
2. `getElementById()`처럼 중간중간 대소문자가 섞여있어 오타가 나기 쉬운데, 에디터의 자동완성 기능을 적극 활용하자.
3. 브라우저의 개발자 도구로 오류 내용을 확인하며 디버깅을 하자
	- 또는 오류 내용을 구글링 하여 해결하기
```

```ad-todo
- 닫기 버튼 function 문법으로 바꿔보기
	```html
	
	<button onclick="alertClose()">닫기</button>
	<script>
		function alertClose() {
	      document.getElementById('alert').style.display = 'none'
	    }
    </script>
	```
```

### function의 파라미터 문법
#### function에 사용가능한 파라미터 문법
```js
function 알림창열기(구멍){
  document.getElementById('alert').style.display = 구멍;
}

알림창열기('안녕');
알림창열기('바보');
```

```js
function 알림창열기(구멍){
  document.getElementById('alert').style.display = 구멍;
}

알림창열기('none'); //이거 실행하면 알림창열릴듯
알림창열기('block');  //얘는 닫힐듯 
```
- 👉 함수에 파라미터를 설정하면, 함수 호출시 넣는 값에 따라 유동적으로 작동하게 만들 수 있다.

```js
function plus(a, b){ 
  a + b
}
plus(2, 5);
```
- 👉 파라미터는 2개 이상 사용 가능하며, 콤마로 구분한다.

```ad-todo
- 버튼 2개를 만들어놓고 <br>버튼1과 버튼2를 누르면 각각 다른 이름의 alert 박스가 나오도록 코드를 짜봅시다.
	- 버튼1을 누르면 '아이디를 입력하세요' 라는 alert 박스가 등장해야합니다.
	- 버튼2를 누르면 '비밀번호를 입력하세요' 라는 alert 박스가 등장해야합니다. 
```

```html
<!-- 풀이1 -->
<div class="alert-box" id="alert">
	<p id='title'>알림창임</p>
    <button onclick="알림창열기('none')">닫기</button>
</div>
<button onclick="알림창열기('block'); changeText('아이디를 입력하세요');">버튼1</button>
<button onclick="알림창열기('block'); changeText('비밀번호를 입력하세요')" >버튼2</button>
  
<script>
    
    function 알림창열기(구멍){
      document.getElementById('alert').style.display = 구멍;
    }
    
    function changeText(text){
      document.getElementById('title').innerHTML = text;
    }
    
</script>
```

```html
<!-- 풀이2 -->
<body>

  <div class="alert-box" id="alert">
    <p id='title'>알림창임</p>
    <button onclick="알림창열기('none')">닫기</button>
  </div>
  <button onclick="openWindow('아이디를 입력하세요');">버튼1</button>
  <button onclick="openWindow('비밀번호를 입력하세요');" >버튼2</button>
  
  <script>
    
    function 알림창열기(구멍){
      document.getElementById('alert').style.display = 구멍;
    }
    
    function openWindow(text) {
      document.getElementById('alert').style.display = 'block' ;
      document.getElementById('title').innerHTML = text;
    }
    
  </script>
  
</body>
```


### 자바스크립트 이벤트리스너
#### getElementsByClassName 셀렉터
```html
<p class="title1"> 테스트1 </p>
<p class="title1"> 테스트2 </p>
<script>
  document.getElementsByClassName('title1')[0].innerHTML = '안녕';
		<!-- getElementsByClassName('클래스명')[순서] -->
</script>
```
- 👉`getElementsByClassName` 셀렉터는 일치하는 class가 들어있는 **모든 html 요소를 찾아주기 때문**에 인덱스가 꼭 붙어야 한다. 
	- 이때 HTML 문서 최상단에서부터 첫번째(`[0]`) 부터 순서대로 순번이 매겨진다.
- 이밖에도 `getElementsByTagName` (태그명으로 찾아줌), `getElementsByName` (name 속성으로 찾아줌) 등이 있다. 

#### EventListener
```js
document.getElementById('어쩌구').addEventListener('click', function(){
    //실행할 코드 
});
```

```html
<div class="alert-box" id="alert">
  <p id="title">알림창임</p>
  <button id="close"> 닫기 </button>
</div>

<script>
	document.getElementById('close').addEventListener('click', function(){
      document.getElementById('alert').style.display = 'none';
    })
</script>
```

##### event
- 이벤트란?
	- 유저가 웹페이지 접속해서 클릭, 스크롤, 키보드입력, 드래그 등을 할 수 있는데 이걸 전문용어로 **이벤트**라고 부릅니다.
- 참고: [10. Event](../KDT/Web/10.%20Event.md)

- 이벤트 예시
```js
// 이러면 셀렉터로찾은요소에 마우스를 스윽 갖다대면 특정 코드를 실행해줍니다.
셀렉터로찾은요소.addEventListener('mouseover', function(){ 
  실행할코드
});

// 이러면 셀렉터로찾은요소가 스크롤되면 특정 코드를 실행해줍니다. (당연히 그 요소에 스크롤바가 있어야됨)
셀렉터로찾은요소.addEventListener('scroll', function(){ 
  실행할코드
});

// 셀렉터로찾은요소에 키보드로 글자를 입력하면 특정 코드를 실행해줍니다. (그 요소가 글자를 입력할 수 있는 input 이런거여야 합니다)
셀렉터로찾은요소.addEventListener('keydown', function(){ 
  실행할코드
});

```
- 👉 이밖에도 다양한 이벤트가 있는데, 필요할 때 찾아보자 ([MDN - Event refence](https://developer.mozilla.org/en-US/docs/Web/Events)) 

##### 콜백함수
```js
셀렉터로찾은요소.addEventListener('scroll', function(){} );
```
- 👉함수 파라미터 자리에 들어가는 함수를 전문용어로 **'콜백함수'** 라고 한다.


### 서브메뉴 만들어 보기와 classList 다루기
#### Bootstrap 사용
- [Bootstrap 홈페이지](https://getbootstrap.com/)에서 CDN 주소 확인한 후, css 주소는 `<head> 태그 안`에,  js 주소는 `<body>태그 끝나기 전`에 붙여넣으면 된다.

```html
<nav class="navbar navbar-light bg-light">
  <div class="container-fluid">
    <span class="navbar-brand">Navbar</span>
    <button class="navbar-toggler" type="button">
      <span class="navbar-toggler-icon"></span>
    </button>
  </div>
</nav>

<ul class="list-group">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
  <li class="list-group-item">A fourth item</li>
  <li class="list-group-item">And a fifth one</li>
</ul> 
```

```css
/* main.css */
.list-group {
  display : none
}
.show {
  display : block
}
```


#### 버튼 클릭시 저기에 클래스명을 추가해주세요
- class명을 원하는 요소에 추가하는 법은 
	- 👉 `셀렉터로찾은요소.classList.add('클래스명')` 이렇게 쓰면 됩니다.
- class명을 원하는 요소에서 제거하는 법은 
	- `셀렉터로찾은요소.classList.remove('클래스명')` 이렇게 쓰면 됩니다.

```js
document.getElementsByClassName('navbar-toggler')[0].addEventListener('click', function(){
  document.getElementsByClassName('list-group')[0].classList.add('show');
});
```
- 참고로 `getElementsByClassName` 의 경우, **해당하는 항목이 하나 밖에 없을지라도** ==반드시 인덱스(`[0]`)==를 붙여야 한다.

#### 버튼 한 번 더 누르면 숨기기
```js
document.getElementsByClassName('navbar-toggler')[0].addEventListener('click', function(){
  document.getElementsByClassName('list-group')[0].classList.toggle('show');
});
```
- `classList.toggle()` 쓰면
	- 클래스명이 있으면 제거하고
	- 클래스명이 없으면 붙여줍니다.

#### querySelector
```html
<div class="test1">안녕하세요</div>
<div id="test2">안녕하세요</div>

<script>
  document.querySelector('.test1').innerHTML = '안녕';
  document.querySelector('#test2').innerHTML = '안녕';
</script>
```
- querySelector() 안에는 css 셀렉터 문법을 사용가능합니다.
	- (css에서 마침표(`.`)는 class라는 뜻이고 `#`은 id라는 뜻)
- ==다만 querySelector() 는 맨 위의 한개 요소만 선택해줍니다.==

```html
<div class="test1">안녕하세요</div>
<div class="test1">안녕하세요</div>

<script>
  document.querySelectorAll('.test1')[1].innerHTML = '안녕';
  
</script>
```
- 동일한 클래스를 가진 요소가 여러개일 때, `querySelectorAll()`를 사용하면 된다.
	- 👉 이때도 인덱스(`[]`)를 통해 해당 순번의 요소를 찾는다.


### jQuery 사용법 간단정리

#### jQuery 설치
![](assets/JS%20입문.png)
- [jQuery CDN](https://releases.jquery.com/)에서 cdn 주소를 복사한다.
- 기본적으로 cdn 주소 스크립트는 html 내 `<body>` 태그 전에 작성하는게 일반적이나, 실습에서는 상단 `<head>` 내에 포함시킨다. 
	- 👉 ***해당 주소가 쓰인 지점 아래***를 기준으로 jQuery를 사용할 수 있다. 


#### jQuery 기본 사용
```html
<!-- html 변경 
  document.querySelector('.hello').innerHTML = '바보'; 과 동
-->
<p class="hello">안녕</p>

<script>
  $('.hello').html('바보'); 
</script>


<!-- css 변경 
  document.querySelector('.hello').style.color = 'red';
-->
<p class="hello">안녕</p>

<script>
  $('.hello').css('color', 'red');
</script>
```

- 👉 ==이 때 `$(.hello)` 뒤에는 꼭 `jQuery 함수` 를 사용해야 한다.==
	- html 셀렉터로 찾으면 html 함수들을 뒤에 붙여야하고, jQuery 셀렉터로 찾으면 jQuery 함수들을 뒤에 붙여야 잘됩니다. `$('어쩌구').innerHTML` 이렇게 혼합해서 사용하면 안 된다.

#### jQuery를 사용한 클래스 리스트 조작
```html
<p class="hello">안녕</p>

<script>
  $('.hello').addClass('클래스명');
  $('.hello').removeClass('클래스명');
  $('.hello').toggleClass('클래스명');
</script>
```

#### html 여러개를 바꾸려면
```html
<!-- vanilla JS의 경우 -->
<p class="hello">안녕</p>
<p class="hello">안녕</p>
<p class="hello">안녕</p>

<script>
  document.querySelectorAll('.hello')[0].innerHTML = '바보';
  document.querySelectorAll('.hello')[1].innerHTML = '바보';
  document.querySelectorAll('.hello')[2].innerHTML = '바보';
</script>


<!-- jQuery의 경우 -->
<p class="hello">안녕</p>
<p class="hello">안녕</p>
<p class="hello">안녕</p>

<script>
  $('.hello').html('바보');
</script>
```
- 위 코드에서 알 수 있듯이 코드가 상당히 축약된다. 
	- 👉 이유는 `$()`는 해당 셀렉터에 맞는 요소를 전부 찾아주기 때문이고, 따라서 인덱스 지정 없이도 **한번에 찾은 요소 ==모두를 조작==** 할 수 있다.

#### 이벤트리스너는
```html
<p class="hello">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
    어쩌구~
  });
</script>
```
- `addEventListener` 대신 `on` 쓰면 똑같습니다.
	- `on`은 `$()` 이걸로 찾은 것들에만 붙일 수 있습니다. 


#### UI 애니메이션은
```html
<p class="hello">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
    $('.hello').fadeOut();
  });
</script>
```

- 기타 애니메이션 효과들

|    메소드     |       기능        |  반대메소드  |
|:-------------:|:-----------------:|:------------:|
|    .hide()    |     사라지게      |   .show()    |
|  .fadeOut()   |  서서히 사라지게  |  .fadeIn()   |
|  .slideUp()   | 줄어들며 사라지게 | .slideDown() |
| .fadeToggle() | fade in/out 토글  |              |


```ad-todo
- 버튼하나 아무데나 만들고 버튼 누르면 모달창을 띄워오십시오.

	```html
	<style>
		.notShowing {
		  display: none;
		}
	</style>

	 <div class="black-bg notShowing" id='modal'>
        <div class="white-bg">
          <h4>로그인하세요</h4>
          <button class="btn btn-danger" id="close">닫기</button>
        </div>
    </div>

	  <button class="modal-btn">모달 버튼</button>

	<script>
      
	    $('.modal-btn').on('click', function(){
	        $('#modal').removeClass('notShowing');     
	     });
	      
	    $('#close').on('click', function(){
	        $('#modal').addClass('notShowing');       
	    })  
    </script>
	```
```

```ad-tip
- 모달창은 되도록 html 상단에 위치하도록 작성한다.
```

### 모달창만들기와 간단한 애니메이션

#### 모달창 띄우기 숙제 1. 클래스부터 만들어놓읍시다
```css
.black-bg {
  (생략)
  display : none;
}

.show-modal {
  display : block;
}
```
- 👉 css 속성을 class 화 해서 추후에 재활용할 수 있게 만들기 

#### 모달창 띄우기 숙제 2. 버튼클릭시 모달창 띄워주세요
```css
<button id="login">로그인</button>
<script>
  $('#login').on('click', function(){
    $('.black-bg').addClass('show-modal');
  });
</script>
```


#### UI 애니메이션 만드는 법
-  **one-way 일방향 애니메이션 만드는 법**
1. 시작스타일 만들고 (class로)
2. 최종스타일 만들고 (class로) 
3. 원할 때 최종스타일로 변하라고 JS 코드짭니다
4. 시작스타일에 transition 추가 

##### 1. 시작스타일 2. 최종스타일을 class로 만들어봅시다.
```css
.black-bg {
  (생략)
  visibility : hidden;
  opacity : 0;
}
.show-modal {
  visibility : visible;
  opacity : 1;
}
```
- 👉 `display : none`을 주면 애니메이션이 잘 동작하지 않기 때문에, 그거랑 비슷한 역할을 할 수 있는 `visibility : hidden` 을 사용
- opacity는 투명도 조절할 수 있는 속성입니다. 
	- 0이면 투명, 1이면 불투명, 0.5면 반투명

##### 3. 원할 때 최종스타일로 변하라고 자바스크립트 코드짬
- 앞서서 먼저 해결 

##### 4. 시작스타일에 transition 추가
```css
.black-bg {
  (생략)
  visibility : hidden;
  opacity : 0;
  transition : all 1s;
}
.show-modal {
  visibility : visible;
  opacity : 1;
}
```
- `transition`은 스타일이 변할 때 천천히 변경하라는 뜻


```ad-todo
1. 모달창이 위에서 아래로 내려오게 구현해 보기
2. 서브메뉴 천천히 열리고, 접히게 구현해 보기
```

1. 모달창이 위에서 아래로 내려오게 구현해 보기
```css
.black-bg {
  width : 100%;
  height : 0%; /* 여기를 0으로 바꾸고 */
  position : fixed;
  background : rgba(0,0,0,0.5);
  z-index : 5;
  padding: 30px;
  visibility: hidden;
  opacity: 0;
  transition: all 1s;
}

.notShowing {
  height : 100%; /* 여기를 100으로 바꿈 */
  visibility: visible;
  opacity: 1;
}
```

2. 서브메뉴 천천히 열리고, 접히게 구현해 보기

```html
  <ul class="list-group">
	<li class="list-group-item">An item</li>
	...
	<li class="list-group-item">And a fifth one</li>
  </ul>
```

```css
.list-group {
  overflow: hidden;
  visibility: hidden;
  height: 0px;
  transition: all 1s;
}

.show {
  visibility: visible;
  height: 200px;
}
```
- 👆 위와 같이 설정한 후 `<ul class="list-group">` 태그에 `'show'` 클래스를 탈부착 식으로 구현하면된다.

- alert 창 띄우기
```js
      document.querySelector('.navbar-toggler').addEventListener('click', function(){
	alert('JS 배우기')
}
```

![](assets/JS%20입문-1.png)

```ad-todo
- 전송버튼 클릭시 첫째 `<input>`에 입력된 값이 공백이면 아이디 입력하라고 알림을 띄워봅시다. 
	```js
	      document.querySelector('#loginBtn').addEventListener('click', function(){
        let value = document.getElementById('loginId').value;
        if (value === '') {
          alert('입력창이 비어있습니다!!')
        }
      })
	```
```


### 공백검사 숙제와 else if 문법
#### 전송버튼 누르면 공백체크하라던 숙제

```js
  $('form').on('submit', function(){
	실행할 코드
  })
```
- 버튼에 click 이벤트리스너 달아도 되고 `<form>`태그 찾아서 submit 이벤트리스너 달아도 됩니다. → 똑같이 동작합니다.
	- 👉 폼전송이 되면 `<form>` 태그에서 submit 이벤트도 발생하기 때문 
- 원하는 html을 태그명으로 찾고 싶으면 마침표(`.`)나 # 없이 `$('태그명')`만 적으면 됩니다.

```js
$('form').on('submit', function(){
  if ($('#email').val() == '') {
    alert('아이디 입력하쇼');
  }
});
```
- `<input>`에 입력된 값이 공백인지 확인하기 위해 `document.getElementById('email').value == ''` 를 사용했다. 
	- 👉 jQuery로 줄여써서 `$('#email').val() == ''`

```js
$('form').on('submit', function(e){
  if (document.getElementById('email').value == '') {
    e.preventDefault();
    alert('아이디 입력하쇼');
  }
});
```
- 폼이 전송되면서 새로운 페이지로 넘어가는데, 이를 방지하기 위해 `e.preventDefault();`를 쓴다. **이때, 콜백함수에 `매개변수 e`를 넘겨준다.**

#### else if 문법
```js
if (1 == 3) {
  console.log('맞아요1')
} else if (3 == 3){
  console.log('맞아요2')
}

if (1 == 3) {
  console.log('맞아요1')
} else if (3 == 3){
  console.log('맞아요2')
} else if (4 == 4){
  console.log('맞아요3')
} else {
  console.log('틀렸어요')
}
```
- 여러 조건을 한번에 검사하기 위해 `else if`를 사용할 수 있다. 
- 위에서 부터 순차적으로 조건을 검사하면서, 조건이 참일 경우 해당 코드를 실행을 하고 이후 코드는 무시된다.
- 마지막 `else`는 경우에 따라 선택적으로 사용이 가능하다. 

```ad-todo
1. 전송버튼 누를 때 아이디랑 패스워드 둘 다 공백검사하려면?
2. 전송버튼 누를 때 입력한 비번이 6자 미만이면 알림띄우기
```

1. 전송버튼 누를 때 아이디랑 패스워드 둘 다 공백검사하려면?
```js
      document.querySelector('#loginBtn').addEventListener('click', function(e){
        
        let value = document.getElementById('loginId').value;
        let value2 = document.getElementById('password').value;
        
        if (value === '' | value2 === '') {
          e.preventDefault
          alert('입력창이 비어있습니다!!')
        }
      });
```

2. 전송버튼 누를 때 입력한 비번이 6자 미만이면 알림띄우기
```js
      document.querySelector('#loginBtn').addEventListener('click', function(e){
        
        let value = document.getElementById('loginId').value;
        let value2 = document.getElementById('password').value;
        
        if (value === '' | value2 === '') {
          e.preventDefault
          alert('입력창이 비어있습니다!!')
        }
        
        if (value2.length < 6){
          e.preventDefault
          alert('비밀번호는 6자리 이상!!')  
        }
        
      });
```


### input, change 이벤트와 and, or 연산자
#### input 이벤트와 change 이벤트
```js
document.getElementById('email').addEventListener('input', function(){
  console.log('안녕')
});
```
- 👉 `<input>` 창에 입력된 값이 변경될 때 input 이벤트가 발생

```js
document.getElementById('email').addEventListener('change', function(){
  console.log('안녕')
});
```
- 👉 `<input>` 창에 입력된 값이 변경되고, 다른 곳을 클릭하면 (포커스가 전환되면) change 이벤트가 발생

#### true/false 자료
```js
if (true){
  console.log('진짜임')
}
```
- 👉 true는 참, false는 거짓을 뜻하는 자료형 (boolean 타입)
	- **타입이란?** → 자료가 무슨 형식을 가지고 있는지 구분하기 위한 용어


#### 다른지 같은지 비교하고 싶으면
```js
console.log(2 != 1)
```
- 👉 `!=` → 다름을 비교!

```js
console.log(2 == '2')  //true 나옴
console.log(2 === '2')  //false 나옴
```

| ==  | 느슨한 비교 | 자료의 타입변환을 지가 알아서 해보고 <br>동일하면 true라고 판정 |
| --- | ----------- | ----------------------------------------------------------- |
| === | 엄격한 비교 | 자료의 타입까지 동일해야 true라고 판정                      |

#### 실은 if문 안에서 true, false 역할을 하는 자료들도 있음
```js
0
''
null
undefined
NaN
```
- 👉 이런 것들은 if문 소괄호 안에서 false랑 같은 역할을 합니다. (**falsy자료들**)

```js
0제외 모든 숫자
'아무문자'
[]
{}
```
- 이런 것들은 if문 소괄호 안에서 true랑 같은 역할을 합니다. (**truthy자료들**)

#### and/or 연산자
```js
// true
if (1 == 1 && 2 == 2){
  console.log('안녕')
}

// false
if (1 == 1 && 2 == 3){
  console.log('안녕')
}
```
- `&&` 기호는 논리학의 and 역할을 해줍니다.
	- 👉 왼쪽 오른쪽이 둘 다 true면 전체를 true로 바꿔줍니다.

```js
// true || false -> true
if (1 == 1 || 2 == 3){
  console.log('안녕')
}

// false || false -> false
if (1 == 4 || 2 == 3){
  console.log('안녕')
}
```
- `||` 기호는 논리학의 or 역할을 해줍니다.
	- 👉 왼쪽 오른쪽 둘 중 true가 적어도 1개 있으면 전체를 true로 남겨줍니다.

### if/else, function 실력향상 과제
```ad-question
- Q1. 철수는 369게임을 더럽게 못합니다. 
	- 실제 369게임 말고 약간 쉽게 각색해서 
	- '3의 배수에서' 박수를 치면 되는 게임을 하고 있습니다. 

	- 근데 철수는 바보라 숫자를 하나 주었을 때 이 숫자가 3의 배수인지 아닌지 파악하기 넘나 힘든 관계로 프로그래밍으로 이 문제를 해결하려고 합니다.
	- 어떤 숫자를 함수 안에 집어넣으면 박수를 쳐야할 지 말아야할 지 판단해주는 함수를 만들려고 하는데
	- 어떻게 함수를 만들어야할까요?
```

```js
function game369(num) {
  if (num % 3 == 0){
	  console.log('박수')
  } else {
	  console.log('통과')
  }
}
```

```ad-question
- Q2. 하지만 369게임 업그레이드 버전이 등장했습니다. 
	- 369게임 업그레이드 버전은 3의 배수에서 박수를 치는건 맞지만
	- 9의 배수에서는 박수를 두번 쳐야합니다.
	- 철수는 역시나 이것도 프로그래밍으로 이 문제를 해결하려고 합니다.
	- 아까 만들었던 369게임() 함수를 어떻게 고치면 될까요?
```

```js
function game369_v2(num) {
  if (num % 9 == 0) {
	  console.log('박수x2')
  } else if (num % 3 == 0){
	  console.log('박수')
  }  else {
	  console.log('통과')
  }
}
```

```ad-tip
- 함수이름 작명시 맨 처음 단어는 숫자를 사용하시면 안됩니다.
- 페이지 내의 다른 곳에서 자바스크립트 문법 에러가 뜨는 경우 다른 코드도 실행이 제대로 되지 않습니다. 콘솔창에 에러가 없는지 한번 확인해보십시오.
```


```ad-question
- Q3. 공인중개사 시험점수를 입력하면 합격인지 알려주는 함수를 만들어봅시다.
	- 공인중개사 1차 시험은 개론, 민법 2개 과목이 있습니다.
	- 과목마다 100점 만점이지만 두 과목 합해서 120점 이상이면 합격시켜줍니다. 
	- 다만 한 과목이 40점 미만이면 과락으로 불합격됩니다.  
	- 과목 점수 2개를 파라미터로 입력하면 합격인지 불합격인지 여부를 콘솔창에 출력하는 함수를 만들어보십시오. 
```

```js
function passCheck(score1, score2){
  if (score1 < 40 || score2 < 40) {
	  console.log('불합격')
  } else if ((score1 + score2) >= 120){
	  console.log('합격')
  } else {
	  console.log('불합격')
  }
}
```

```ad-question
1. (응용) 원래의 369게임 룰을 적용하려면 어떻게 해야할까요?
	- 3의 배수에서 박수를 치는게 아니라 끝자리가 3,6,9로 끝나는 숫자라면 '박수'를 출력되게 하는겁니다. 
	- 이건 숫자의 마지막자리를 어떻게 파악할지 구글 검색해보면 쉽게 해결되니 답은 없습니다. 

2. (응용2) 합격판독기에 0에서 100사이 숫자가 아닌걸 입력하면 장난치지 말라고 alert를 띄우려면 어떻게 코드짜야할까요?
	- 이것도 간단하게 if문 알아서 추가해봅시다.
```

```js
function game369_v3(num) {

  const lastNum = String(num)
  // console.log(lastNum[lastNum.length-1])

  if (lastNum[lastNum.length-1] == '3' 
  || lastNum[lastNum.length-1] == '6' 
  || lastNum[lastNum.length-1] == '9' ){
    console.log('박수')
  } else {
    console.log('통과')
  }
}
```

```js
function passCheck(score1, score2){

  if (0 > score1 
  || score1 > 100 
  || 0 > score2 
  || score2 > 100){
	  alert('장난치지마세요')
  }
  
  if (score1 < 40 || score2 < 40) {
	  console.log('불합격')
  } else if ((score1 + score2) >= 120){
	  console.log('합격')
  } else {
	  console.log('불합격')
  }
}
```


### 변수문법과 Dark mode 버튼만들기
#### 자료를 잠깐 저장할 수 있는 변수문법
```js
// var 변수명 = 넣을값;
var 나이 = 20;
var 이름 = 'kim';
```
- 👉 **변수 작명시엔 camelCase** 사용

- 변수를 사용하는 이유? 
	1. 길고 복잡한 자료가 있으면 잠깐 변수에 저장해서 쓰면 편리합니다.
	2. 특정 값을 기록하고 싶으면 변수씁니다.

#### 변수에 +1 하는 법
```
변수명++

변수 += 1

변수 = 변수 + 1


(변수에 -1 하는 법)

변수명--

변수 -= 1

변수 = 변수 - 1

```

```ad-todo
- 다크모드 버튼 눌렀을 때 
	- 버튼 누른 횟수가 홀수면 버튼 내부 글자를 Light로 변경해주세요~
	- 버튼 누른 횟수가 짝수면 버튼 내부 글자를 Dark로 변경해주세요~
```

```js
      var count = 0;
      
      $('.badge').on('click', function(){
        count += 1;

        if (count % 2 == 0){
          $('#modeChangeBtn').text('Dark 🔄')
        } else {
          $('#modeChangeBtn').text('light 🔄')
        }
      })
      
//     뱃지 클릭 횟수가 홀수면 내부 글자를 light로 변경 
//     뱃지 클릭 횟수가 짝수면 내부 글자를 Dark로 변경
```
- 👉 `$('#modeChangeBtn').html('Dark 🔄')` 사용해도 됨

### 변수 심화학습시간 & 저번시간 숙제

```html
<body class='DarkMode'>
...
</body>
```

```css
.DarkMode{
	background : black;
	color : white;
	...
}
```

- 페이지에 다크모드를 적용하고 싶다면, `DarkMode`라는 클래스를 만들고, 탈부착식으로 작동하게 하면 된다. 
	- Bootstrap 스타일이 적용된 요소는 css 덮어쓰기가 어려울 수 있습니다.<br>bg-dark 클래스명을 bg-light 이런 식으로 바꾸거나 <br>아니면 붙어있던 class를 제거하거나 그러면 됩니다.

#### 변수의 선언, 할당, 범위라는 개념
```js
// 변수의 선언
var 나이; 
var 이름;

// 변수의 할당
나이 = 20;
이름 = 'kim';

// 변수의 선언과 할당
var 나이 = 20;
var 이름 = 'kim';
```
- 저렇게 선언만 따로, 할당만 따로 할 수 있습니다. 
	- 선언만 한 변수를 출력하면 `undefined(정의되지 않음)` 라고 출력됨
- 이미 있는 변수를 재선언도 가능합니다.
- 이미 들어있는 값을 등호로 재할당도 가능합니다.

```js
function 함수(){
  var 나이 = 20;
  console.log(나이); //가능
}

console.log(나이); //불가능
```
- 변수는 사용가능한 범위가 있습니다.
	- **함수 안에서 변수를 만들었을 경우 함수 안에서만 사용가능**합니다.<br>**밖에선 사용불가능**합니다. 밖에서 출력하면 변수가 정의 안 되었다고 에러남.
	- 반대로 함수 바깥에서 만든 변수는 함수 안에서는 사용가능합니다.

#### var let const 문법 전부 변수생성 가능
```js
let 거주지 = 'seoul';
const 가격 = 3000;

//let, const는 재선언 불가능합니다. 재선언하면 에러를 내줍니다.  
let 거주지 = 'seoul';
let 거주지; //에러내줌

// const는 재할당도 불가능합니다. 재할당하면 에러를 내줍니다.
const 가격 = 3000;
가격 = 4000;  //에러내줌
```
- 👉 **let과 const 사용의 장점**
	- **let** → 코드가 방대해 지면, 나중에 변수만든거 또 만들고 그런 실수가 있습니다. 이걸 미연해 방지해 줍니다.
	- **const** → 값을 수정하면 큰일나는 변수들을 만들고싶을 때 유용합니다. 나중에 값을 변경하는 실수를 방지하고 싶을 때 쓰면 됩니다.

```js
if (true) {
  let 이름 = 'kim';
}

console.log(이름); //없다고 나옴
```
- let과 const는 범위가 더 좁습니다. 모든 중괄호가 범위입니다.
	- if, function, 나중에 배울 for 반복문 이런 것은 중괄호가 있습니다.
	- 중괄호 안에서 만든 let const 변수의 경우 중괄호를 벗어나면 없다고 나옵니다. 

| 키워드 | 범위            | 재선언   | 재할당   |
| ------ | --------------- | -------- | -------- |
| var    | Function-scoped | 재선언 O | 재할당 O |
| let    | {Block-scoped} | 재선언 X | 재할당 O |
| const    | {Block-scoped} | 재선언 X | 재할당 X |

- 참고
	- [1. 변수와 식별자](../KDT/Web/09.%20ECMA%20Script.md#1.%20변수와%20식별자)

### 변수, 사칙연산 실력향상 과제
```ad-question
- Q1. 변수를 만들어봅시다
	- 내 나이와 출신지역을 자바스크립트 변수에 저장해봅시다. 
	- 나이는 맨날 변하니 재할당가능한 변수,
	- 출신지역은 바뀌지 않으니 재할당불가능한 변수에 저장해보십시오.
```

```js
let age = 31;
const birthRegion = 'Ulsan';
```

```ad-question
- Q2. 왜 이 변수는 동작하지 않죠?
	```js
	var name = 'park';
	var id = 0;
	
	function showName(){
	  var name = 'kim';
	  var id = 1;
	  console.log(name);
	}
	
	showName();
	console.log(id);
	```
- 다음 코드를 실행했을 때 콘솔창에 무엇이 출력될까요?
```

```
kim
0
```

```ad-question
- Q3. 이자율 계산하기 
	- 철수는 은행에 예금을 하러 갔는데 예금 금액에 따라 이율이 달라지는 것을 보고 크게 당황했습니다.
	- 첫 예금액이 5만원 미만이면 이율이 연 15퍼센트,
	- 첫 예금액이 5만원 이상이면 이율이 연 20퍼센트라고 합니다.

	- 그래서 민준이는
	- (1) 변수에 예금액을 넣으면
	- (2) 2년 후의 총 예금액을 자동으로 콘솔창에 출력해주는 기능을 자바스크립트로 만들려고하는데

- 어떻게 코드를 짜면 될까요? 
```

```js
var deposit = 60000;
var futureMoney = 0;

function bankRate(deposit) {
	if ( deposit < 50000 ){
		deposit *= 1.15
		deposit *= 1.15
		}
	else {
		deposit *= 1.20
		deposit *= 1.20
		}
	futureMoney = deposit
}
 
console.log(futureMoney) 
```

```ad-question
- Q4. 커피 리필을 이상하게 해주는 곳이 있습니다. 최대한 마실 수 있는 커피양을 계산해봅시다. 
	- 방금 마신 커피의 3분의 2만큼 총 2번 리필해주는 카페가 있습니다.
	- 예를 들면 처음 커피를 90ml 주문하면 첫 리필은 60ml를 해주며, 그 다음 리필은 40ml를 해주는 카페입니다.
	- 그럼 처음 주문한 커피 양에 따라서 최대한 마실 수 있는 커피를 콘솔창에 계산해주는 코드를 작성해봅시다. 
```

```js
var first = 360;

function refill(first) {
	first = first + (first * 2/3) + ((first * 2/3) * 2/3)
	console.log(first)
}

refill(first)
```

```ad-question
- Q5. 간단한 퀴즈 UI를 만들어봅시다.
	```html
	<p>태조 이성계가 태어난 년도는?</p>
	<input type="text" id="answer">
	<button id="send-answer">제출</button>
	
	<script>
	  여기에 기능 알아서 만드십시오
	</script>
	```
	
- 유저가 `<input>`에 답을 적고 제출버튼을 누를 수 있는 퀴즈 UI 입니다.
1. 유저가 답을 맞추면 alert('성공');
2. 유저가 답을 3번 찍어서 못맞추면 alert('멍청아') 를 띄워봅시다.
하단에 자바스크립트 작성하면 됩니다.
(위 문제의 답은 1335입니다)
```

```html

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>

<p>태조 이성계가 태어난 년도는?</p>
<input type="text" id="answer">
<button id="send-answer">제출</button>

<script>
  
  count = 0;
  
  $('#send-answer').on('click', function(){
    let answer = $('#answer').val();
    //console.log(answer)
    count += 1;
      
    if (answer == 1335){
      alert('성공')
      count = 0;
    }
    
    if (count >= 3){
      alert('멍청아')
    }
  })
</script>
```

```ad-question
- (응용 1)
	- 위에서 1.2를 여러번 곱했는데 1.2를 10번 곱하려면 코드를 어떻게 짜야될까요? 
	- `1.2 * 1.2 * 1.2 ...` 계속 하면 되긴 하는데
	- 자바스크립트엔 ** 이런 거듭제곱 연산자 기능도 있습니다.

- (응용 2)
	- 커피리필 문제에서
	- 커피리필을 무한으로 해준다면 처음 담아주는 커피가 360ml일 때 총 몇 ml의 커피를 마실 수 있을까요?
	- 무한등비수열의 합 그런건데 공식이 가물가물해서 여기까지 하겠습니다.
```

