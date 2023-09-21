```html

<!-- 텍스트 색상 변경 -->
<p class="text-danger">happy hacking</p>

```



- viewport (뷰포트)
  - 현재 화면에 보여지고 있는 다각형(보통 직사각형)의 영역입니다. 
  - 웹 브라우저에서는 현재 창에서 문서를 볼 수 있는 부분(전체화면이라면 화면 전체)을 말합니다. 
  - 뷰포트 바깥의 콘텐츠는 스크롤 하기 전엔 보이지 않습니다.



- responsive web (반응형 웹)

  - 하나의 웹사이트로 데스크탑 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹 페이지



- 미디어 쿼리

  디바이스의 화면 크기에 따라 출력 형태를 다르게 적용할 수 있게 하는 방법

  반응형 웹을 구성하기 위한 핵심 요소

  ```css
  @media media-type and (media-feature-rule) {
    /* CSS rules go here */
  }
  ```

  - media-type : all, print, screen

  - media-feature-rule : width, min-width, max-width

    - 미디어(화면)의 특정 사이즈에 꼭 맞거나, 그 이상 그 이하를 표현함

    - ```css
      /*화면 너비가 768px 이하 일 때 적용 되는
      stylesheet를 불러옴*/
      
      <link rel="stylesheet" media="screen and (max-width: 768px)" href="mystyle.css" />
      
      /*화면 너비가 768px 이하 일 때 적용되는 style*/
      @media screen and (max-width: 768px) {
      	body {
      		background-color: lightgreen;
      	}
      }
      ```

    - 

### Breakpoints

- Breakpoints are customizable widths that  determine how your responsive layout behaves across device or viewport  sizes in Bootstrap.
  - **Breakpoints are the building blocks of responsive design**
  - **Use media queries to architect your CSS by breakpoint.**
  - **Mobile first, responsive design is the goal.**
  - Website content responds to these points and adjusts itself to the screen size to display the accurate layout.
  - ```css
    /* 그리드에서, 각각 화면의 크기에 따라 차지하는 비율을 나타냄 */
    
    <div class="col-12 col-sm-8 col-md-6 col-lg-4">
    
    
    ```
  - 

- Available breakpoints

  | Breakpoint        | class infix | Dimensions |
  | ----------------- | ----------- | ---------- |
  | Extra small       | None        | <576px     |
  | Small             | sm          | >=576px    |
  | Medium            | md          | >=768px    |
  | Large             | lg          | >=992px    |
  | Extra Large       | xl          | >=1200px   |
  | Extra extra large | xxl         | >=1400px   |

  

---



### Content

#### images

```css

/* max-width: 100%; height: auto; */
.img-fluid

.img-thumnail

/*border-radius*/
.rounded

/* Align images */
.float-start
.float-end


```

