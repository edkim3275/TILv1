Vue

## hw관련

- Life Cycle Hook

  ```python
  class Car:
      def __init__(self):
          pass
      def __del__(self):
          pass
      def __del__(self):
          pass
      def hi(self):
          pass
      
  c = Car()
  del c
  ```

  객체의 탄생과 죽음

![image-20210511090732046](02_vue intro(webex).assets/image-20210511090732046.png)

---

인스턴스 라이프사이클 훅

![image-20210511091027656](02_vue intro(webex).assets/image-20210511091027656.png)

- `beforeCreate` : life cycle에 접근은 가능

- `beforeMount`: 마운트 되기 직전(심장이생기기 전)
- `mounted` : mounted된 이후에 HTML과 통신이 가능. DOM에 다 그려지는 시점에 실행

---

package : 돈까스 메뉴

pacakge-lock : 돈까스를 만들기 위한 모든 과정

---

SPA는 이동을 기본적으로 이동하지 않습니다(화면전환이 이루어지지 않습니다.) 근데 URL은 이동시 화면전환이 이루어집니다. SPA의 큰 단점 특정 URL과 매핑된 것이 있어야만 공유가 가능합니다. URL이 변화되지 않으면 불편함이 생깁니다.

=> URL과 한 화면에서 계속 유지되는 것은 별개의 개념이라는 것.

---

## 실습

- `vue add router` 를 하게되면

  ![image-20210511093359995](02_vue intro(webex).assets/image-20210511093359995.png)

  4가지 변화가 있습니다.

- npm : node package manager

  node환경은 결국 컴퓨터 환경인데, 브라우저 환경과는 다릅니다.

  ![image-20210511094139598](02_vue intro(webex).assets/image-20210511094139598.png)

  node에서는 윈도우가 존재하지 않습니다.

  node에서는 최상위 키값이 global

  ![image-20210511094234505](02_vue intro(webex).assets/image-20210511094234505.png)

  `console.log(global.console.log('hi'))`가 가능해진다. 당연히 global 은 생략가능

  ![image-20210511094311243](02_vue intro(webex).assets/image-20210511094311243.png)

- export default router

  ![image-20210511095144891](02_vue intro(webex).assets/image-20210511095144891.png)

  main.js에서는

  ![image-20210511095250471](02_vue intro(webex).assets/image-20210511095250471.png)

  index.js에서는

  ![image-20210511095318028](02_vue intro(webex).assets/image-20210511095318028.png)

  위는 계약서에 서명하는것과, 악수하는 것과 유사한 의미.

  결국, 위에 내용과는 상관없이 export 내부에 넣는 것을 export하겠다는 것

  

  ![image-20210511094503561](02_vue intro(webex).assets/image-20210511094503561.png)

  import vue from 'vue'는 순정에서는 불가능.

  순정(?) node에서는 const vue = require('vue')로가능하기떄문에 node a.js식으로 실행가능.

![image-20210511094730232](02_vue intro(webex).assets/image-20210511094730232.png)

![image-20210511094738672](02_vue intro(webex).assets/image-20210511094738672.png)

console.log(b)를 해보면 빈객체 {}가 나옵니다.

이쯤에서 export default를 다시 얘기해보자면,

![image-20210511094856755](02_vue intro(webex).assets/image-20210511094856755.png)

위에 있는 내용과는 상관없이 export뒤에있는 내용이 a개 됩니다.

![image-20210511094915954](02_vue intro(webex).assets/image-20210511094915954.png)

---

- router 되돌리기

  ![image-20210511101452280](02_vue intro(webex).assets/image-20210511101452280.png)

  soft mixed hard 세가지가 존재합니다. 

  `git reset HEAD --?`

  ![image-20210511101635689](02_vue intro(webex).assets/image-20210511101635689.png)

  soft : commit은 한 단계 돌아가고 add된 상황까지 돌아간다(바로 커밋가능)

  mixed : add에서 내려서  working directory로 돌아감(add하고 커밋가능)

  hard : 실제 파일이 바뀜.

  `git reset HEAD~` : 지금 현재위치에서 한단계 뒤로 가겠다.

  `git reset --soft HEAD~`: add가 끝나있는 상태에서 뒤로 돌아가기

  `git reset --hard HEAD~` : add도 안되어있고, working directory 수정전의 커밋되어있는 상태로 돌아간다(내용이 바뀌기 때문에 조심해야함)

  `git restore <file>` : 파일복구 => `git restore src/App.vue`

