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
// 또는
console.log(함수());
```
- 👉 `return` 뒤에는 수식(`1+1`), 문자열(`뽀로로라이프`) 등 다양한 것들이 올 수 있다.
- 👉 `return` 은 함수종료의 의미를 갖고 있기에, `return` 아래에 있는 코드는 실행되지 않는다. 

- **함수 function 문법은**
	- 긴 코드 짧게 축약해서 쓸 수 있다. 
	- 파라미터도 가능하다.
	- 오늘 배울 `return`을 쓰면 함수를 쓰고나서 원하는 값을 그 자리에 반환할 수도 있습니다.

#### 자바스크립트에서 소수점 연산시 주의점
```js
console.log(1.1 + 0.3)
// 실행 결과는 1.40000000001
```
- 👉 자바스크립트를 포함한 프로그래밍 언어(컴퓨터 구조)상의 문제
- 이를 해결하기 위해서는
	1. 덧셈하기 전에 10 곱해서 덧셈하고 10으로 나누든가 
	2. 외부라이브러리 쓰든가 
	3. 오차는 무시할 정도로 작으니 그냥 반올림하든가 

#### 소수점 반올림하는 법
```js
console.log( (1.1 + 0.3).toFixed(1));
// 숫자.toFixed(반올림할 자릿수)
```
- 👉 주의! 반환값은 **숫자가 아니라 문자**이다!

#### '숫자'를 숫자로 변환하고 싶으면
```js
parseFloat('123')
parseInt('123') 
```
- 👉 각각 문자화된 실수, 정수를 숫자 실수, 정수로 바꿔준다

```ad-todo
- 오늘의 숙제 : 

- Q1. 함수에 분과 초를 차례로 파라미터로 입력하면 ms단위로 바꿔서 뱉어주는 함수를 만들어봅시다. (1초 == 1000ms 입니다)

	```js
	// (동작예시)
	console.log(함수(1,30))
	```

- 이렇게 사용하면 콘솔창에 90000이 출력되어야합니다 (90초인데 x 1000 하면 90000)

	```js
	console.log(함수(2,10))
	```

- 이렇게 사용하면 콘솔창에 130000이 출력되어야합니다 (130초인데 x 1000 하면 130000)
```

```js
function transMs(minute, seconds){
  let result = 0;
  result += ((minute * 60) * 1000);
  result += (seconds * 1000);
  return result;
}

console.log(transMs(2, 10));
```


```ad-todo
- Q2. 가격을 파라미터로 입력하면 10% 할인가를 뱉는 함수를 만들어봅시다.

	- 근데 첫 구매여부도 true/false로 둘째파라미터에 입력해서 첫 구매가 맞을 경우 추가로 1.5 달러도 할인해줘야합니다. 
	
	- 주의사항은 가격으로 10.3 이런거 넣으면 뒤에 소수점 길게 나올 수도 있으니 알아서 처리해보든가 합시다. 

 
	```js
	// (동작예시)
	
	console.log(함수(70, false))
	// 이렇게 사용하면 콘솔창에 63이 출력되어야합니다
	// (70의 10% 할인가격이고 추가할인 없음)
	
	console.log(함수(10, true))
	// 이렇게 사용하면 콘솔창에 7.5가 출력되어야합니다
	//(10의 10% 할인가격 9에 추가할인 1.5 해줌)
	```
```

```js
function salePrice(price, firstPurchase){
  price *= 0.9;
  
  if (firstPurchase) {
    price -= 1.5
  }
  
  return parseFloat(price.toFixed(1));
}

console.log(salePrice(70, false));
console.log(salePrice(10, true));
```


### 스크롤 이벤트로 만드는 재밌는 기능들

#### 문제 1. 스크롤바 100px 내리면 로고 폰트사이즈 작게 만들기
```css
.navbar {
  position : fixed;
  width : 100%;
  z-index : 5
}
.navbar-brand {
  font-size : 30px;
  transition : all 1s;
}
```

##### 스크롤 이벤트리스너 
```js
window.addEventListener('scroll', function(){
  console.log('안녕')
});
```
- 👉 여기서 `window`는 그냥 전체 페이지를 의미합니다.
	- 실은 document도 전체 페이지입니다. window가 약간 더 큰 개념인데 scroll 이벤트리스너는 관습적으로 window에 붙임

##### 스크롤 관련 유용한 기능들
```js
window.addEventListener('scroll', function(){
  console.log( window.scrollY )
});

