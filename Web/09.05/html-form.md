## HTML - form 추가 내용 정리

```html

<form action="/my-handling-form-page" method="post">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" />
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" />
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg"></textarea>
    </div>

    <div class="button">
        <button type="submit">Send your message</button>
    </div>
</form>
```

- `action`과 `method`는 필수
- label은 선택(클릭 or 터치) 부위를 넓게 만들어줌
- `<textarea>`는 여러 줄의 텍스트를 입력 받을 수 있음 (다른 input 요소는 한 줄) -> 반드시 받는 태그 필요 `</textarea>`



```html
 <form>
 <!-- 두가지 텍스트 타입의 기본값 설정 -->    
    <input type="text" value="by default this element is filled with this text" />
     
    <textarea>by default this element is filled with this text</textarea>
  </form>
```



<button> 의 3가지 종류

- `submit` : 버튼을 클릭하면 폼 데이터를 form 요소의 action속성에 정의된 웹페이지 에 전송된다.

- `reset` : 버튼을 클릭하면 모든 폼 위젯을 기본 값으로 바꾼다. (UX 관점에서 좋은 방법은 아님)
- `button` : 그 자체로는 아무런 역할을 하지 않는다. 단, JS 를 사용해서 기능을 구현해서 쓸 수 있다. 

  ***<input>요소는 오직 일반 텍스트만 보내는 반면 <button>요소는 전체 HTML 콘텐츠를 보낸다***



form 에 CSS 적용하기

```css
/* 기본 설정*/
form {
    /* Just to center the form on the page */
    margin: 0 auto;
    width: 400px;
    /* To see the outline of the form */
    padding: 1em;
    border: 1px solid #CCC;
    border-radius: 1em;
}

/* 각각 폼 위젯사이에 여백을 추가 */
form div + div {
    margin-top: 1em;
}


label {
    /* To make sure that all label have the same size and are properly align */
    display: inline-block;
    width: 90px;
    text-align: right;
}

/* 활성화된 위젯 하이라이팅 */
input:focus, textarea:focus {
    /* To give a little highlight on active elements */
    border-color: #000;
}


```

