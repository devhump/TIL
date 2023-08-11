---
tag: [CodingApple/JS, JS]
---

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
셀렉터로찾은요소.addEventListener('mouseover', function(){ 
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
- 👉함수 파라미터자리에 들어가는 함수를 전문용어로 **'콜백함수'** 라고 한다.


### 서브메뉴 만들어보기와 classList 다루기
#### Bootstrap 사용
- Bootstrap 홈페이지에서 CDN 주소 확인한 후, css 주소는 `<head> 태그 안`에,  js 주소는 `<body>태그 끝나기 전`에 붙여넣으면 된다.

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
- lass명을 원하는 요소에서 제거하는 법은 
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
	- 👉 이유는 `$()`는 해당 셀렉터에 맞는 요소를 전부 찾아주기 때문이고, 따라서 인덱스 지정 없이도 **한번에 찾은 요소를 조작**할 수 있다.

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

| 메소드     | 기능              | 반대메소드  |
| ---------- | ----------------- | ----------- |
| .hide()    | 사라지게          | show()      |
| .fadeOut() | 서서히 사라지게   | fadeIn()    |
| .slideUp() | 줄어들며 사라지게 | slideDown() |
| fadeToggle() | fade in/out 토글 |             |


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

```js
      document.querySelector('.navbar-toggler').addEventListener('click', function(){
        
   기
```js
alert('어쩌구')
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
- 원하는 html을 태그명으로 찾고 싶으면 마침표나 # 없이 `$('태그명')`만 적으면 됩니다.

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
- 폼이 전송되면서 새로운 페이지로 넘어가는데, 이를 방지하기 위해 `e.preventDefault();`를 쓴다. 이때, 콜백함수에 `매개변수 e`를 넘겨준다.

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