```
- 👉 `window.scrollY` 사용하면 **현재 페이지를 얼마나 위에서 부터 스크롤했는지 px 단위**로 알려줍니다.
- `window.scrollX` 는 가로로 얼마나 스크롤했는지 알려줍니다. (가로 스크롤바가 있으면)
- `window.pageYOffset` → `window.scrollY`와 동일한 기능(구버전 호환성이 좋음)

```js
window.scrollTo(0, 100)
```
- `window.scrollTo(x, y)` 실행하면 강제로 스크롤바를 움직일 수 있습니다.
- 👉 위 코드는 위에서부터 100px 위치로 스크롤해줍니다.

```js
window.scrollBy(0, 100)
```
- `window.scrollBy(x, y)` 실행하면 현재 위치에서부터 스크롤해줍니다.
- 👉위 코드는 현재 위치에서부터 +100px 만큼 스크롤해줍니다.

```ad-tip
- 근데 원래 `.scrollTo` 실행하면 스크롤 위치가 순간이동해야되는데 bootstrap을 설치했을 경우 이상하게 천천히 이동할 수 있습니다.
- 이때, 아래 코드를 css 파일 최상단에 추가하면 해결된다.
	```css
	:root { 
		scroll-behavior : auto; 
	}
	```
```

```js
$(window).on('scroll', function(){
  $(window).scrollTop();
})

$(window).on('scroll', function(){
  $(window).scrollTop(100);
})
```
- 👉 현재 페이지 스크롤 양을 알려줍니다.
-  `$(window).scrollTop(100)` 이러면 페이지 강제이동도 해줌


#### 문제 2. 박스 끝까지 스크롤시 알림띄우기
```html
<div class="lorem" style="width: 200px; height: 100px; overflow-y: scroll">
  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae voluptas voluptatum minus praesentium fugit debitis at, laborum ipsa itaque placeat sit, excepturi eius. Nostrum perspiciatis, eligendi quae consectetur praesentium exercitationem.
</div> 
```
- 👉 회원약관(가정)인데 이 박스를 끝까지 스크롤하면 alert()을 띄우고 싶다. <br>어떻게 해야 할까?
	- **div 스크롤바 내린 양 == div 실제높이일 경우 alert 띄워주세요~**

#### div 박스의 스크롤바 내린 양은 
- 박스를 셀렉터로 찾고 `.scrollTop` 붙이면 스크롤바를 위에서 부터 얼마나 내렸는지 알려줍니다.
```js
$('.lorem').on('scroll', function(){
  var 스크롤양 = document.querySelector('.lorem').scrollTop;
  console.log(스크롤양);
});
```
- 👉 현재 페이지 스크롤양도 `.scrollTop`으로 구할 수 있습니다. html 태그 찾아서 `.scrollTop` 붙이면 됩니다.

#### div 박스 높이 구하는 법 
- 스크롤바가 생긴 박스의 경우 실제 높이같은게 궁금할 수 있습니다. (**스크롤가능한 실제높이**)
- 그럴 땐 셀렉터로 찾아서 `.scrollHeight` 붙이면 나옵니다.
```js
$('.lorem').on('scroll', function(){
  var 스크롤양 = document.querySelector('.lorem').scrollTop;
  var 화면에보이는박스높이 = document.querySelector('.lorem').clientHeight;
  var 실제높이 = document.querySelector('.lorem').scrollHeight;
  console.log(스크롤양, 실제높이);
});
```
- 👉 참고로 박스가 화면에 보이는 부분 높이는 `.clientHeight` 하면 나옵니다.


#### `scrollTop` 으로 구한 높이 != div 실제 높이
![](assets/JS%20입문%202.png)

- 👉왜냐면 스크롤바 내린 양은 진짜 스크롤바 내린 양일 뿐이라 그렇습니다.<br>거기에 박스가 보이는 높이(`.clientHeight`)는 포함안함
- **div 스크롤바 내린 양 + div가 화면에 보이는 높이 == div 실제높이일 경우 alert 띄워주세요~**

```ad-tip
- 스크롤 내린 양은 정수단위로 나오지 않고, OS 마다 부정확해서 **여유를 두고 비교**하는게 좋습니다. 

