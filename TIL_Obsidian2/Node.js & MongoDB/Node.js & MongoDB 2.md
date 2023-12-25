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

- 게시판의 경우에 글제목 누르면 상세페이지 같은걸로 이동하지 않습니까<br>그래서 우리도 글마다 상세페이지를 만들어봅시다.

- 한글로 기능설명부터하면 되는데<br>근데 내가 그 기능이 어떻게 돌아가는지 몰라서 한글로 설명도 못하겠으면 <br>다른 사이트의 상세페이지 기능은 어떻게 돌아가고 있는지 살펴보면 됩니다. 

![](Node.js%20&%20MongoDB%202-10.png)

- 네이버 Vibe라는 음악감상하는 사이트인데 <br>곡을 누르면 곡마다 상세페이지가 있습니다.  

- 근데 URL 주목해보시면 
```
/track/곡번호 
```

- 이렇게 접속하면 거기에 맞는 곡의 상세페이지를 보여주는 식으로 만들어놨군요. <br>여기말고도 다른 서비스의 상세페이지들도 다 비슷하게 동작할걸요.

- 그래서 우리도 요 시스템을 카피해보도록 합시다.

- 누가 `/detail/글번호`로 접속하면 그 글번호를 가진 글의 상세페이지를 보여줍시다. <br>자 지금 DB에 글이 3개 있는데 그럼 상세페이지는 몇개 필요하죠?<br>3개 필요합니다.

- 그럼 여러분이 직접 ejs파일도 3개 만들고 `app.get()` 3번써가지고 각각 상세페이지들을 만들면 될 것 같습니다. 

- 예를 들면<br>유저가 /detail/1 로 접속하면 `_id가 1`인 글의 상세페이지 보여주기<br>유저가 /detail/2 로 접속하면 `_id가 2`인 글의 상세페이지 보여주기<br>...<br>실제로는 `_id`가 정수가 아니라 `ObjectId 형태`라 좀 길긴 하겠지만 아무튼 그럽시다.

#### URL 파라미터 문법
- 근데 문제가 있는데 만약에 글이 100개 있으면 어쩔겁니까?<br>app.get( ) 100개 만들거에요? 

- 실은 그래도 되는데 그게 싫으면 방법이 하나 있습니다. <br>**URL 파라미터 문법**을 이용하면 비슷한 URL을 가진 API를 여러개 만들 필요가 없습니다.

```JS
app.get('/detail/:aaaa', (요청, 응답) => {
  응답.send('detail.ejs')
})
```

- URL 입력란에 `:어쩌구` 이런 식으로 URL을 작성할 수가 있는데 <br>이게 뭔 뜻이냐면 _"이 자리에 유저가 아무 문자나 입력하면~"_ 이라는 뜻입니다.

- 그래서 이제 누가 _/detail/아무문자_ 로 접속하면 이 안에 있는 코드가 실행됩니다.<br>이러면 아까처럼 API 100개 만들필요가 없으니 비슷한 URL의 API가 여러개 필요하면 가져다가 쓰도록 합시다. 

- 그래서 detail.ejs 페이지도 하나 만들어서 보내주면 될거같은데 <br>**Q. 이러면 계속 같은 페이지만 보여줄 수 있는거 아님?**<br>그럴 수 있습니다.

- 지금 유저가 `/detail/1` 로 접속해도 `detail.ejs` 보내주고<br>지금 유저가 `/detail/2` 로 접속해도 `detail.ejs` 보내주기 때문에 이러면 안될 것 같은데

- 실은 ejs 파일로 여러분이 맘대로 데이터를 전송할 수 있기 때문에<br>매번 똑같은 페이지만 보일 걱정은 안해도 될 것 같습니다.


#### detail.ejs 파일 만들기
- 상세페이지로 쓸 detail.ejs 파일도 하나 만들어봅시다.

- 👇기존 ejs 페이지 복사해서 필요한 곳만 고칩시다. 
```html
<div class="detail-bg">
    <h4>글제목임</h4>
    <p>글내용임</p>
</div> 
```

```css
.detail-bg {
  background: white;
  padding: 15px;
  margin-top: 10px;
}
```

