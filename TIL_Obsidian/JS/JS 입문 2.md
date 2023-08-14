---
tag: [CodingApple/JS, JS]
---

### setTimeout 타이머주는 법

#### setTimeout
```js
setTimeout(function(){실행할 코드}, 기다릴 시간)
// 시간은 ms 단위, 1ms는 1000분의 1초

// setTimeout 함수 활용1
  setTimeout(function(){
	$('.alert').hide();
  }, 5000)
      

// setTimeout 함수 활용2
setTimeout(함수, 1000)

function 함수(){
	console.log('안녕')
}
```

#### 타이머 삭제 방법
- (참고) 타이머를 삭제하고 싶으면 <br>`var 타이머 = setInterval(어쩌구);` <br>이렇게 변수에 저장해둔 다음 타이머 삭제하고 싶을 때 <br>`clearTimeout(타이머)` 이 코드 실행하면 됩니다.
#### 페이지 방문 5초 후에 `<div>` 숨기는 방법
```html
<div class="alert alert-danger">
  5초 이내 구매시 사은품 증정
</div>

<script>
  setTimeout(function(){
    $('.alert').hide();
  }, 5000);

</script>
```
- 👉 이때, jQuery 함수 `.hide()`는 `display : none` 과 비슷하게 작동한다.

#### X초마다 코드를 실행하고 싶으면 setInterval()

```js
setInterval(function(){ 실행할코드~ }, 기다릴시간);
// 시간은 ms 단위, 1ms는 1000분의 1초

setInterval(function(){
	console.log('안녕')      
  }, 1000)
```

```ad-tip
- 웹 개발에서는 JS 문법과 Web API를 두루 알아야 한다.
	```js
	var let const if function
	```
	- 👉 JS 문법
	```html
	document.querySelector()
	
	alert()
	
	setTimeout()
	
	addEventListener()
	```
	- 👉 웹 브라우저 사용법 (Web Api)
```

#### 콜백함수관련 짧은 테크닉
- 콜백함수? 
	- 👉 함수 파라미터 자리에 들어가는 함수
- 콜백함수도 일종의 함수기 때문에 **다른 곳에서 만든 함수를 집어넣어도 잘 작동**한다
```js
setTimeout(함수, 1000);

function 함수(){ 
  console.log('안녕')
}
```


```ad-todo
- **오늘의 숙제:**

위에서 만든 `<div>`안에 "5초 이내 구매시 사은품 증정" 이라는 문자가 있습니다.

1초마다 5라는 문자를 1씩 감소시켜봅시다.

0이 되면 `<div>`를 안보이게 처리합시다.

**(힌트)** 5라는 문자만 <span>5</span> 이걸로 감싸면 html 조작하기 쉬워집니다.
```

```html
<div class="alert alert-danger"> 
	5초 이내 구매시 사은품 증정!
</div>

<script>
      timeCount = 5;

      setInterval(function(){
        if (timeCount >= 0){
          $('.alert').text(`${timeCount}초 이내 구매시 사은품 증정!`);
          timeCount -= 1;
        }
      }, 1000)
      
      setTimeout(function(){
        $('.alert').hide();
      }, 6000)

</script>
```


### 정규식으로 이메일형식 검증해보기

#### 문자 검사하는 가장 쉬운 방법 
```js
'문자'.includes('찾을단어')
```
- 아무 문자나 뒤에 `.includes()` 붙일 수 있습니다.
	- 👉그럼 문자에 찾을 단어가 들어있는지 검사해주고 있으면 true / 없으면 false 남겨줍니다.
- 하지만
	- 한글이 들어있냐
	- 영어가 들어있냐
	- A로 끝나냐
	- 마침표 다음에 영어가 있냐 
- 이런건 includes() 만으로 검사하기 어렵습니다.

#### 정규표현식 (regular expression)
```js
// "어떤 문자에 'abc'라는 단어가 들어가있냐?"
/abc/

/abc/.test('abcdef')

/정규식/.test(정규식으로 검사해볼문자)
```
- 👉 진짜 들어있으면 true를 남기고 없으면 false를 남겨줍니다.