- 그래서 끝까지 스크롤했냐~ 체크하는 것 보다, 끝에서 10px 정도 남기고 스크롤했냐~ 라고 체크해봅시다. 
```



```ad-todo
**오늘의 숙제 :** 

1. 스크롤바를 100px 내리면 로고 폰트사이즈를 작게 만들어오십시오.

반대로 100px 미만으로 내리면 로고 폰트사이즈를 크게 만들어옵시다. 

2. 회원약관 박스를 거의 끝까지 스크롤하면 alert를 띄워줍시다.
```


```js
    // 스크롤 조작 (navbar 로고 폰트 사이즈)
    window.addEventListener('scroll', function(){
      let scrollMount = window.scrollY
      
      if (scrollMount >= 100){
        $('.navbar-brand').css('font-size', '20px');
      } else {
        $('.navbar-brand').css('font-size', '30px');
      }
    })
```

```js
    // 스크롤 조작 (박스 끝까지 스크롤시 알림띄우기)
    $('.lorem').on('scroll', function(){
	  // scroll 할(한) 수 있는 높이 
      let scrollMount = document.querySelector('.lorem').scrollTop;
      // 화면에 보이는 div 박스 높이
      let divBoxHeight = document.querySelector('.lorem').clientHeight;
      // div 박스 실제 높이
      let realHeight = document.querySelector('.lorem').scrollHeight;

      if ((scrollMount + divBoxHeight + 10) > realHeight){
        alert('약관에 동의하십니까?');
      }
    })
```


### 스크롤 이벤트 숙제 해설 & 페이지 스크롤 응용
#### 스크롤 다룰 때 주의점
1. 스크롤이벤트리스너 안의 코드는 1초에 60번 이상 실행됩니다. <br>그래서 스크롤 이벤트리스너는 많이 달면 성능저하가 일어나니 스크롤바 1개마다 1개만 씁시다. 
2. 스크롤이벤트리스너 안의 코드는 1초에 여러번 실행되다보니 바닥체크하는 코드도 여러번 실행될 수 있습니다. (숙제2에서 alert가 2번 뜨고 그럴 수 있다는 뜻입니다.)<br>그걸 방지하고 싶으면 구글에 검색해보는 것도 나쁘지않습니다. 변수같은걸 활용하면 됩니다. 

```js
// flag를 넣어서 한번만 실행되게끔 처리
    let flag = true;
    
    $('.lorem').on('scroll', function(){
      let scrollMount = document.querySelector('.lorem').scrollTop;
      let divBoxHeight = document.querySelector('.lorem').clientHeight;
      let realHeight = document.querySelector('.lorem').scrollHeight;

      if ((scrollMount + divBoxHeight + 10) > realHeight){
        
        if (flag) {
          alert('약관에 동의하십니까?');
          flag = false;
        };
      }
    })
```

#### jQuery에서 함수가 한번만 이벤트가 적용되게 하는 방법
```ad-note
- jQuery에서 함수가 한번만 이벤트가 적용되게 하는 방법
- 출처: https://backstreet-programmer.tistory.com/68
-
1. `.one()` 함수 사용
	```html
	<button type="button" id="oneClickTest">oneClick</button>

	<script>
	  $( "#oneClickTest" ).one( "click", function( event ) {
		  alert( "This will be displayed only once." );
	  });
	</script>
	```

2. `.on()` 함수 사용 및 `$(this).off(event)` 추가
	```html
	<button type="button" id="onClickTest">onClick</button>

	<script>
	  $( "#onClickTest" ).on( "click", function( event ) {
	  	alert( "This will be displayed only once." );
	  	$( this ).off( event );
	  });
	</script>
	```
```

#### 현재 페이지를 끝까지 스크롤했는지 체크하려면?
```js
document.querySelector('html').scrollHeight; // 현재 페이지 실제 높이
document.querySelector('html').clientHeight; //페이지 보이는 부분 높이
document.querySelector('html').scrollTop; // 현재 페이지 스크롤양, window.scrollTop; 과 동일
```
- 👉 html 전체를 확인해야 하기 때문에, `<body>` 태그 끝나기 전에 넣어주는 게 좋다. 
- `document.querySelector('html').scrollTop;` 과 `window.scrollTop;`은 동일

```ad-tip
- **(주의)**
1. 웹페이지 scrollHeight 구할 땐 브라우저마다 아주 약간의 오차가있을 수 있어서 테스트해보는게 좋습니다.