- 그럼 만들고 싶은 기능을 한글로 정리부터 해보면 
1. 누가 /detail/어쩌구로 접속하면
2. `_id`가 어쩌구인 글을 DB에서 찾아와서 
3. ejs에 글을 박아서 유저에게 보냄

- 이러면 될 것 같은데 1번은 아까 해본 거 같고 <br>2번부터 해봅시다. 

- 누가 `/detail/abc` 라고 입력해서 접속하면 <br>`_id가 abc인 글`을 찾아오면 될거같은데<br>DB에서 `_id가 abc`인걸 찾고싶으면 어떻게 하냐고요? 

![](Node.js%20&%20MongoDB%202-11.png)

#### DB에서 특정 document 1개 찾기
```js
await db.collection().findOne({a : 1}) 
```

- 이렇게 쓰면 이 자리에 `a : 1`이라는걸 가지고 있는 document를 하나 찾아서 출력해준다는군요.<br>`a : 1`을 가진게 많으면 그 중에 맨 위에 있는 document 한개만 출력해줍니다. 

- 근데 지금 a : 1 기입된 document 찾고싶은게 아니라<br>우리는 { `_id : 어쩌구` } 인 document를 찾고싶은데 이거 잘 되나 한번 테스트해봅시다.

 ![](Node.js%20&%20MongoDB%202-16.png)
▲ 대충 이런 document를 `_id`로 찾고싶으면 코드를 어떻게 짜야할까요?

```js
await db.collection('post').findOne({_id : new ObjectId('64bfde3b02d2932a4c06ffba')}) 
```

- 이렇게 작성하면 이 자리에 document를 출력해줄 것 같습니다. 진짠지 변수에 저장해서 출력해봅시다. <br>new는 왜 붙였냐면 mongodb 만든 사람이 그렇게 쓰래요.<br>근데 실은 **서버파일에서 ObjectId() 를 쓰려면 셋팅 하나가 필요**합니다. 

![](Node.js%20&%20MongoDB%202-13.png)

```js
const { ObjectId } = require('mongodb') 
```
- 서버파일 상단 쯤에 위에 이거 집어넣어놔야 하단에서 ObjectId()를 쓸 수 있습니다.

![](Node.js%20&%20MongoDB%202-14.png)

#### 유저가 URL 입력한거 가져오기 
1. 누가 /detail/어쩌구로 접속하면
2. `_id`가 어쩌구인 글을 DB에서 찾아와서 
3. ejs에 글을 박아서 유저에게 보냄

- 이제 이거 코드로 번역하면 되는데 <br>일단 유저가 /detail/어쩌구 로 접속하면<br>{ `_id : 어쩌구` } 를 가지고 있는 document를 찾아야합니다. <br>그니까 {` _id : 유저가URL 파라미터에입력한거` } 이런 document를 찾아와야 합니다. <br>"유저가 URL 파라미터에 입력한거" 이건 어떻게 알 수 있냐고요? 


```js
app.get('/detail/:aaaa', (요청, 응답) => {
  console.log(요청.params)
})
```

- `요청.params`라고 출력해보면 유저가 URL 파라미터 자리에 입력한 데이터가 출력됩니다.<br>아마 object 자료형으로 출력될걸요 

 - 그럼 배울건 다 배웠으니 1, 2, 3번 기능을 구현해서 상세페이지 기능을 다음시간까지 완성해옵시다. 

```ad-todo
오늘의 숙제 : 
- 상세페이지 기능을 완성해옵시다.
- 유저가 /detail/ 뒤에 글_id 를 입력해서 GET요청을 날리면
- detail.ejs 페이지를 보여주는데 글제목과 내용이 페이지에 박혀있어야합니다. 
```

![](Node.js%20&%20MongoDB%202-12.png)

![](Node.js%20&%20MongoDB%202-17.png)

```html
<!-- list.ejs -->
  <body class="grey-bg">
    <%- include('nav.ejs') %>
    <div class="white-bg">
      <% for (let i = 0; i < 글목록.length; i++){ %>
      <div class="list-box">
        <a href="/detail/<%= 글목록[i]._id %>"
          ><h4><%= 글목록[i].title %></h4></a
        >
        <p><%= 글목록[i].content %></p>
      </div>
      <% } %>
    </div>
  </body>
```

