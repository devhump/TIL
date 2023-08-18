---
tag: [jQuery, JS]
---

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
```js
// vanilla JS의 경우
document.querySelectorAll('.card-body h5')[0].innerHTML

// jQuery 의 경우
$('.card-body h5').eq(0).html
```


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