##### 몇개만 배워보는 정규식 문법
```js
/a/.test('abcde')  //true 
// 영어나 한글의 경우 그냥 쓰면 글자가 있는지 없는지 물어볼 수 있습니다.

/[a-d]/.test('aefg')  //true
/[가-다]/.test('다라마바')  //true
// [ ] 기호를 이용해서 문자 범위를 지정할 수 있습니다.
// [a-z] 는 a부터 z까지 아무문자 하나를 의미합니다.

/[a-zA-Z]/.test('반가워요')  //false
/[a-zA-Z]/.test('반가워요a') //true
/[ㄱ-ㅎ가-힣ㅏ-ㅣ]/.test('반가워요')  //true
// [a-zA-Z] 이건 아무 알파벳 하나라는 뜻입니다. 
// [ㄱ-ㅎ가-힣ㅏ-ㅣ] 이건 아무 한글 하나라는 뜻입니다. 
```

```js
/\S/.test('abcde')   //true  
```
- 👉 백슬래시S 는 특수문자 포함 아무문자 1개라는 뜻입니다. (**특수기호 포함**)

```js
// 특정 문자로 시작하는지 여부
/^a/.test('abcde')   //true

// 특정 문자로 끝나는지 여부
/e$/.test('abcde') //true  
```
- `^a` 라고 적으면 a로 시작하는지 검사할 수 있습니다.
- `e$` 라고 적으면 e로 끝나는지 검사할 수 있습니다.

```js
// or 기호(|) 또는 소괄호 사용 가
/(e|f)/.test('abcde')   //true

// +기호는 반복되는 글자가 일치하는지 확인
/a+/
```

#### 간단히 작성해보는 이메일 정규식
```js
/\S+@\S+\.\S+/
```
- `\.` 이라는 기호는 왜 이렇게 썼냐면 마침표는 정규식에서 특수한 문법이기 때문에<br>마침표 문법을 쓰는게 아니라 **진짜 마침표를 찾아달라라는 의미로 쓰려면 백슬래시를 앞에 붙여야**합니다.

#### 참고문서
```dataview
list from #regex 
```


```ad-todo
**오늘의 숙제 :** 

폼 전송시 유저가 입력한 비번에 영어 대문자가 적어도 1개 있는지 검사해봅시다.
```


```js
[a-zA-Z0-9._+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9.]+
```

```js
      // ID & PW 검사
      document
        .querySelector("#loginBtn")
        .addEventListener("click", function (e) {
          let idInput = document.getElementById("email").value;
          let pwInput = document.getElementById("password").value;

          if (!/[a-zA-Z0-9._+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9.]+/.test(idInput)){
            alert('이메일 형식이 아님');
            e.preventDefault();
          }
          
          if (!/[A-Z]+/.test(pwInput)){
            alert('비밀번호에는 대문자가 하나 이상 포함되어야 합니다!');   e.preventDefault(); 
          }
    }
```

### 코드 3줄로 캐러셀 (이미지 슬라이드) 만들기
- 슬라이드되는 UI들을 캐러셀이라고 한다.
- 한번에 다 완성하려고 애쓰기 보다, 하나씩 완성해 나가자.
#### one-way 애니메이션 들어있는 UI 만들기
1. 시작화면 만들기
2. 최종화면 만들기
3. 원할 때 최종화면으로 변하게 JS
4. transition : all 1s; 추가

#### 1. 시작화면 만들기
```html
<div style="overflow: hidden">
    <div class="slide-container">
      <div class="slide-box">
        <img src="car1.png">
      </div>
      <div class="slide-box">
        <img src="car2.png">
      </div>
      <div class="slide-box">
        <img src="car3.png">
      </div>
    </div>
 </div> 
```

```css
.slide-container {
  width: 300vw;
  transition: all 1s;
}
.slide-box {
  width: 100vw;
  float: left;
}
.slide-box img {
  width: 100%;
} 
```
- 👉 **vw 단위**는 브라우저 폭에 비례한 단위입니다. 100vw는 브라우저 폭의 100%입니다.

#### 2. 애니메이션 종료 후 화면 만들기
```css
.slide-container {
  width: 300vw;
  transition: all 1s;
  transform: translateX(-100vw); // ← 이부분이 추가되면 된다.
} 
```


#### 3. 언제 종료화면으로 변할지 JS 코드짜기
```js
// jQuery
$('.slide-2').on('click', function() {
  $('.slide-container').css('transform', 'translateX(-100vw)');
});

// vanilla JS
  document.querySelector(".slide-2").addEventListener('click', function(){
	document.querySelector(".slide-container").style.transform = "translateX(-100vw)";
  });
```

