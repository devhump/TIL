---
tag: [jQuery, JS]
---

#### 선택자 선택시
```js
$('.클래스명')

$('#아이디명')

$('HTML태그명')
```
#### .insertAdjacentHTML
```js
var template = '<p>안녕</p>';

// vanilla JS
document.querySelector('#test').insertAdjacentHTML('beforeend', template);

// jQuery
$('#test').append(template);
```
#### value 값 확인
```js
$('.form-select').eq(0).val();
```

#### jQuery 셀렉터 여러개 중 선택하기(querySelectorAll)
- jQuery 셀렉터로 여러 요소 찾은 뒤 하나만 고르기
```js
// vanilla JS의 경우
document.querySelectorAll('.card-body h5')[0].innerHTML

// jQuery 의 경우
$('.card-body h5').eq(0).html

$('.tab-button').eq(0).on('click', function(){
  
});
```
- jQuery에서 `$( ) 셀렉터`는 `querySelectorAll()`과 비슷하게, 해당하는 쿼리를 전부 찾아준다.
	- 👉 `$( ) 셀렉터`로 찾은 요소 중에 x번째 요소만 선택하고 싶으면 `$( ).eq(x)` 쓰면 됩니다
	- 👉 querySelectorAll() 쓰는 경우에도 `[0]` 붙여야 한다!

#### 이벤트 리스너 설정 (addEventListener)
```js
// case 1
$('.list').on('click', function(){
  
})

// case 2
$('.list').click(function(){
  
})
```

#### jQuery 에서 특정 클래스 삭제 / 추가 하는 방법
```js
// 클래스 삭제
$('.tab-button').removeClass('orange');
// 여러 클래스 한번에 삭제
$('.tab-button').removeClass('orange red purple');
  
// 클래스 추가
$('.tab-button').addClass('orange');
// 여러 클래스 한번에 추가
$('.tab-button').addClass('orange red purple');
```


#### innerHTML, innerText
```js
innerHTML
  내용설정:
  - DOM객체.innerHTML = "내용";
  - jQuery객체.html("내용");
  
  내용확인:
  - DOM객체.innerHTML;
  - jQuery객체.html();
  
innerTEXT
  내용설정:
  - DOM객체.innerTEXT = "내용";
  - jQuery객체.text("내용");

  내용확인:
  - DOM객체.innerText;
  - jQuery객체.text();
```

#### .hide()
```js
  setTimeout(function(){
    $('.alert').hide();
  }, 5000);
```
- 👉 이때, jQuery 함수 `.hide()`는 `display : none` 과 비슷하게 작동한다.

#### scroll 관련
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


#### 비교용 함수
```js
// 모달창 배경화면 클릭시 창 닫기
    $('.black-bg').on('click', function(e){
      // 지금 실제로 클릭한게 검은 배경일 때만 닫아라
      if (e.target == document.querySelector('.black-bg')){
          $(".black-bg").removeClass("show-modal");
          }
    }

// vanilla JS 
document.querySelector('.black-bg').addEventListener('click', function(e){
  if ( e.target == document.querySelector('.black-bg') ) {
    document.querySelector('.black-bg').classList.remove('show-modal');
  }
})
```
- 이때, `e.target == document.querySelector('.black-bg')` 를 `e.target == $('.black-bg')` 로 바꿔쓰면 제대로 작동하지 않음 (==jQuery 셀렉터끼리 등호비교는 불가능==)
	- 👉 `$(e.target).is($('.black-bg'))`를 사용해야함 (비교용 함수)
- 저기서 `e.currentTarget` 출력해보면 검은배경이 나오기 때문에 <br>`e.target == e.currentTarget` 또는 `e.target == this` 이렇게 써도 됨

#### jQuery에서 transform : scale 넣는 법
```js
var z = (-1/5000) * 높이 + 565/500; 
$('.card-box').eq(0).css('transform', `scale( ${z} )`);
```