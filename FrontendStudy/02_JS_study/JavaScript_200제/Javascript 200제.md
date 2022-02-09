# Javascript 200제

## 파트 1

### 웹 콘솔

- 자바스크립트의 콘솔 객체 함수를 통해 명시적으로 오류, 경고 및 정보 메시지 등을 출력
  - 출력 정보를 확인하는 방빗을 응용하여 디버깅 용도로 활용 가능
  - 대화형 쉘 프롬프트(Interactive Shell Prompt) 용도 또한 가능
    - 대화하는 것처럼 처리 흐름을 주고받는 형식
    - 콘솔 입력 창을 통해 JS 코드를 실시간으로 입력 - 실행하고, 검증된 실행 결과를 바로 보여주는 대화형 상호 작용이 가능하다는 것.

- 모든 웹 브라우저는 **브라우저 객체 모델(Browser Object Model)**을 갖고 있다.
  -  웹 브라우저와 관련된 객체의 집합
  - 대표적으로 window, location, navigator, history, screen, document 객체가 있다.

- 브라우저 콘솔 vs. 웹 콘솔
  - 브라우저에 따라 브라우저 콘솔과 웹 콘솔로 나뉨
  - 브라우저 콘솔은 단일 콘텐츠 탭이 아닌 전체 브라우저에 적용되는 콘솔
  - 일반적으로 단일 탭마다 환경을 다르게 활용하는 것이 유용하므로 웹 콘솔을 주로 사용

### Node.js REPL

REPL이 무엇인지 알아보기 전에 노드 REPL 환경을 실행

`윈도우 + r > cmd` 명령프롬프트 실행

`$ node` 명령어로 노드 REPL환경을 실행

이제 `>`로 시작하는 프롬프트에서 원하는 자바스크립트 코드를 입력할 수 있다.

<img src="C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20211218124413494.png" alt="image-20211218124413494" style="zoom:50%;" />

- REPL은 'Read-Eval-Print-Loop'의 약자
- 사용자가 입력한 결과를 바로 반환하는 대화형 Shell 환경을 의미한다.
- 노드는 REPL 환경을 기본적으로 제공하며 다음과 같은 기능을 수행한다.
  - Read : 사용자의 명령어를 입력받으면 메모리에 자바스크립트 데이터 구조로 분석(Read)
  - Eval : 분석한 명령어를 내부 데이터 구조로 가져와서 평가(Evaluate). 여기서 '평가'란 해당 명령어를 실행하는 것을 의미
  - Print : Eval에 의해 얻어진 결과를 받아서 사용자에게 출력(Print)
  - Loop : Print까지 완료된 다음, 다시 Read 상태로 돌아가는 환경이 반복(Loop). `ctrl + c`를 입력하면 루프를 종료

### VS Code

웹 콘솔이나, 노드 REPL만으로는 길거나 복잡한 코드를 작업하기에는 한계가 있을 수 있기에 사용하는 것이 에디터.

마이크로소프트에서 개발한 소스코드 에디터 비주얼 스튜디오 코드(Visual Studio Code)

- html파일에서 js파일 사용는 방법

![image-20211218130109408](C:\Users\edgar\AppData\Roaming\Typora\typora-user-images\image-20211218130109408.png)