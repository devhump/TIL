---
tag: [jQuery, JS]
---

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