---

router-link : 컴포넌트

router-view : vue가 보여지는 통로

![image-20210511104140213](02_vue intro(webex).assets/image-20210511104140213.png)

이름 컨벤션의 경우 카멜케이스, 파스칼케이스 둘다 가능하지만 HTML상에서는 케밥케이스만 가능합니다.

![image-20210511104501944](02_vue intro(webex).assets/image-20210511104501944.png)

![image-20210511104510540](02_vue intro(webex).assets/image-20210511104510540.png)

- route정의 순서

1. Component 호출
2. Component 라우터 등록

- RouterView로 들어가게 되는 애들과 아닌애들의 차이가 components와 views의 차이

---

- 게시글 작성과 redirect부분

---

## 유튜브 API 실습

- API key발급 받기

API key : AIzaSyA-jlE3pnCbCNbLHiJxlIzXnXLRsl3ePuo

- postman에서 요청보내서 정상적으로 작동하는지 확인

  ![image-20210511124658679](02_vue intro(webex).assets/image-20210511124658679.png)

- data를 살펴보면 여러가지가 있는데 .. videoID가여기서는 중요합니다!

- 유튜브에서 영상 공유해보면

  ![image-20210511125103133](02_vue intro(webex).assets/image-20210511125103133.png)

  저기서 k뭐시기가 저 영상의 id인데 우리에게 필요한 것은 id입니다.

- 다시 퍼가기를 눌러보면 iframe이 나옵니다.

  ![image-20210511125136795](02_vue intro(webex).assets/image-20210511125136795.png)

  여기서 필요한 부분은 src

  ![image-20210511125200793](02_vue intro(webex).assets/image-20210511125200793.png)

- vue create vue-youtube로 프로젝트 시작하기

- 만들려고 하는 것 구성짜기(컴포넌트)

  ![image-20210511125958811](02_vue intro(webex).assets/image-20210511125958811.png)

  APP

  최상단의 SearchBar

  VideoDetail

  VideoList

  VideoListItem

  ![image-20210511130140213](02_vue intro(webex).assets/image-20210511130140213.png)

- 컴포넌트 생성

  ![image-20210511130234276](02_vue intro(webex).assets/image-20210511130234276.png)

- main.js

  ![image-20210511130823098](02_vue intro(webex).assets/image-20210511130823098.png)

  createElement라는 함수가 들어오는데 굳이 길게 쓰지말고 인자명을 h로 해서 가져오자.

  ![image-20210511130907922](02_vue intro(webex).assets/image-20210511130907922.png)

  el: '#app' 또는 mount해주기

  ![image-20210511130948255](02_vue intro(webex).assets/image-20210511130948255.png)

  production은 배포용으로 사용하는 코드(지금은 굳이 사용하지 않겠습니다.)

### Searchbar

![image-20210511131634565](02_vue intro(webex).assets/image-20210511131634565.png)

- input에 data가 들어오면

  ![image-20210511131820164](02_vue intro(webex).assets/image-20210511131820164.png)

- input이 들어오면?? 여기서는 ssafy일건데, 해당하는 input에 대해서 결과가 나와야하니까 여기서느는 change가 적당할 수도있다.(물론 input으로 해도 됨.)

- youtube서버에 요청을 보내서 응답을 받으면? 해당 응답을 다시 List에 넘겨줘야만 합니다.

  ![image-20210511132112704](02_vue intro(webex).assets/image-20210511132112704.png)

  응답으로 N개의 배열이 오면 N개를 List에 보여주는 것

  클릭하면 다시 Detail로 보내줄 겁니다.

  이경우에는 SearchBar에서 App으로 올려보내서 VideoList로 보내줄겁니다.(근데 또 App에서 검색을 해서 밑으로 내려보내주는게 나을수도? 있습니다.)

- 검색 => 올리고 => 내린다

- axios를 예전에는 cdn을 사용했었는데(결국 js덩어리를 가지고 오는건데)이제는 node package manager를 통해서 편하게 설치 할 겁니다.

  `npm i axios`

  ![image-20210511133009025](02_vue intro(webex).assets/image-20210511133009025.png)

- ![image-20210511133305830](02_vue intro(webex).assets/image-20210511133305830.png)

- Q) 교수님 main.js 첫번째 줄에 현재 위치에서 vue 파일을 찾는데 없다면 node_modules를 탐색하는건데 현재위치에 App.vue가 있기 때문에 저기에서 Vue는 App.vue를 의미하는 건가요??

