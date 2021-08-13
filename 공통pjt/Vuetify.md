# Vuetify

> 프로젝트 중 Vuetify를 사용하면서 유용한 정보들을 모아놓고, 몰랐던 점을 기록하는 markdown입니다.

### bottom-navigation

#### props

- `active-class` : `v-btn`에 영향을 줍니다. `default`는 `v-btn--active`
- `app` : 해당 컴포넌트를 애플리케이션 레이아웃의 일부로 지정합니다. content sizing을 동적으로 조정하는데 사용됩니다. 즉 content내용을 덮어씌우지 않고 해당 컴포넌트가 적용됩니다.
  - 이 prop을 사용하는 컴포넌트는 기능을 적절히 수행하기 위해 `v-main`의 **바깥에** 위치해야 합니다.
- `background-color` : 배경색 지정
- `color` : 특정한 색상을 적용.
  -  it can be the name of material color (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`)

### border

```css
// border: 너비, 스타일, 색
border: 2px dotted black
```

### input

- 투명도설정 css

  ```
  https://codingbroker.tistory.com/58
  ```

  ```
  <input style="background-color=transparent;"
  ```

### div

-  배경을 이미지로 설정

  ```
  background: url("url주소")
  ```

  