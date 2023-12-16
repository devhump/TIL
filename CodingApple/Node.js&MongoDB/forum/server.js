const express = require("express");
const app = express();

app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const { MongoClient, ObjectId } = require("mongodb");

let db;
const url =
  "mongodb+srv://ramy:mongo123@cluster0.1obbp2g.mongodb.net/?retryWrites=true&w=majority";
new MongoClient(url)
  .connect()
  .then((client) => {
    console.log("DB연결성공");
    db = client.db("forum");

    app.listen(8080, () => {
      console.log("http://localhost:8080 에서 서버 실행중");
    });
  })
  .catch((err) => {
    console.log(err);
  });

app.get("/", function (요청, 응답) {
  응답.sendFile(__dirname + "/index.html");
});

app.get("/news", (요청, 응답) => {
  응답.send("오늘 비옴");
});

app.get("/shop", function (요청, 응답) {
  응답.send("쇼핑페이지입니다~");
});

app.get("/list", async (요청, 응답) => {
  let result = await db.collection("post").find().toArray();
  응답.render("list.ejs", { 글목록: result });
});

app.get("/time", async (요청, 응답) => {
  let result = new Date();
  응답.send(result);
});

app.get("/write", async (요청, 응답) => {
  응답.render("write.ejs");
});

app.post("/add", async (요청, 응답) => {
  console.log(요청.body);

  try {
    if (요청.body.title == "") {
      응답.send("제목입력 안했는데?");
    } else {
      await db
        .collection("post")
        .insertOne({ title: 요청.body.title, content: 요청.body.content });
      응답.redirect("/list");
    }
  } catch (e) {
    console.log(e);
    응답.status(500).send("서버 에러남");
  }
});

app.get("/detail/:aaaa", async (요청, 응답) => {
  console.log(요청.params);
  let result = await db
    .collection("post")
    .findOne({ _id: new ObjectId("653a66f64ca3397a50f26de3") });
  console.log(result);
  응답.render("detail.ejs");
});

// app.post("/add", (요청, 응답) => {
//   db.collection("post").insertOne({
//     title: `${요청.body["title"]}`,
//     content: `${요청.body["content"]}`,
//   });
//   console.log("저장완료");
// });
