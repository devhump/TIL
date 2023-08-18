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

### Array 와 Object 자료형
#### Array 자료형
- 여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다.
- 저장된 데이터의 **순서가 있음** → 인덱싱 가능
```js
var car = ['소나타', 50000, 'white'];

// 인덱싱을 통한 항목 선택 가능
console.log(car[1]);

// 특정 인덱스의 값 수정 가능 
car[1] = 60000;

console.log(car.slice(1,2)); // [50000] 출력
```

#### Object 자료형 
- 여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다.
- `key : value` 형태로 데이터 저장
- - 저장된 데이터의 **순서가 없음**
```js
var car2 = { name : '소나타', price : 50000 };

console.log(car2['name']);
console.log(car2.name);
```

- 데이터 접근 방법
```js
var car2 = { name : '소나타', price : 50000 };

car2['key값']
car2.key값

// key를 활용해 데이터 수정 가능
car2['name'] = '그랜저';
car2.price = 60000;
```


#### Array/Object 차이
- 순서개념의 유무 → `Array` 로 가능한 것
	- 가나다순 정렬
	- x번 자료부터 x번 자료까지 자르기
	- x번 자료 바꾸기
	- 맨 뒤, 맨 앞에 자료 넣기
	- 원하는 자료가 들어있나 검색

- Array의 기본 함수
```js
array자료.sort() // 가나다순 정렬되고
array자료.slice(x, y) // x번부터 y번 전까지 자를 수 있고 
array자료.push(x) // x를 맨 뒤에 입력할 수 있고
```


```ad-todo
- **오늘의 숙제** 
	```html
	<div class="container mt-3">
	  <div class="card p-3">
	    <span>상품명</span>
	    <span>가격</span>
	  </div>
	</div> 
	
	<script>
	  var car2 = { name : '소나타', price : 50000 } 
	</script>
	```
- 여기서 car2 에 저장된 소나타라는 상품명과 50000이라는 가격을 뽑아서 html에 집어넣어보십시오.

- 자바스크립트 작성해서 구현합시다. 
```

```html
  <div class="container mt-3">
    <div class="card p-3">
      <span id="productName">상품명</span>
      <span id="productPrice">가격</span>
    </div>
  </div>

  <script>
    var car2 = { name : '소나타', price : 50000 } 

    document.querySelector('#productName').innerHTML = car2['name'];
    $("#productPrice").text(`${car2['price']}`);

  </script>
```

### 약간 복잡한 Array & Object 데이터바인딩
#### 조금 더 복잡한 자료를 다뤄봅시다
```html
<div class="container mt-3">
  <div class="card p-3">
    <span class="car-title">상품명</span>
    <span>가격</span>
  </div>
</div> 

<script>
  var car2 = { name : '소나타', price : [50000, 3000, 4000] } 
  document.querySelector('.car-title').innerHTML = car2.name;
</script>
```
- 👉 object 안에 array/object 또는 array 안에 array/object 가 포함 될 수 있다. 

```ad-tip
- object 자료형 사용 방법의 특징
	```js
	var car2 = { name : '소나타', price : 50000 };
	 
	car2.name
	car2['name']
	```
	- 위와 같은 자료형에 접근하는 방법은 2가지인데, 이때 아래와 같은 방법으로 <br>사용시 **추후 변수를 활용한 코드**를 짤 수 있다.
```

#### 복잡한 데이터에서 자료꺼내려면
- 데이터의 형태가 복잡할 때는 우선 console창에 출력을 해보자

![](assets/JS%20입문%203.png)
- 👆 위와 같이 중괄호(`{}`) 로 시작하는 경우, 대부분 **object 자료형**이다.

![](assets/JS%20입문%203-1.png)
- 👆 위와 같이 중괄호(`[]`) 로 시작하는 경우, 대부분 **Array 자료형**이다.

- object/Array 자료형이 중첩된 형태일 때
	- `car2['key값'][인덱스]`
	- `car2.키값[인덱스]`
	- 와 같은 형태로 접근 할 수 있다.

```js
var car2 = { name : '소나타', price : [50000, 3000, 4000] };

car2['key값'][인덱스]
car2.키값[인덱스]

car2['price'][0];
car2.price[0]

```

#### 실제 웹서비스 개발할 땐 2개 방식이 있는데
- 그냥 누가 내 사이트로 접속하면 html 이쁘게 만들어서 보내주는걸 웹서비스라고 합니다. 
- 근데 html을 누가 완성하는지에 따라 개발방식의 차이가 있습니다. 

1. **server-side rendering**
	- 서버에서 html을 미리 완성해서 고객에게 보내줌 
![](assets/JS%20입문%203-3.png)[^자료출처: 코딩애플]

