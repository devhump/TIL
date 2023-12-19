### 글 작성기능 만들기 1 (POST 요청)

- 글쓰기 기능을 만들어볼건데<br>알아서 한번 코드 짜보시면 되겠습니다. 

- 안배운건데 코드를 어떻게 짜냐고요?<br>첨보는 기능하나 만들라고 했을 때 어떻게 해야되냐면 
	1. 기능이 어떻게 동작하는지 한글로 상세히 정리부터 하고
	2. 그걸 코드로 번역하기  
- 이렇게 하면 처음보는 기능도 알아서 잘 만들 수 있습니다. <br>숙련된 프로그래머들도 다들 이렇게 합니다. 

%%자바스크립트 기초강의에서 맨날 연습하던 것임%%

#### 글작성 기능이 어떻게 동작하는지 정리부터
- 글작성 기능은<br>유저가 작성한 글을 DB에 저장하면 그게 글쓰기 기능 끝아니겠습니까<br>이렇게 써놓고 그대로 코드로 번역만 하면 될거같은데 <br>이렇게 코드짜면 금방 서비스 종료한다고 했습니다. 

- 유저가 DB와 직접 통신하게 냅두면 유저가 DB에 이상한 짓을 할 수도 있기 때문에<br>DB조작이 필요한 경우는 **중간에 서버를 거치는 식으로** 코드짜는게 좋습니다 
	1. **유저가 글작성페이지에서 글을 작성해서 서버로 글을 보내고** 
	2. **서버는 글을 받으면 잘썼나 확인해보고** 
	3. **서버는 그걸 DB에 저장**
- 이러면 될거같습니다 

- 그럼 이거 그대로 코드로 번역만 하면 구현 끝입니다.<br>그리고 모르는 내용이 나오면 구글 검색하면 되는 것임

#### write.ejs 글작성 페이지 만들기
- 1번기능을 만들어볼건데 그러기 위해서 유저가 글을 작성할 수 있는 html 페이지부터 만들어봅시다.<br>ejs파일로 하나 만들면 좋을거같아서 write.ejs 파일 하나 만들었고 <br>안에 글작성할 수 있는 폼을 만들면 되겠군요. 

##### write.ejs 레이아웃
```html
<form class="form-box">
    <h4>글쓰기</h4>
    <input>
    <input>
    <button type="submit">전송</button>
</form> 
```

```css
input,div {
  box-sizing: border-box;
}
.form-box {
  background : white;
  padding : 25px;
  margin: 20px;
  border-radius: 8px;
}
.form-box input {
  padding : 10px;
  font-size: 16px;
  width: 100%;
  border: 1px solid black;
  border-radius: 5px;
  margin-bottom: 10px;
}
.form-box button {
  padding: 10px;
  border : none;
  background : lightgrey;
  border-radius: 5px;
}
```

- 잠깐 설명하자면
	- 웹페이지에서 뭔가 작성할 수 있는 인풋을 만들고 싶으면 `<form>` 안에 `<input>` 을 쓰면 됩니다 
	- `<input type=" ">` type속성 안에 다양한걸 집어넣어서 다양한 인풋을 만들 수 있음  
	- 전송 버튼은 `type="submit"` 속성을 넣은 `<button>` 만들면 됩니다. 

#### 버튼누르면 서버로 글 전송하기
- 그럼 서버로 작성한 글을 전송하면 되는데<br>어떻게 전송하냐면 POST요청을 사용하면 쉽게 전송이 가능합니다. 

- 서버에 뭔가 요청하려면 정확히 URL과 method를 기입하랬습니다. <br>그래서 실은 `<form>`태그에도 URL과 method 기입란이 있는데 

```html
(write.ejs 중)

<form action="/어쩌구" method="POST">
```

- action 속성열어서 /url 채우고 <br>method 속성을 열어서 POST라고 채우면 <br>이제 폼태그안에있던 전송버튼누르면 /어쩌구 URL로 POST요청이 갑니다.<br>편리하죠?

```html
(write.ejs 중)

<form class="form-box" action="/add" method="POST">
   <h4>글쓰기</h4>
    <input name="title">
    <input name="content">
    <button type="submit">전송</button>
</form> 
```

- 근데 이렇게만 하면 `<input>`안에 유저가 적은 내용은 서버로 전달이 되지 않습니다.<br>서버로 전달하고 싶으면 `<input>`에다가 전부 `name=" "` 속성을 열어서 아무거나 영어로 작명해주면 됩니다. 

- 이제 여기다가 서버에 만들어둔 /url과 method 채우면 되는데 <br>아직 서버기능 개발 안했으니까 <br>아무거나 채워넣고 서버에서 이거 그대로 기능을 만들어두면 되겠군요.

- 저는 URL을 /add로 작명해봤습니다.<br>서버에서 이제 /add 로 POST요청 받는 코드 작성하면 되겠군요. 

