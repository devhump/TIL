### 플렉스 레이아웃으로 무엇을 할 수 있나요?

- **행 또는 열로 표시할 수 있습니다. (1차원 레이아웃)**
- 문서의 쓰기 모드를 존중합니다.
- 기본적으로 한 줄이지만 여러 줄로 줄 바꿈하도록 요청할 수 있습니다.
- 레이아웃의 항목이 DOM의 순서와 다르게 시각적으로 재정렬될 수 있습니다.
- 공간이 항목 내부에 분산될 수 있으므로 상위 항목의 사용 가능한 공간에 따라 더 커지고 작아집니다.
- 상자 정렬 속성을 사용하여 래핑된 레이아웃의 항목 및 플렉스 라인 주위에 공간을 분배할 수 있습니다.
- 항목 자체를 교차 축에 정렬할 수 있습니다.



![image-20220901114103548](C:\Users\blues\AppData\Roaming\Typora\typora-user-images\image-20220901114103548.png)

- 플렉스 컨테이너 사용하기

```css
.container {
  display: flex;
}
```

- 이것이 의미하는 바는
  - 항목이 행으로 표시됩니다. (기본값 `row`)
  - 래핑하지 않습니다.
  - 컨테이너를 채우기 위해 크기가 확대되지 않습니다.
  - 컨테이너의 시작 부분에 줄을 맞춥니다.



- 항목의 방향 제어 (`flex-direction`)
  - `row` ***(기본값)***  
  - `row-reverse`(rtl, 아랍어 등)
  - `column` 
  - `column-reverse`



![image-20220901114818477](C:\Users\blues\AppData\Roaming\Typora\typora-user-images\image-20220901114818477.png)



![image-20220901114848706](C:\Users\blues\AppData\Roaming\Typora\typora-user-images\image-20220901114848706.png)

- 컨테이너 크기를 벗어나 오버플로우 된 상태 (`nowrap` 일 경우)

```css
.container {
  display: flex;
  flex-wrap: wrap;
}

.container {
  display: flex;
  flex-flow: column wrap;
    /*flex-direction과 flex-wrap을 합쳐서 표현 
    각각 첫번째, 두번째 value */
}
```



![image-20220901115046433](C:\Users\blues\AppData\Roaming\Typora\typora-user-images\image-20220901115046433.png)

- wrapping 된 경우



### Flexbox 정렬 개요

`justify-content`: 주 축의 공간 분배.

`align-content`: 교차 축의 공간 분배.

`place-content`: 위의 두 속성을 모두 설정하기 위한 줄임 속성.



```css
.container {
  display: flex;
  justify-content: flex-end;
  /*
      justify-content: flex-start; 기본값
      justify-content: flex-end;
      justify-content: center;
      justify-content: space-around;
      justify-content: space-between;
      justify-content: space-evenly;
    */
}
```



```css
.container {
  align-content: stretch; /* 기본값*/
    /*
          align-content: flex-start;
          align-content: flex-end;
          align-content: center;
          align-content: space-around;
          align-content: space-between;
          align-content: space-evenly;
    */
}

.container {
  place-content: space-between;
  /* sets both to space-between */
  /* */
}

.container {
  align-items: stretch;
    /*
          align-content: flex-start;
          align-content: flex-end;
          align-content: center;
          align-content: stretch;
    */
}
```



. `align-content`는 여러 줄들 사이의 간격을 지정하며, `align-items`는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정합니다. 한 줄만 있는 경우, `align-content`는 효과를 보이지 않습니다.

- flex 항목에 지정 가능한 속성들

  - flex-grow
  - flex-shrink
  - flex-basis

- 500 픽셀의 크기를 갖는 **flex 컨테이너** 내에 100 픽셀 크기의 자식 세 개가 존재할 때, **사용가능한 공간** 200 픽셀이 남게 됩니다. 기본적으로 flexbox는 이 공간을 마지막 자식 요소 다음에 빈공간으로 남겨둡니다.

- **flex 항목**에 크기가 지정되어 있지 않으면, **flex 항목**의 내용물 크기가 flex-basis 값으로 사용됩니다.

  ```css
  .container {
    display: flex;
    flex-basis: auto /* 기본값*/
  }
  
  /*주축에서 남는 공간을 할당할 때 */
  .container {
    display: flex;
    flex-grow: 1; /* 동일한 비율 */
    flex-grow: 2; /* 2배의 가중치를 줌 */
  }
  
  /*주축의 공간이 부족할 때 각 항목의 사이즈를 줄이는 방법*/
  .container {
    display: flex;
    flex-shrink: 1; /* 동일한 비율 */
    flex-shrink: 2; /* 2배의 가중치를 줌 */
  }
  ```

  

- [MDN - flexbox](https://developer.mozilla.org/ko/docs/Learn/CSS/CSS_layout/Flexbox#%EC%99%9C_flexbox%EC%9D%B8%EA%B0%80)

- [MDN - flexbox의 기본개념](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

- [Flex 관련 개념들 정리](https://thrillfighter.tistory.com/489)