2. **client-side rendering**
	- 서버가 비어있는 html과 데이터만 보내줌 <br>👉 그리고 자바스크립트를 이용해서 고객 브라우저안에서 html을 완성
![](assets/JS%20입문%203-4.png)[^자료출처: 코딩애플]

```ad-todo
- 오늘의 숙제 :
	- list.html 만들고 하단 코드를 복사붙여넣기합니다.
	- 그럼 상품 3개를 진열할 수 있는 카드레이아웃이 나옵니다. (bootstrap 필요) 
	- products 변수안에 상품데이터도 준비되어있는데
	- 자바스크립트를 열심히 짜서 3개의 상품 제목, 가격을 html에 전부 꽂아넣어오십시오.

	```html
	<div class="card-group container">
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	</div>
	
	<script>
	  var products = [
	    { id : 0, price : 70000, title : 'Blossom Dress' },
	    { id : 1, price : 50000, title : 'Springfield Shirt' },
	    { id : 2, price : 60000, title : 'Black Monastery' }
	  ];
	</script> 
	```
```

```html
    <div class="card">
      <img src="https://via.placeholder.com/600">
      <div class="card-body">
        <h5 class="productTitle">Card title</h5>
        <p>가격 : 70000</p>
        <button class="btn btn-danger">주문하기</button>
      </div>
    </div>
```

```js
var products = [
  { id : 0, price : 70000, title : 'Blossom Dress' },
  { id : 1, price : 50000, title : 'Springfield Shirt' },
  { id : 2, price : 60000, title : 'Black Monastery' }
]; 

for (let i = 0; i < 3; i++){
  dataUpdate(i);
}

function dataUpdate(idx) {
  document.querySelectorAll('.productTitle')[idx].innerHTML = products[idx]['title'];
  document.querySelectorAll('.card-body p')[idx].innerHTML = `가격 : ${products[idx].price}`;
}
```

### 데이터바인딩 숙제 & 문자중간에 변수넣는 법
#### 저번시간 숙제는
- 첫째 상품명을 뽑는 법을 알아봅시다.
```js
var products = [
  { id : 0, price : 70000, title : 'Blossom Dress' },
  { id : 1, price : 50000, title : 'Springfield Shirt' },
  { id : 2, price : 60000, title : 'Black Monastery' }
]; 
```

```js
products = [{}, {}, {}] 
```
- Array 안에 object가 있는 형태
	- 👉 `products[0]` → 인덱스로 접근!

```js
products[0] = { id : 0, price : 70000, title : 'Blossom Dress' }
```
- object 형태
	- 👉 `products[0].price` 또는 `products[0]['price']`로 접근!


```ad-tip
- 추가 클래스 삽입 없이 셀렉터로 접근하려면?
	```html
	<div class="card">
      <img src="https://via.placeholder.com/600">
      <div class="card-body">
        <h5 class="productTitle">Card title</h5>
        <p>가격 : 70000</p>
        <button class="btn btn-danger">주문하기</button>
      </div>
    </div>
	```
- 👉 기존 클래스와 하위 태그 활용!
	```js
	document.querySelector('.card-body h5')[0].innerHTML;
	```
- `querySelector('.card-body h5')` 
	- 👉 `card-body` 클래스를 가진 요소의 자식  중에서 `<h5>` 태그를 가진 요소
```


#### 문자 중간에 변수 쉽게넣기
1. `+` 기호 활용
```js
var a = '안녕';
console.log('문자' + a + '문자');  // '문자안녕문자'출력됨
```

2. 백틱(backtick, `` ` `` ) 문법 활용
```js
var a = '안녕';
console.log(`문자 ${a} 문자`);  // '문자안녕문자'출력됨
```
- 👉 문자 중간에 엔터키 칠 수 있음


### Select 인풋 다루기
#### select 들어간 폼을 만들어봅시다
- `<select>` 는 `<input>` 이랑 똑같은데<br>사용자가 고를 수 있는 선택지를 드랍다운 메뉴로 제공하는 `<input>` 입니다. 
- 선택지는 `<option>`으로 넣으면 됩니다. 

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
</form>
```
- `<select>` 태그도 선택시 input, change 이벤트가 발생합니다.
- `<select>` 태그도 `.value`로 유저가 입력한 값을 가져올 수 있습니다.

#### 셔츠고르면 밑에 `<select>` 더 보여주기
- UI 어떻게 만든다고 했습니까
	- 👉 html css로 미리 디자인해놓고 원할 때 보여주기만 하면 됩니다

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
    <select class="form-select mt-2 form-hide">
      <option>95</option>
      <option>100</option>
    </select>
</form>
```

```css
.form-hide{
	display : none;
}
```
- `display : none` 을 포함하는 클래스 만들어서 탈부착하기
	- "유저가 셔츠선택하면 form-hide 제거해주세요~" 구현

```html
<script>
  if (유저가 선택한거 == '셔츠') {
    $('.form-select').eq(1).removeClass('form-hide');
  }
</script>
```

#### `<script>` 안에 대충 적은 코드는 페이지 로드시 1회 실행됨
```html
<script>
  var value = $('.form-select').eq(0).val();
  if (value == '셔츠') {
    $('.form-select').eq(1).removeClass('form-hide');
  }
</script>
```
- 👉 작동되지 않는이유?
	- ==페이지 로드시 1회 실행되고 다시는 실행되지 않기 때문==

```html
<script>
  $('.form-select').eq(0).on('input', function(){

    var value = $('.form-select').eq(0).val();
    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
    }

  });