2. 웹페이지 scrollHeight 구하는 코드는 페이지 로드가 완료되고나서 실행해야 정확합니다. 그래서 <body> 끝나기 전에 적는게 좋습니다.
```

```ad-tip
- ==코드를 외우려 하지 말고, 이해하고 넘어가자 !==
1. 스크롤바 조작할 때 마다 코드실행가능하구나
2. 박스의 숨겨진 실제 높이도 구할 수 있구나 
3. 스크롤내린 양도 구할 수 있군
```

```ad-todo
(응용)

페이지 내릴 때 마다 페이지를 얼마나 읽었는지 진척도를 알려주는 UI 같은건 어떻게 만들면 될까요?

까만색의 가로로 긴 div 박스 하나 만들고 

페이지를 1% 읽으면 div 박스 길이는 1%

페이지를 50%정도 읽으면 div 박스 길이는 50% 

페이지 다 읽으면 div 박스 길이는 100% 
```

```js
    // 스크롤 진행사항 바
    window.addEventListener('scroll', function(){
      
      let scrollHeight = document.querySelector('html').scrollHeight;
      let scrollTop = document.querySelector('html').scrollTop;
      let clientHeight = document.querySelector('html').clientHeight;
      
      let progressBar = ((scrollTop+clientHeight)/scrollHeight)*100;

      document.querySelector('.scrollProgress').style.width = `${progressBar}%`;
    })
```


### 탭기능 만들며 배우는 for 반복문

#### tab 기능 디자인 요소
```html
<style>
  ul.list {
    list-style-type: none;
    margin: 0;
    padding: 0;
    border-bottom: 1px solid #ccc;
  }
  ul.list::after {
    content: '';
    display: block;
    clear: both;
  }
  .tab-button {
    display: block;
    padding: 10px 20px 10px 20px;
    float: left;
    margin-right: -1px;
    margin-bottom: -1px;
    color: grey;
    text-decoration: none;
    cursor: pointer;
  }
  .orange {
    border-top: 2px solid orange;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid white;
    border-left: 1px solid #ccc;
    color: black;
    margin-top: -2px;
  }
  .tab-content {
    display: none;
    padding: 10px;
  }
  .show {
    display: block;
  }
</style>

<div class="container mt-5">
  <ul class="list">
    <li class="tab-button">Products</li>
    <li class="tab-button orange">Information</li>
    <li class="tab-button">Shipping</li>
  </ul>
  <div class="tab-content">
    <p>상품설명입니다. Product</p>
  </div>
  <div class="tab-content show">
    <p>스펙설명입니다. Information</p>
  </div>
  <div class="tab-content">
    <p>배송정보입니다. Shipping</p>
  </div>
</div> 
```

#### 자바스크립트 파일 모듈화하는 법
- 자바스크립트 코드가 너무 길고 복잡하면 다른 파일로 뺄 수 있습니다.
- 작업폴더에다가 `어쩌구.js`  파일 만들고 거기다가 열심히 코드짠 다음에 그 코드가 필요한 html 파일에서 아래내용 추가
```html
<script src="어쩌구.js"></script>
```

#### 첫 버튼부터 기능개발해보기
- ***개발할 내용이 복잡할 경우, 잘게 나눠서 하나씩 해결하는 습관을 기르자!***

- 버튼0 누르면
	- 버튼0,1,2에 붙어있던 orange 클래스명 전부 제거하라고 코드 3줄 짜기
	- 버튼0에 orange 클래스명 부착
	- 박스0,1,2에 붙어있던 show 클래스명 전부 제거하라고 코드 3줄 짜기
- 박스0에 show 클래스명 부착

- Q. 왜 버튼0,1,2에 붙어있던 orange 클래스명 전부 제거하라고 코드 3줄이나 짬?
	- 👉 A. 무슨 버튼에 orange가 들어있을지 모르니까 <br>그냥 귀찮아서 3개 버튼에 있는거 전부 제거하라고 코드짜면 간단하니까요 

#### jQuery 셀렉터로 여러 요소 찾은 뒤 하나만 고르기
```js
$('.tab-button').eq(0).on('click', function(){
  
});
```
- jQuery에서 `$( ) 셀렉터`는 `querySelectorAll()`과 비슷하게, 해당하는 쿼리를 전부 찾아준다.
	- 👉 `$( ) 셀렉터`로 찾은 요소 중에 x번째 요소만 선택하고 싶으면 `$( ).eq(x)` 쓰면 됩니다
	- 👉 querySelectorAll() 쓰는 경우에도 `[0]` 붙여야 한다!

```ad-todo
**오늘의 숙제 :**

