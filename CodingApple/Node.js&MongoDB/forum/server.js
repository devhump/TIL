const express = require("express");
const app = express();

app.use(express.static(__dirname + "/public"));

const { MongoClient } = require("mongodb");

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

app.get("/", (요청, 응답) => {
  응답.sendFile(__dirname + "/index.html");
});

app.get("/news", (요청, 응답) => {
  db.collection("post").insertOne({ title: "어쩌구" });
  // 응답.sendFile(__dirname + "/index.html");
});

app.get("/shop", function (요청, 응답) {
  응답.send("쇼핑페이지입니다~");
});

app.get("/about", function (요청, 응답) {
  응답.sendFile(__dirname + "/about.html");
});

app.get("/list", async (요청, 응답) => {
  let result = await db.collection("post").find().toArray();
  console.log(result);
  응답.send("DB에 있던 게시물");
});