</script>
```

```ad-tip
- **이벤트: change**
	- `change` 이벤트는 요소 변경이 끝나면 발생합니다.
	- 텍스트 입력 요소인 경우에는 요소 변경이 끝날 때가 아니라 포커스를 잃을 때 이벤트가 발생합니다.
- **이벤트: input**
	- input 이벤트는 사용자가 값을 수정할 때마다 발생합니다.
	- 키보드 이벤트와 달리 input 이벤트는 어떤 방법으로든 값을 변경할 때 발생합니다. 마우스를 사용하여 글자를 붙여 넣거나 음성인식 기능을 사용해 글자를 입력할 때처럼 키보드가 아닌 다른 수단을 사용하여 값을 변경시킬 때도 input 이벤트가 발생합니다.
- 참고: [이벤트: change, input, cut, copy, paste](https://ko.javascript.info/events-change-input)
```



```ad-todo
(응용)

1. 심심하면 '모자'를 선택했을 때 `<select>`를 다시 숨기는 기능도 만들어봅시다. 

2. 지금 비슷한 셀렉터들이 많은데 변수화하면 성능개선이 되겠군요

3. 이벤트리스너 안에서 e.currentTarget 아니면 this 이런거 써도 될듯요 
```

```html
  <form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
    <select class="form-select mt-2 selectHidden" id="secondSelect">
      <option>90</option>
      <option>95</option>
      <option>100</option>
    </select>
  </form>
```

```js
 // 셀렉터 변수화
	let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");
    
    formSelect.on('input', function(){
      let value = formSelect.val();
      if (value == '셔츠'){
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```

```js
    let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");
    
    formSelect.on('input', function(e){
      let value = e.currentTarget.value;
      // let value = this.value; 도 동일
      if (value == '셔츠'){
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```
- `e.currentTarget`을 쓸 경우, `e.currentTarget.value`로 사용
- `let value = this.value;`도 동일하게 작동

### Select 2 : 자바스크립트로 html 생성하는 법
1. document.createElement()
```html
<div id="test">
  
</div>

<script>
    let a = document.createElement('p');
    a.innerHTML = '안녕';
//    a.classList.add();
    document.querySelector('#test').appendChild(a);
</script>
```

2. .insertAdjacentHTML()
```html
<div id="test">
  
</div>

<script>
// vanilla JS
var template = '<p>안녕</p>';
document.querySelector('#test').insertAdjacentHTML('beforeend', template); // 안쪽 맨 밑에 추가하라

// jQuery
$('#test').append(template);
</script>
```
- 👉 속도에서는 `createElement()`가 더 빨리 동작하나, 실질적으로는 크게 의미 없음

```ad-todo
(응용)

- 바지 눌렀다가 다시 셔츠 누르면 뭔가 이상해지는 문제도 해결해보면 어떨까요.
	- 셔츠눌렀을 때 둘 째 `<select>` 안에 있는 html도 조정해줘야겠군요.
```

```html
  <form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>
    <select class="form-select mt-2 selectHidden" id="secondSelect">
    </select>
  </form>
```

```js
    // select 인풋 
    let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");

    formSelect.on('input', function() {
      let value = this.value;
      if (value == '셔츠') {

        let shirtsSize = [90, 95, 100]

        secondSelect.html("");
        for (let i = 0; i < shirtsSize.length; i++) {
          document.querySelector('#secondSelect').insertAdjacentHTML('beforeend', `<option>${shirtsSize[i]}</option>`);
        }
        secondSelect.removeClass('selectHidden');
      } else if (value == '바지') {

        let pantsSize = [28, 29, 30]

        secondSelect.html("");
        for (let i = 0; i < pantsSize.length; i++) {
          document.querySelector('#secondSelect').insertAdjacentHTML('beforeend', `<option>${pantsSize[i]}</option>`);
        }
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```
- 👉 옷 종류별 사이즈 저장 → 해당 옵션 선택시 마다 종류별 사이즈 출력