- 배열 뽑기

  ![image-20210511135450543](02_vue intro(webex).assets/image-20210511135450543.png)

- 근데 여기서 key는 숨겨야 할 것 같지 않음? 해결책!!!

  package.json을 보면

  ![image-20210511135508662](02_vue intro(webex).assets/image-20210511135508662.png)

  ![image-20210511135623829](02_vue intro(webex).assets/image-20210511135623829.png)

  그리고나면 아래와같이 사용할 수 있을겁니다

  ![image-20210511135739939](02_vue intro(webex).assets/image-20210511135739939.png)

  그럼 에러나는데

  ![image-20210511135822618](02_vue intro(webex).assets/image-20210511135822618.png)

  반드시 VUE_APP라는 것으로 해줘야합니다.

  ![image-20210511135849755](02_vue intro(webex).assets/image-20210511135849755.png)

  ![image-20210511135854913](02_vue intro(webex).assets/image-20210511135854913.png)

  이렇게 하면 .env.local은 .gitignore에 등록되어있기 때문에 public에서는 보여지지 않습니다.

  다만 요청을 할때는 공개키를 보낼 수 밖에 없습니다.

  ![image-20210511140058370](02_vue intro(webex).assets/image-20210511140058370.png)

  애초에 브라우저에서 request날라가는 건 공개키입니다. 근데 왜 숨기냐면 github에 돌아다니는 해킹봇을 피하기 위함.

- 이제 data위로 올리기

  ![image-20210511140703249](02_vue intro(webex).assets/image-20210511140703249.png)

  정보가 일단 응답된다는 것을 확인할 수 있습니다.

  ![image-20210511140849955](02_vue intro(webex).assets/image-20210511140849955.png)

- App.vue에서 들어주기

  ![image-20210511141243093](02_vue intro(webex).assets/image-20210511141243093.png)

  ![image-20210511141538425](02_vue intro(webex).assets/image-20210511141538425.png)

### VideoList

- 배열을 videolist로 내려주기

  불러오기, 등록, 사용

  ![image-20210511141652412](02_vue intro(webex).assets/image-20210511141652412.png)

  ![image-20210511141656041](02_vue intro(webex).assets/image-20210511141656041.png)

  ![image-20210511141700561](02_vue intro(webex).assets/image-20210511141700561.png)

  ![image-20210511144005980](02_vue intro(webex).assets/image-20210511144005980.png)

  ![image-20210511144018290](02_vue intro(webex).assets/image-20210511144018290.png)

  v-for는 좀 특별합니다. key는 유니크하면서 절대 겹치지 않도록 설정을 해줌으로써 해당하는 요소를 특정지어줘야만 합니다.

  유니크한 값은 여기서 인덱스나 videoId, etag... 여러개가 있으므로 알아서 찾은다음에 사용하시면 됩니다.

  ![image-20210511144919653](02_vue intro(webex).assets/image-20210511144919653.png)

- 이제 영상을 보여주게 한번 해보면(일단 이렇게 안할거임)

  ![image-20210511145316172](02_vue intro(webex).assets/image-20210511145316172.png)

- 이제 이 리스트에서 detail로 넘겨주어야만 합니다.

  ![image-20210511145736555](02_vue intro(webex).assets/image-20210511145736555.png)

  ![image-20210511145748767](02_vue intro(webex).assets/image-20210511145748767.png)

  ![image-20210511145729073](02_vue intro(webex).assets/image-20210511145729073.png)

  컴포넌트도 v-for의 대상이 될 수 있다.

### VideoListItem

- 얘네 각각을 받아줘야만 합니다.

  ![image-20210511145825228](02_vue intro(webex).assets/image-20210511145825228.png)

  ![image-20210511145932137](02_vue intro(webex).assets/image-20210511145932137.png)

  `:video="video"`로 컴포넌트를 뽑아서 보내주면 됩니다.

- 이쯤되면 부트스트랩을 한번 사용해봅시다.

  bootstrap vue라는게있는데 별로입니다.(너무 vue에 dependent합니다.)

  우린 그냥 bootstrap사용하겠습니다.

  ![image-20210511150954201](02_vue intro(webex).assets/image-20210511150954201.png)

  vue cli쓰고있는데 vue init이라는 것이 또 있습니다.(이건 또 다른 구조가 나오게 됩니다.)

  또 Vuetify라는 것도 존재합니다.

  ![image-20210511151158693](02_vue intro(webex).assets/image-20210511151158693.png)