4. step 1에 포함되서 생략
	- `<div style="overflow: hidden">`


```ad-todo
**오늘의 숙제 :** 

버튼1, 버튼3 기능도 알아서 만들어옵시다.

넘 쉬워서 예습을 원하면 다음사진보기 & 이전사진보기 버튼과 기능도 만들어보십시오.
```

```js
// 버튼1, 버튼3 기능 
	document.querySelector(".slide-2").addEventListener('click', function(){
	        document.querySelector(".slide-container").style.transform = "translateX(-100vw)";
	      });

      $(".slide-3").on('click', function(){
        $(".slide-container").css("transform", "translateX(-200vw)");
      });
      
      $(".slide-1").on('click', function(){
        $(".slide-container").css("transform", "translateX(0vw)");
      });
```

```js
// 다음사진보기 & 이전사진보기
      document.querySelector(".slide-4").addEventListener('click', function(){
        let now = document.querySelector(".slide-container").style.transform;
        
        if (now == ""){
          document.querySelector(".slide-container").style.transform = "translateX(-200vw)";
        } else if (now == "translateX(-200vw)") {
          document.querySelector(".slide-container").style.transform = "translateX(-100vw)";
      } else if (now == "translateX(-100vw)") {
          document.querySelector(".slide-container").style.transform = "translateX(0vw)";
      } else if (now == "translateX(0vw)"){
          document.querySelector(".slide-container").style.transform = "translateX(-200vw)";
      }
      });
      
      
      document.querySelector(".slide-5").addEventListener('click', function(){
        let now = document.querySelector(".slide-container").style.transform;
        
        if (now == ""){
          document.querySelector(".slide-container").style.transform = "translateX(-100vw)";
        } else if (now == "translateX(-100vw)") {
          document.querySelector(".slide-container").style.transform = "translateX(-200vw)";
      } else if (now == "translateX(-200vw)") {
          document.querySelector(".slide-container").style.transform = "translateX(0vw)";
      } else if (now == "translateX(0vw)"){
          document.querySelector(".slide-container").style.transform = "translateX(-100vw)";
      }
      });
```

```js
// 변수화
      let picture1 = "translateX(0vw)";
      let picture2 = "translateX(-100vw)";
      let picture3 = "translateX(-200vw)";
        
      document.querySelector(".slide-5").addEventListener("click", function () {
        let now = document.querySelector(".slide-container").style.transform;

        if (now == "") {
          document.querySelector(".slide-container").style.transform =
            picture2;
        } else if (now == picture2) {
          document.querySelector(".slide-container").style.transform =
            picture3;
        } else if (now == picture3) {
          document.querySelector(".slide-container").style.transform =
            picture1;
        } else if (now == picture1) {
          document.querySelector(".slide-container").style.transform =
            picture2;
        }
      });
```

### 코드 3줄로 캐러셀 (이미지 슬라이드) 만들기 2
#### 문자 중간에 변수를 집어넣고 싶으면
```js
var count = 1;
console.log('문자' + count + '문자')
console.log(`문자${count}문자`)
```


```ad-todo
- 사진이 4개(혹은 그 이상)가 되어도 잘 작동하는 다음 버튼 만들기
```

```html
<button class="next">다음</button> 

<script>
	let 지금사진 = 1;
        
      document.querySelector(".slide-5").addEventListener("click", function () {
        document.querySelector(".slide-container").style.transform = `translateX(-${지금사진}00vw`
        지금사진 += 1;
      });
</script>
```

```html
<!-- jQuery -->
<button class="next">다음</button>
<script>

  var 지금사진 = 1;

  $('.next').on('click', function(){
      $('.slide-container').css('transform', 'translateX(-' + 지금사진 + '00vw)');
      지금사진 += 1;
  })
</script>
```

### 함수의 return 문법 & 소수점 다루기
```js
function 함수(){
	return 123 
}

var 변수 = 함수();
cosole.log(변수); // 123
```
- 👉 `return` 뒤에는 수식(`1+1`), 문자열(`뽀로로라이프`) 등 다양한 것들이 올 수 있다.
- 👉 `return` 은 함수종료의 의미를 갖고 있기에, `return` 아래에 있는 코드는 실행되지 않는다. 