탭 기능 알아서 다 코드짜오면 됩니다.
```

```js
// tab 버튼 기능 구현
$('.tab-button').eq(0).on('click', function(){
  $('.tab-button').removeClass('orange');
  $('.tab-button').eq(0).addClass('orange');
  
  $('.tab-content').removeClass('show');
  $('.tab-content').eq(0).addClass('show');
})

$('.tab-button').eq(1).on('click', function(){
  $('.tab-button').removeClass('orange');
  $('.tab-button').eq(1).addClass('orange');
  
  $('.tab-content').removeClass('show');
  $('.tab-content').eq(1).addClass('show');
})

let tabBtn = $('.tab-button');
let tabContent = $('.tab-content');

tabBtn.eq(2).on('click', function(){
  tabBtn.removeClass('orange');
  tabBtn.eq(2).addClass('orange');
  
  tabContent.removeClass('show');
  tabContent.eq(2).addClass('show');
})
```

```ad-tip
- jQuery 에서 특정 클래스 삭제 / 추가 하는 방법
	```js
	  $('.tab-button').removeClass('orange');
	  $('.tab-button').addClass('orange');
	```
```

### 탭기능 만들며 배우는 for 반복문 2

#### 좋은 관습 : 반복적인 셀렉터는 변수에 넣어서 쓰기
```ad-tip
- 위 숙제에서 보면 비슷한 셀렉터가 매우 많이 등장합니다.
- 셀렉터 문법은 기본적으로 작동시간이 오래걸립니다.
	- 셀렉터 하나 쓸 때 마다 html을 쭉 읽고 찾아야해서 오래걸리는 것임 
	- html이 길고 복잡할 수록 더 오래걸립니다. 
- 👉 그래서 저게 **반복적으로 등장하면 그냥 변수에 넣어서** 쓰십시오. 
- **querySelector** 도 마찬가지입니다. 
```

```js
var 버튼 = $('.tab-button');

버튼.eq(0).on('click', function(){
  버튼.removeClass('orange');
  버튼.eq(0).addClass('orange');
  $('.tab-content').removeClass('show');
  $('.tab-content').eq(0).addClass('show');
})
```


#### 코드 복붙하고 싶으면 for 반복문 (반복실행)
```js
for (var i = 0; i < 3; i++) {
  console.log('안녕')
}

for (var i = 0; i < 3; i++) {
  console.log(i)
}
```


#### for 반복문으로 탭기능 코드 줄여보기
```js
// tab 버튼 기능 구현 (반복문)
for (let i = 0; i < 3 ; i++){
  let tabBtn = $('.tab-button');
  let tabContent = $('.tab-content');

  tabBtn.eq(i).on('click', function(){
    tabBtn.removeClass('orange');
    tabBtn.eq(i).addClass('orange');

    tabContent.removeClass('show');
    tabContent.eq(i).addClass('show');
  });
  
}
```
- 👉 이때, 반복문 조건문에 변수 선언이 `var` 이면 잘 작동되지 않는 경우가 있다. 

#### var 쓰면 안되고 let 쓰면 잘되는 이유는
```js
for (var i = 0; i < 3; i++){

  $('.tab-button').eq(i).on('click', function(){
    $('.tab-button').removeClass('orange');
    $('.tab-button').eq(i).addClass('orange');
    $('.tab-content').removeClass('show');
    $('.tab-content').eq(i).addClass('show');
  })

});
```

- 위 코드는 제대로 작동하지 않는데 <br>컴퓨터의 입장이 되어서 위 코드를 읽으면 이해가 쉽습니다.

```ad-note
0. 컴퓨터는 위에서부터 한줄한줄 코드를 해석합니다.
1. for 반복문을 발견해서 안에 있는 코드를 반복실행하려고 합니다.  
2. 이벤트리스너를 만납니다. 이벤트리스너 안의 코드는 바로 실행안됩니다. 
	- (사용자가 버튼을 클릭시 실행되는 코드이기 때문)   
	- 그래서 이벤트리스너 내의 4줄 코드는 아직 실행하지 않고 지나갑니다.  <br>그런 식으로 반복문 안의 코드를 3번 실행합니다.