```html
<!-- detail.ejs --> 

  <body class="grey-bg">
    <%- include('nav.ejs') %>

    <div class="detail-bg">
      <h4><%= 글목록.title %></h4>
      <p><%= 글목록.content %></p>
    </div>
  </body>
```

```js
// server.js

app.get("/detail/:aaaa", async (요청, 응답) => {
  console.log(요청.params.aaaa);
  let result = await db
    .collection("post")
    .findOne({ _id: new ObjectId(`${요청.params.aaaa}`) });
  응답.render("detail.ejs", { 글목록: result });
});
```

### 상세페이지 만들기 2 (링크 만들기)
- 저번시간에 상세페이지 열심히 완성해오랬는데<br>코드 따라치기만 하면 그냥 따라치기 잘하는 사람이 될 뿐<br>직접 뭐라도 해보는 시간이 정말 중요합니다.

#### 저번시간 숙제
1. 누가 /detail/어쩌구로 접속하면
2. { `_id` : 어쩌구 } 인 글을 DB에서 찾아와서
3. detail.ejs 파일에 집어넣어서 유저에게 보냄 
- 이걸 코드로 옮겨보면

```js
app.get('/detail/:id', async (요청, 응답) => {
  let result = await db.collection('post').findOne({ _id : new ObjectId(요청.params.id) })
  응답.render('detail.ejs', { result : result })
})
```

- 이거 아닐까요<br>URL파라미터 사용시 : 콜론기호 뒤엔 자유롭게 작명가능합니다.

![](Node.js%20&%20MongoDB%202-18.png)

```html
(detail.ejs)
<div class="detail-bg"> 
  <h4><%= result.title %></h4> 
  <p>글내용임</p> 
</div>
```
- 이제 detail.ejs 파일에선 result라고 쓰면 그 document 내용이 잘 출력될 것 같습니다. <br>이제 테스트 삼아서 **/detail/DB에있던글_id** 로 한번 접속해보시길 바랍니다. 
- 그럼 페이지 내용이 잘 출력되는군요.

#### 링크만들기
- 그래서 아무튼 이제 /detail/DB에있던글_id 로 접속하면 <br>그 글의 상세페이지를 보여주고 있는데 의문점이 하나 듭니다. <br>유저들이 천재도 아니고 이거 글_id를 주소창에 어떻게 입력하죠?

![](Node.js%20&%20MongoDB%202-20.png)
- 👆Object, array는 이렇게 나옴

- 👇 `JSON.stringfy(result)`로 출력 
![](Node.js%20&%20MongoDB%202-19.png)


![](Node.js%20&%20MongoDB%202-22.png)

![](Node.js%20&%20MongoDB%202-21.png)


- _실은 링크라는게 좋은게 있습니다._<br>누르면 자동으로 /detail/DB에있던글_id로 GET요청되는 링크나 버튼 만들어두면 되는거 아닙니까.<br>그래서 list페이지에 링크들을 만들어보도록 합시다.

```js
<a href="/어쩌구">클릭</a>
```
- `<a>`태그를 쓰면 링크를 만들 수 있고 그거 누르면 /어쩌구라는 URL로 페이지가 이동됩니다.

```js
(list.ejs)

<div class="white-bg">
  <% for (let i = 0; i < 글목록.length; i++){ %>
    <div class="list-box">
      <h4>
        <a href="/detail/<%= 글목록[i]._id %>">
          <%= 글목록[i].title %>
        </a>
      </h4>
      <p>글내용임</p>
    </div>
  <% } %>
</div>
```

- 그래서 href=" " 안에 글의 `_id`를 집어넣어봤습니다.<br>글의 `_id`는 글목록이라는 변수 출력해보면 나올텐데<br>거기서 뽑아서 집어넣어봤습니다. 

- 클릭하면 이동 잘 되나 확인해봅시다. <br>참고로 링크들에 밑줄쳐있는게 아니꼬우면 <br>a태그에 text-decoration : none 스타일을 줍시다. 


#### 예외상황 처리하기
![](Node.js%20&%20MongoDB%202-23.png)
- \* 참고: 서버의 에러 코드 

