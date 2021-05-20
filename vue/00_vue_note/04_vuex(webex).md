# Vuex

다음주 장고 서버만들고, 서버와 vue를 붙이면 끝이납니다...!

- hw : FTFT

---

- validation 관련해서 store의 action에서 할 것인지, 컴포넌트의 method에서 할 것인지...

  확장성을 고려한다면 actions에서, 단일성이라고 한다면 method에서

  ![image-20210513092422319](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20210513092422319.png)



- 1 deleTodo를 삭제

  ![image-20210513092921096](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20210513092921096.png)

  2 DELETE_TODO를 호출

  ![image-20210513092934144](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20210513092934144.png)

  3 deleteTodo를 호출

  ![image-20210513092945525](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20210513092945525.png)

  ![image-20210513093058240](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20210513093058240.png)

  여기서 너무 자주 deleteTodo를 명명해야 하는 것이 번거롭다. 어딜 거쳐 가는 것이 너무 까다로움

  ![image-20210513093252272](04_vuex(webex).assets/image-20210513093252272.png)

  실제로 deleteTodo는 action에 있으니.. 바로 action으로 이동하게 하면 안되는 걸까?? => 그것이 바로 helper

  그렇다면 본래 dispatch를 사용했던 것 과의 차이는 무엇일까?

  ![image-20210513100657001](04_vuex(webex).assets/image-20210513100657001.png)

  ![image-20210513100731072](04_vuex(webex).assets/image-20210513100731072.png)

  큰 차이는 없으나 편의성이 증대된다는 것(그래서 헬퍼임)



- helper

  `import vuex from 'vuex'` 를 하고 console.log(vuex)를 해보면..

  ![image-20210513093508716](04_vuex(webex).assets/image-20210513093508716.png)

  ![image-20210513094333096](04_vuex(webex).assets/image-20210513094333096.png)



- 그렇다면 helper를 사용할때 인자는 어떻게 넘기는가??

  호출을 할때 ()안에 인자를 넣어주는 방식으로 넘겨주게 된다.(함수를 실행하는 것이 아니라 인자를 넘겨준다는 의미)

  ![image-20210513102046070](04_vuex(webex).assets/image-20210513102046070.png)



- splice : 해당 인덱스 부터 두번째 인자개수 만큼 삭제를 한 후, 원본 변경

  ![image-20210513095114980](04_vuex(webex).assets/image-20210513095114980.png)

  해당 인덱스를 확인 뒤 사용하게 되는거 ㅇㅇ

  ![image-20210513095251748](04_vuex(webex).assets/image-20210513095251748.png)



- 특별한 값이 존재할 때 해당하는 값을 뽑을때는 for 문을 도는 방법도 있지만 find나 filter를 사용해보자(Array Helper Method)

  ![image-20210513102742590](04_vuex(webex).assets/image-20210513102742590.png)



- (클래스와 스타일 바인딩)

  버튼을 클릭할때 클래스 속성을 바뀌게 하고 싶다면??

  ![image-20210513103308522](04_vuex(webex).assets/image-20210513103308522.png)

  ![image-20210513103457250](04_vuex(webex).assets/image-20210513103457250.png)

  ![image-20210513103518539](04_vuex(webex).assets/image-20210513103518539.png)



- localStorage에 저장하기

  localStorage.setItem('key', 'value')

  ![image-20210513111243149](04_vuex(webex).assets/image-20210513111243149.png)

  ![image-20210513111324491](04_vuex(webex).assets/image-20210513111324491.png)

  이 처럼 우리는 state를 저장해야만 합니다.

  `npm i vuex-persistedstate`를 실행

  ![image-20210513111416376](04_vuex(webex).assets/image-20210513111416376.png)

  ![image-20210513111645330](04_vuex(webex).assets/image-20210513111645330.png)



## Youtube_pjt_vuex

- mutation에는 비동기 작업이 들어가지 않는다. 외부요청이 들어갈 경우?? 어떻게 해야할까??에 대해서 생각해보시길

- App.vue와 컴포넌트들을 일단 가져옵니다.

- Modeling을 해야하는데 시작할때 어떤 점을 생각해야 할까요?

  'state'와 컴포넌트 구조

  1 화면구성

  2 안에서 사용되는 데이터와 동작들

- state에는 videos, seletedVideo만 존재

  ![image-20210513164020367](04_vuex(webex).assets/image-20210513164020367.png)

- mutations(비동기요청x)

  state건드는 것들 뿐이니 SET으로 시작해봅니다

  ![image-20210513164151577](04_vuex(webex).assets/image-20210513164151577.png)

- actions

  첫번째 인자로 context가 들어오고, 두번째 인자로 받아올 데이터를 선택해줍니다. 확인해보면 query가지고 오는 것을 확인가능

  ![image-20210513164546075](04_vuex(webex).assets/image-20210513164546075.png)

  ![image-20210513164622691](04_vuex(webex).assets/image-20210513164622691.png)

  state변경하는 것은 action이 아닌 mutation이므로 호출해야만 합니다. mutation은 commit으로 호출.

  `context.commit('SET_VIDEOS', res.data.items)`

  ![image-20210513164810385](04_vuex(webex).assets/image-20210513164810385.png)

- actions.selectVideo()

  ![image-20210513165321147](04_vuex(webex).assets/image-20210513165321147.png)



- 모듈화 분리

  통신에 관련된 곳은 따로 모듈화해놓을 수 있습니다.

  URL들만 따로 모아서 담을 파일을 하나 만들어 줍니다.

  ![image-20210513165700691](04_vuex(webex).assets/image-20210513165700691.png)

  ![image-20210513165713765](04_vuex(webex).assets/image-20210513165713765.png)

  ![image-20210513165705463](04_vuex(webex).assets/image-20210513165705463.png)



- computed관련내용은 getters로 해결

  ![image-20210513165912263](04_vuex(webex).assets/image-20210513165912263.png)

- imgUrl만 따로 뽑아오는 computed내용이 존재합니다.(이건 잠깐 보류)

  ![image-20210513170042913](04_vuex(webex).assets/image-20210513170042913.png)