3. 그리고 반복문 끝나서 var i 변수는 3이 되어있습니다. 
4. 반복문이 다 돌고난 후 한참 후에, 사용자가 버튼0을 클릭합니다. <br>그럼 컴퓨터는 이벤트리스너 안의 코드 4줄을 실행시켜야겠군요
5. 근데 i 라는 변수를 발견합니다. 

	```js
	$('.tab-button').eq(i).addClass('orange');
	$('.tab-content').eq(i).addClass('show');
	```
- 👆 컴퓨터는 변수를 발견하면 근처에서 변수를 찾아서 채우려는 습성이 있습니다.<br>그래서 주변을 살펴보니 반복문을 다 돌고난 var i라는 변수가 3이 되어있는걸 찾아냅니다. 그거 씁니다. <br>(반복문이 다 돌고난 후라서 var i라는 변수는 3이 되어 남아있습니다.)

6. 하지만 `$('.tab-button').eq(3)` 이런건 없습니다. (4번 버튼은 없잖습니까)
7. 그래서 에러를 냅니다. 
```

- 근데 let 변수를 사용하면 변수포스트잇이 for 바깥이 아니라 안쪽에 생성됩니다.

- 더 쉽게 그림으로 비교해보자면 👇

![](assets/JS%20입문%202-1.png)

- **for 안에서 var i = 0 쓰면**
	- var 변수는 범위가 function입니다.
	- var i 들어있는 포스트잇은 for 바깥에 생성됩니다. 

- **for 안에서 let i = 0 쓰면**
	- let 변수는 범위가 { } 입니다.
	- let i 들어있는 포스트잇은 for 안쪽에 3개 생성됩니다.
	- 그리고 컴퓨터는 변수가져다쓸 때 가까운거 가져다 쓰려고합니다.

```ad-caution
- 반복문이 정상적으로 작동하기 위해서는 반복문 조건문에서 변수를 선언할 때,<br> `let` 키워드를 사용해야한다!
```

#### 확장성있는 코드로 바꾸기
- "제 코드가 좋은 코드인지 모르겠어요" 라고 묻는 분들이 많은데
	1. 원하는 기능이 잘 구현되었는가
	2. 확장성좋은가
	3. 나중에 관리가 쉬울 것인가
	4. 성능문제 없는가
- 이런거 체크해보면 됩니다. 그럼 자연스럽게 좋은 코드임

```ad-todo
Q. 지금 탭이 3개면 잘 동작하지만 4개 5개가 되면 잘 동작하지 않습니다.

탭이 4개나 5개로 바뀌어도 알아서 잘 동작하는 코드가 되려면 현재 코드를 어떻게 수정하면 될까요? 
```

```js
let tabLen = $('.tab-button').length;

// tab 버튼 기능 구현 (반복문)
for (let i = 0; i < tabLen ; i++){
  let tabBtn = $('.tab-button');
  let tabContent = $('.tab-content');

  tabBtn.eq(i).on('click', function(){
    tabBtn.removeClass('orange');
    tabBtn.eq(i).addClass('orange');

    tabContent.removeClass('show');
    tabContent.eq(i).addClass('show');
  });
  
}
```


### 이벤트 버블링과 이벤트관련 함수들

> CSS z-index 속성은 위치 지정 요소와, 그 자손 또는 하위 플렉스 아이템의 Z축 순서를 지정합니다. 더 큰 z-index 값을 가진 요소가 작은 값의 요소 위를 덮습니다.
> \- [MDN - Z-index](https://developer.mozilla.org/ko/docs/Web/CSS/z-index)