- 일단 CDN으로 사용합니다.

  CDN복사해서 index.html에 붙여넣기

  - style에서 scoped적용해서 div, input이렇게 하지 않고, scoped적용은 하지만, class를 줘서 적용해준다.

  ![image-20210511152025435](02_vue intro(webex).assets/image-20210511152025435.png)

  이렇게 되면 scoped를 사용하지 않아도 됩니다.

- 이제 list를 올리고 올리고 내리기를 해야합니다.

  ![image-20210511152654210](02_vue intro(webex).assets/image-20210511152654210.png)

### VideoListItem

![image-20210511160406746](02_vue intro(webex).assets/image-20210511160406746.png)

이걸 computed해도 괜춘함

![image-20210511160513075](02_vue intro(webex).assets/image-20210511160513075.png)

computed에 정의해주고 위에는 아래와 같이 사용하면 된다.

![image-20210511160524690](02_vue intro(webex).assets/image-20210511160524690.png)

- 현재 페이지에서 clickable하다는 느낌을 주기 위해서는??

  ![image-20210511161141285](02_vue intro(webex).assets/image-20210511161141285.png)

  ![image-20210511161423202](02_vue intro(webex).assets/image-20210511161423202.png)

---

![image-20210511163133081](02_vue intro(webex).assets/image-20210511163133081.png)

참고 : javascript observer pattern

![image-20210511171516011](02_vue intro(webex).assets/image-20210511171516011.png)

data에서는 this를 사용하지 못하기 때문에 아래와 같은 방법은 불가능하다

![image-20210511171632245](02_vue intro(webex).assets/image-20210511171632245.png)

대신 computed에 작성하면 가능합니다

![image-20210511171845473](02_vue intro(webex).assets/image-20210511171845473.png)

![image-20210511172006078](02_vue intro(webex).assets/image-20210511172006078.png)

- 여기서 문제. 처음에 object가 비어있어서 빈 object인 경우 안보여주도록 해야된다 

  ![image-20210511172506748](02_vue intro(webex).assets/image-20210511172506748.png)

  ![image-20210511172613677](02_vue intro(webex).assets/image-20210511172613677.png)

  ![image-20210511172736059](02_vue intro(webex).assets/image-20210511172736059.png)

  v-show는 error가 등장하지만, v-if는 괜찮다.

  여기서 Object는 클래스라고 임의로 얘기하는 애입니다. Object를 만드는 함수에서keys라는 메서드가 있는데 안에 검증하고자 하는 애를 넣으면 object를 뽑아줍니다.(얘는 native JS입니다.)

  ![image-20210511173050362](02_vue intro(webex).assets/image-20210511173050362.png)

  ![image-20210511173104036](02_vue intro(webex).assets/image-20210511173104036.png)

  ![image-20210511173213517](02_vue intro(webex).assets/image-20210511173213517.png)

  이건 또 다시 삼항연산자로 바꿀수가 있는데

  ![image-20210511173325004](02_vue intro(webex).assets/image-20210511173325004.png)

  또 다시 바꾸면

  ![image-20210511173432886](02_vue intro(webex).assets/image-20210511173432886.png)

  ![image-20210511173953980](02_vue intro(webex).assets/image-20210511173953980.png)

  위처럼 data를 return하는 기능은 거의 모두 computed가 합니다.(게터)

  data setting하는 부분은 methods로 갑니다.(세터)

  ![image-20210511173553486](02_vue intro(webex).assets/image-20210511173553486.png)

- 그리드를 좀 주고 싶다면

  ![image-20210511173819130](02_vue intro(webex).assets/image-20210511173819130.png)

  ![image-20210511173832606](02_vue intro(webex).assets/image-20210511173832606.png)

- ![image-20210511174237096](02_vue intro(webex).assets/image-20210511174237096.png)

![image-20210511174253359](02_vue intro(webex).assets/image-20210511174253359.png)

​	![image-20210511174415705](02_vue intro(webex).assets/image-20210511174415705.png)

![image-20210511174432482](02_vue intro(webex).assets/image-20210511174432482.png)

- `npm i lodash`

  잘못 깔아서 삭제하고 싶다면 `npm r lodash`

- `npm run build` 모두 마무리 한 후에 이렇게 한다면 생짜 js css가 됩니다.

  ![image-20210511180045436](02_vue intro(webex).assets/image-20210511180045436.png)