#### 서버는 글 받으면 잘보냈나 검사해보기 
- 이제 이거 2번기능 구현하면 될 것 같습니다. 
- 그 전에 셋팅이 하나 필요한데<br>유저가 보낸 정보를 서버에서 쉽게 출력해보고 싶으면

```js
app.use(express.json())
app.use(express.urlencoded({extended:true})) 
```

- 서버파일 상단 쯤에 이런거 추가합시다. <br>원래 유저가 데이터를 보내면 그걸 꺼내쓰는 코드가 좀 귀찮게 되어있는데<br>그걸 `요청.body`로 쉽게 꺼내쓸 수 있게 도와주는 코드입니다. 

![](Node.js%20&%20MongoDB%202-2.png)

- 일단 유저가 /add로 POST요청하면서 글을 보내고 있기 때문에<br>누가 POST요청시 뭔가 코드를 실행해주고 싶으면

```js
app.post('/add', (요청, 응답)=>{
  console.log(요청.body)
  실행할코드~
}) 
```

- 이거 써놓고 시작하면 됩니다.<br>누가 /add로 POST요청시 안에있는 코드 실행하라는 뜻입니다. 

- 그리고 중요한게 있는데 여기 안에서 `요청.body`라고 쓰면 유저가 `<input>`으로 보낸 데이터를 출력해볼 수 있습니다. <br>그래서 요청.body 출력 잘 되는지 진짜로 글작성하고 전송버튼 눌러서 POST요청 날려봅시다. 

- 유저가 보낸 글을 DB에 저장하는 3번 기능은 알아서 숙제로 구현해오시면 되겠습니다. 

```ad-todo
오늘의 숙제 : 
유저가 /add로 POST요청하면 작성한 제목과 내용이 서버로 전달되고 있습니다.  
그 제목과 내용을 DB에 저장해봅시다. 
안배운걸 내가 어떻게하냐고요?
안배운건 당연히 'mongodb 데이터 저장하는법' 이런거 검색해봐야지 생각한다고 나오는게 아닙니다. 
```

```js
app.post("/add", (요청, 응답) => {
  db.collection("post").insertOne({
    title: `${요청.body["title"]}`,
    content: `${요청.body["content"]}`,
  });
  console.log("저장완료");
});
```


### 글 작성기능 만들기 2 (insertOne, 예외 처리)
```js
app.post("/add", async (요청, 응답) => {
  console.log(요청.body);
  await db
    .collection("post")
    .insertOne({ title: 요청.body.title, content: 요청.body.content });
  응답.redirect("/list");
});
```

- 저번시간에 글작성기능을 만들기 시작했는데
1. 유저가 글작성페이지에서 글을 서버로 글을 보내고 
2. 서버는 글을 받으면 잘썼나 확인해보고 
3. 서버는 그걸 DB에 저장
- **3번**을 마저 해보도록 합시다.

#### DB에 document 하나 만들려면
```js
await db.collection('post').insertOne(저장할데이터) 
```
- 어떤 데이터를 DB에 저장하고 싶으면 이런 코드 작성하면 됩니다.<br>어떻게 알았냐고요? 검색해봤습니다. 

- 이러면 post라는 컬렉션에 새로운 document를 하나 만들어서 이 데이터를 안에 기록해줍니다.<br>데이터는 object자료형식으로 집어넣으면 됩니다. 

```js
await db.collection('post').insertOne({ a : 1 }) 
```

- 예를 들어 이렇게 작성하고 실행하면
![](Node.js%20&%20MongoDB%202-8.png)
- ▲ mongodb 사이트가서 확인해보면 <br>이런 식으로 document 하나가 생성되고 a : 1 이 그대로 저장되어있습니다.<br>(_id는 자동발행됩니다)

- 아무튼 테스트 삼아 해본거니까 삭제하고 <br>그럼 `.insertOne()` 안에 유저가 작성한 글을 넣으면 저장이 잘 될거같은데<br>이거 `.insertOne(요청.body)` 그대로 막 이렇게 넣습니까?<br>정확히 어떤 형식으로 집어넣어야됩니까?

![](Node.js%20&%20MongoDB%202-9.png)
- ▲ 지금 DB를 보면 글들이 이런 식으로 저장되어있습니다. <br>이 document들과 유사하게 저장하는게 좋을 것 같기 때문에 <br>`{title : 어쩌구, content : 어쩌구}`<br>이런 식으로 저장하는게 좋겠죠?

```js
app.post('/add', async (요청, 응답) => {
  await db.collection('post').insertOne({ title : 요청.body.title, content : 요청.body.content })
  응답.send('작성완료')
})
```