- 여러분이 어떤 서버기능을 하나 만들었으면<br>예외상황들에 대처해주는 코드도 넣는게 좋습니다. 

- 예를 들어 유저가 /detail/글_id를 입력하는게 아니라<br>이상한걸 /detail/바보 라고 입력해서 서버로 요청을 날리면 어떻게 될까요? 

- 한번 시도해봅시다.<br>아마 터미널에 에러메세지가 뜰걸요.

```js
app.get('/detail/:id', async (요청, 응답) => {
  try {
    let result = await db.collection('post').findOne({ _id : new ObjectId(요청.params.id) })
    응답.render('detail.ejs', { result : result })
  } catch (){
    응답.send('이상한거 넣지마라')
  }
  
})
```

- 그래서 그런 상황을 막고싶으면 예외처리하면 되는데<br>에러를 막고 싶으면 `try catch` 안에 넣으면 됩니다. 

- 근데 이렇게 해놓으면 잘 될 것 같은데<br>제가 한번 에러를 회피해보도록 하겠습니다.

![](Node.js%20&%20MongoDB%202-25.png)
![](Node.js%20&%20MongoDB%202-26.png)

- 에러메세지 잘 읽어보면 ObjectId() 안에 들어갈 문자가 너무 짧다는 에러같은데<br>그럼 /detail/적절한길이의랜덤문자 로 접속하면 어떻게 될까요? 


#### Q. `_id` 길이는 맞는데 틀렸을 경우
⇒ null 이 출력됨

![](Node.js%20&%20MongoDB%202-27.png)
![](Node.js%20&%20MongoDB%202-24.png)

▲ URL에 24자의 이상한 문자를 기입했더니 이번엔 ejs 파일에서 에러가 났다는군요. <br>null에다가 .title을 붙일 수 없다는 소리같습니다. <br>그래서 다양한 상황을 직접 테스트해보는게 중요합니다. 

- 이런 상황에서 result 변수같은걸 출력해보면 null이 나오는데 <br>(null은 텅 비었다는걸 나타내는 자료형입니다)

- 만약에 db에서 찾은 게시물이 null 이면 메세지 보내라고 if문 같은거 쓰면 될 것 같습니다.

```js
// if 문을 사용하여 예외처리

app.get("/detail/:id", async (요청, 응답) => {
  try {
    let result = await db
      .collection("post")
      .findOne({ _id: new ObjectId(`${요청.params.id}`) });
    if (result == null) {
      응답.status(404).send("그런 글 없");
    }
    응답.render("detail.ejs", { 글목록: result });
  } catch (e) {
    console.log(e);
    응답.status(404).send("이상한 url 입력함");
  }
});
```

- if문을 추가해봤습니다. <br>그리고 예외상황에선 에러코드같은것도 보내주면<br>프론트엔드에서 유저가 어떤 문제인지 파악하기 쉬운데 

- _유저 잘못으로 에러가 났을 경우엔 4XX 같은 코드를_ .status() 안에 넣어주면 되고<br>_서버 잘못으로 에러가 났을 경우엔 5XX 같은 코드를_ .status() 안에 넣어주면 됩니다.

- 안한다고 뭐 나쁜건 없는데 프론트엔드에서 서버와 통신할 때 에러원인 찾는게 쉬워집니다.

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

- 더 정확히 하고싶으면 status code 목록같은게 있는데 <br>이런거 보고 정확히 기재하셔도 좋습니다. 

- 아무튼 결론은 굳이 저 따라안해도 <br>여러분들이 직접 악성 유저가 되어서 테스트해보면 금방 알 수 있습니다.

그래서 저번강의 이번강의 배운거 정리하면 
1. URL 파라미터 문법 이용하면 비슷한 URL가진 API 여러개 만들 필요가 없음 
2. db에서 게시물 하나만 찾아오려면 `db.collection().findOne({ })`
3. 여러분들이 직접 악성유저가 되어서 이거저거 테스트해보고 그걸 다 예외처리하면
더 안정적인 서버기능을 만들 수 있습니다.


### 수정기능 만들기 1
1. 수정버튼 누르면 수정 페이지로
2. 수정 페이지엔 기존 글이 채워져 있음
3. 전송 누르면 수정한 내용이 보여짐