- 그래서 이렇게 저장하라고 했습니다.
- 실은 요청.body 출력해보면 {title : 어쩌구, content : 어쩌구} 이거랑 똑같이 나오기 때문에 <br>요청.body를 그대로 .insertOne()에 넣어도 될거같긴 한데<br>근데 그럴 경우 유저가 이상한 데이터를 보내버리면 그걸 그대로 document에 작성해버리기 때문에 위험할 수도 있을 것 같군요. 

- 그래서 아무튼 저장하고 테스트해보면 <br>이제 전송버튼누르면 글이 DB에 저장됩니다. 성공 

```js
app.post('/add', async (요청, 응답) => {
  await db.collection('post').insertOne({ title : 요청.body.title, content : 요청.body.content })
  응답.redirect('/list')
})
```

- `응답.send()`로 메세지 보내는게 싫으면<br>`응답.redirect()` 이런거 써도 됩니다. _그러면 다른 페이지로 강제로 이동_ 시켜줍니다.


#### 예외처리하는 법
- 유저가 제목을 안 적고 글을 전송하면 어쩔 것입니까.<br>한번 테스트로 글 전송 해보면 `요청.body.title` 부분이 `' '` 이렇게 비어있군요.<br>이 경우엔 DB에 저장시키면 안될 것 같군요.<br>👉 그러고 싶으면 "제목이 비어있으면 DB저장하지말기~" 이거 그대로 코드로 번역하면 되는 것일 뿐입니다. 

```js
app.post('/add', async (요청, 응답) => {
  if (요청.body.title == '') {
    응답.send('제목안적었는데')
  } else {
    await db.collection('post').insertOne({ title : 요청.body.title, content : 요청.body.content })
    응답.redirect('/list') 
  }
  
})
```

- 특정조건에 만족하는 경우에 어떤 코드를 실행하고 싶을 때는 if문 쓰면 됩니다.<br>그럼 내용도 빈칸인지 검사하고 싶으면 어떻게 할까요?<br>제목이 100자 이상으로 너무 길면 어쩌죠? <br>이런 것들도 **전부 알아서 if 문으로 처리**하면 되겠습니다. 

- 참고로 하나하나 if문 쓰기 귀찮으면 validation 라이브러리를 설치해서 쓰는 사람도 있습니다.<br>express-validator, vinejs, validator 이런 것들이 있습니다. 

- DB에 뭔가 저장할 때 몇개의 에러가 발생할 수 있습니다. 
	- DB가 다운되어서 통신이 안되거나 
	- DB에 뭔가 저장하려는데 `_id`가 똑같은게 있어서 에러가 나거나 
- 그런 경우 에러같은게 발생합니다.

- ==에러가 나는 경우에 특정 코드를 실행하고 싶으면 _try catch_ 문법을 쓰면 됩니다.==
![](Node.js%20&%20MongoDB%202-3.png)

```js
try {
   await db.collection('post').insertOne(어쩌구)
} catch (e) {
   console.log(e)
   응답.send('DB에러남')
} 
```

- 이건 try 안에 있는 코드가 뭔가 에러나면 catch 안에있는 코드를 대신 실행해주는 유용한 문법입니다. <br>catch 안에서 e라는 파라미터 출력해보면 에러 원인 같은 것도 알 수 있습니다. 

- 그래서 이런 try, catch 문법도 추가해주면 더 안전하고 뛰어난 서버코드를 작성할 수 있으니까<br>집가서 코드를 업그레이드 해옵시다.

![](Node.js%20&%20MongoDB%202-4.png)

![](Node.js%20&%20MongoDB%202-5.png)



```ad-note
배운거 정리하자면 : 
1. 코드혼자 잘짜고 싶으면 한글로 기능이 어떻게 동작하는지 설명부터하고 그걸 코드로 번역

2. `<form>`태그쓰면 서버로 POST요청할 수 있고 유저가 입력한데이터도 전송할 수 있음 

3. 서버에서 `요청.body`쓰면 유저가 폼에 입력한 데이터출력해볼 수 있음 

4. DB에 데이터저장(Document 발행)하려면 `.insertOne()`

5. 유저가 보낸 데이터 검사는 if ~ else ~ 문

6. 에러상황 처리하고 싶으면 try, catch 
```


```ad-todo
- 심심해서 연습한번 해보고 싶으면 <br>다른 페이지와 `<form>`하나 만들어서<br>전송버튼누르면 새로운 collection에 글 발행해주는 기능 한번 만들어봅시다.
```


### 상세페이지 만들기 1 (URL parameter)

![](Node.js%20&%20MongoDB%202-10.png)

![](Node.js%20&%20MongoDB%202-11.png)

![](Node.js%20&%20MongoDB%202-12.png)

![](Node.js%20&%20MongoDB%202-13.png)

![](Node.js%20&%20MongoDB%202-14.png)



![](Node.js%20&%20MongoDB%202-15.png)