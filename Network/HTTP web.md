# HTTP 웹 기본 지식

[TOC]



- 모든 것이 HTTP 기반 위에서 동작

- 어디서, 왜 해당하는 기능이 필요한지에 대한 공부가 필요합니다.

- 개발자는 평생 HTTP 기반 위에서 개발을 해야합니다. 언젠가 한번은 정리해야하는걸 여기서 해보자

## 강의목표

- HTTP 전체 흐름
- 실무에 꼭 필요한 핵심내용
- 수 많은 예시와 그림으로 쉽게 설명

## 순서

- 인터넷 네트워크

- URI, 웹 브라우저
  - URL, URI, URN
  - HTTP 메시지 전송

- HTTP 기본
  - 무상태 - Stateless
  - 지속연결
- HTTP 메서드
  - GET POST PUT DELETE

- HTTP 메서드 활용

- HTTP 상태코드
- HTTP 헤더

- HTTP 캐시

## 1. 인터넷 네트워크

![image-20210706140407333](HTTP web.assets/image-20210706140407333.png)

### 1.1. 인터넷 통신

인터넷에서 컴퓨터가 어떻게 통신할까?

![image-20210706160658647](HTTP web.assets/image-20210706160658647.png)

어떻게 목적지 까지 안전하게 데이터가 도착할까?

### 1.2. IP

- IP주소부여
- 지정한 IP주소에 데이터 전달
- 패킷(Packet)이라는 통신 단위로 데이터 전달
- IP패킷
  - 출발지IP, 목적지IP
  - 인터넷 망에 IP패킷을 던지게 되면 서로 노드끼리 던지기를 하다가 결국 최종 목적지IP에 데이터가 도달하게 된다

- IP프로토콜의 한계
  - 비연결성
    - 패킷을 받을 대상이 없거나 서비스 불능 사태여도 패킷이 전송됨(예를들어 친구서버가 꺼져있어도 패킷을 보냄)
    - 대상 서버가 패킷을 받을 수 있는 상태인지 모름
  - 비신뢰성
    - 신뢰할 수 없다.
    - 중간에 패킷이 사라진다면?(패킷소실)
    - 패킷이 순서대로 오지 않는다면?(패킷 전달 순서 문제) 보통 1500byte를 넘으면 나누어서 보내게 됨.
  - 프로그램 구분
    - 같은 IP를 사용하는 서버에서 통신하는 애플리케이션이 둘 이상이면?

### 1.3. TCP와 UDP

![image-20210706161524627](HTTP web.assets/image-20210706161524627.png)

- TCP
  - 위에서의 여러가지 문제들(패킷소실, 전달 순서 등의 문제)을 해결하기 위한 프로토콜
  - 전송제어프로토콜
  - 특징
    - 연결지향 - TCP 3 way handshake(가상 연결)
    - 데이터 전달 보증
    - 순서 보장

![image-20210706161657039](HTTP web.assets/image-20210706161657039.png)

![image-20210706161715215](HTTP web.assets/image-20210706161715215.png)

![image-20210706161943774](HTTP web.assets/image-20210706161943774.png)

![image-20210706161951824](HTTP web.assets/image-20210706161951824.png)

- 연결지향
  - 연결이 되지 않으면 데이터 전송과정이 이루어지지않는다.
  - 요즘에는 3ACK과정에서 데이터를 보내긴합니다.
  - 사실상 논리적인 연결이지 물리적인 연결은 아닙니다.

![image-20210706162220488](HTTP web.assets/image-20210706162220488.png)

![image-20210706162528465](HTTP web.assets/image-20210706162528465.png)

![image-20210706162604869](HTTP web.assets/image-20210706162604869.png)

전송제어, 순서, 검증정보들이 TCP헤더에 담겨져 있어서 가능한 것

- UDP
  - 특징이 없음
  - IP와 거의 흡사하나 포트번호가 추가 됩니다.(패킷 구분을 위해서 사용되는 포트번호) + 데이터 검증을 위한 체크섬
  - 최근 각광? 웹브라우저에서 HTTP3.0 통신을 할 때, 3way shake 단계를 줄여보자라는 느낌이기 때문

![image-20210706162729658](HTTP web.assets/image-20210706162729658.png)

### 1.4. PORT

![image-20210706163118414](HTTP web.assets/image-20210706163118414.png)

여러가지 패킷이 오면 어떤 애플리케이션에 대한 패킷인지 구분하는 것에 문제가 생긴다.

따라서 생긴 것이 포트번호(cf IP는 목적지 서버를 찾기위한 주소)

![image-20210706163240426](HTTP web.assets/image-20210706163240426.png)

![image-20210706163301122](HTTP web.assets/image-20210706163301122.png)

![image-20210706163428774](HTTP web.assets/image-20210706163428774.png)

### 1.5. DNS

- IP는 기억하기 어렵다.
- IP는 변경될 수 있다.

![image-20210706163535406](HTTP web.assets/image-20210706163535406.png)

![image-20210706163548092](HTTP web.assets/image-20210706163548092.png)

![image-20210706163609358](HTTP web.assets/image-20210706163609358.png)

![image-20210706163626771](HTTP web.assets/image-20210706163626771.png)

## 2. URI와 웹 브라우저 요청 흐름

### 2.1. URI(Uniform Resouce Indentifier)

![image-20210706170806482](HTTP web.assets/image-20210706170806482.png)

- URI는 로케이터(locator), 이름(name) 또는 둘다 추가로 분류될 수 있다.

- Resource를 식별한다는 URI는 큰 개념(자원 자체를 식별하는 방법)

![image-20210706170908168](HTTP web.assets/image-20210706170908168.png)

- URL(Resource Locator) : Resource의 위치
- URN(Resource Name) : Resource의 이름

![image-20210706171012476](HTTP web.assets/image-20210706171012476.png)

- URN은 말 그대로 자원의 이름이라서 거의 URL을 사용하게 됩니다.

![image-20210706171049426](HTTP web.assets/image-20210706171049426.png)

- Resource : URI로 식별할 수 있는 **모든 것**
- Identifier : 식별자

![image-20210706171137486](HTTP web.assets/image-20210706171137486.png)

- URL : 리소스가 있는 위치를 지정

- URN : 리소스에 이름을 부여

  - 위치는 변할 수 있지만, 이름은 변하지 않는다.

  - isbn이 대표적인 예
  - URN 이름만으로 실제 리소스를 찾을 수 있는 방법이 보편화 되지 않음

- **앞으로 URI를 URL과 같은 의미로 이야기하겠음**

- URL 분석

![image-20210706171420167](HTTP web.assets/image-20210706171420167.png)

![image-20210706171506230](HTTP web.assets/image-20210706171506230.png)

- 스키마(scheme) : 프로토콜 정보
  - 프로토콜 : 어떤 방식으로 자원에 접근할 것인가 하는 약속 규칙
  - http는 80포트, https는 443 포트를 주로 사용(포트는 생략 가능)
  - https는 http에 보안추가 (HTTP Secure)

![image-20210706171611576](HTTP web.assets/image-20210706171611576.png)

- userinfo : URL에 사용자정보를 포함하는 경우 사용
  - 거의 사용하지 않음

![image-20210706171730322](HTTP web.assets/image-20210706171730322.png)

- 호스트명

![image-20210706171802184](HTTP web.assets/image-20210706171802184.png)

- 포트

![image-20210706171810806](HTTP web.assets/image-20210706171810806.png)

- 패스 : 리소스의 경로
  - 보통 계층적구조로 되어있다.
  - 예시
    - /home/file1.jpg
    - /members
    - /members/100, /items/iphone12

![image-20210706171825954](HTTP web.assets/image-20210706171825954.png)

- query
  - key=value의 형태
  - ?로 시작 &로 추가 가능
    - ?`keyA=valueA`&`keyB=valueB`
  - query parameter, query string 등으로 불림.

![image-20210706172204743](HTTP web.assets/image-20210706172204743.png)

- frangment
  - html 내부 북마크 등에 사용
  - 서버에 전송되는 정보는 아님

![image-20210706172214265](HTTP web.assets/image-20210706172214265.png)

### 2.2. 웹 브라우저 요청 흐름

![image-20210706172320610](HTTP web.assets/image-20210706172320610.png)

- 먼저 google.com의 IP주소를 찾기 위해서 DNS서버를 조회하게 됩니다.
- 포트정보는 https가 적혀져 있으므로 생략가능합니다
- 그러면 이제 HTTP 요청 메시지가 생성됩니다.

![image-20210706172352942](HTTP web.assets/image-20210706172352942.png)

- HTTP 요청 메시지 생성
  - [메서드] /[패스]?[쿼리정보] [HTTP버전정보] [호스트]

![image-20210706172447567](HTTP web.assets/image-20210706172447567.png)

![image-20210706172552699](HTTP web.assets/image-20210706172552699.png)

![image-20210706172654537](HTTP web.assets/image-20210706172654537.png)

![image-20210706172703247](HTTP web.assets/image-20210706172703247.png)

- 이 패킷을 인터넷 망으로 던지고 수많은 노드를 통해서 목적지에 도착하게 됩니다.

![image-20210706172729282](HTTP web.assets/image-20210706172729282.png)

- 서버에서 응답 메시지를 생성
  - Content-Type : 데이터의 형식(html) 언어는 UTF-8로 캐릭셋이 되어있다
  - Content-Length : 실제 데이터의 길이

![image-20210706172809953](HTTP web.assets/image-20210706172809953.png)

![image-20210706172917730](HTTP web.assets/image-20210706172917730.png)

![image-20210706172923603](HTTP web.assets/image-20210706172923603.png)

- html 데이터를 까서 우리에게 보여주게 됩니다.

![image-20210706173019884](HTTP web.assets/image-20210706173019884.png)

## 3. HTTP 기본

![image-20210706204628211](HTTP web.assets/image-20210706204628211.png)

### 3.1. HTTP

- HyperText Transfer Protocol
- 모든 것이 HTTP : HTTP 메시지에 모든 것을 전송
  - HTML, TEXT
  - IMAGE, 음성, 영상, 파일
  - JSON, XML(API)
  - 거의 모든 형태의 데이터 전송 가능
  - 서버간에 데이터를 주고 받을 때도 대부분 HTTP 사용
  - **지금은 HTTP 시대!**
- HTTP의 역사
  - HTTP/1.1 : 가장많이 사용하는 버전.

![image-20210706204909942](HTTP web.assets/image-20210706204909942.png)

- 기반 프로토콜
  - HTTP/1.1 HTTP/2는 TCP기반에서 작동(TCP자체가 빠른 프로토콜이 아니기 때문)
  - HTTP/3은 UDP기반에서 작동(UDP에 맞춰 나온 프로토콜이 HTTP/3이라고 생각하면 됨)
  - 현재 HTTP/1.1 주로 사용

![image-20210706205043014](HTTP web.assets/image-20210706205043014.png)

- HTTP 특징
  - 클라이언트 서버 구조
  - 무상태 프로토콜(스테이스리스), 비연결성
  - HTTP 메시지
  - 단순함, 확장 가능

### 3.2. 클라이언트 서버 구조

- HTTP는 클라이언트가 HTTP요청을 보내고 무작정 대기하고 응답이 오면 응답을 열어서 동작을 하게 됩니다.(클라이언트와 서버가 분리)
  - 비즈니스로직, 데이터는 서버에 밀어넣고, UI,UX부분을 클라이언트에 집중하면 서버와 클라이언트 각각 독립적으로 진화가 가능하게 됩니다.

![image-20210706205454071](HTTP web.assets/image-20210706205454071.png)

### 3.3. 무상태 프로토콜(Stateless)

- HTTP의 특징 중 하나는 무상태 프로토콜을 지향한다는 겁니다.
- 서버가 클라이언트의 **상태를 보존X**
- 이를 위해 먼저 예시를 들어서 차이를 확인해봅니다. 먼저 상태를 유지함(Stateful)

![image-20210706210039999](HTTP web.assets/image-20210706210039999.png)

![image-20210706210111353](HTTP web.assets/image-20210706210111353.png)

![image-20210706210206124](HTTP web.assets/image-20210706210206124.png)

- 무상태(Stateless)

![image-20210706210324369](HTTP web.assets/image-20210706210324369.png)

![image-20210706210419502](HTTP web.assets/image-20210706210419502.png)

- 고객이 필요한 정보를 중간에 계속 넘겨주기 때문에 중간에 점원이 바뀌어도 문제가 생기지 않는다.
  - 갑자기 고객이 증가해도 점원을 대거 투입할 수 있다.
  - 갑자기 클라이언트 요청이 증가해도 서버를 대거 투입할 수 있다.
- 무상태는 응답 서버를 쉽게 바꿀 수 있다. => 무한한 서버 증설이 가능

![image-20210706210611378](HTTP web.assets/image-20210706210611378.png)

- 상태유지(Stateful) : 항상 같은 서버가 유지 되어야 한다.

![image-20210706210751811](HTTP web.assets/image-20210706210751811.png)

- 무상태(Stateless) : 아무 서버나 호출해도 된다.
  - 스케일 아웃 - 수평 확장 유리(장비를 확 늘려버리는 것이 가능해짐)

![image-20210706210906330](HTTP web.assets/image-20210706210906330.png)

![image-20210706211112453](HTTP web.assets/image-20210706211112453.png)

- Stateless도 한계가 존재합니다.
  - 로그인과 같이 상태를 유지해야하는 경우 => 브라우저 쿠키와 서버 세션등을 사용해서 상태를 유지

![image-20210706211125730](HTTP web.assets/image-20210706211125730.png)

### 3.4. 비연결성(Connectionless)

- 기본적으로 TCP/IP는 연결을 유지

![image-20210706211334716](HTTP web.assets/image-20210706211334716.png)

- 이 와중에 클라2가 접속요청을해도 클라이언트1과의 연결또한 유지가 됩니다.

![image-20210706211413528](HTTP web.assets/image-20210706211413528.png)

![image-20210706211424152](HTTP web.assets/image-20210706211424152.png)

- 연결을 유지하지 않는 모델

![image-20210706211446627](HTTP web.assets/image-20210706211446627.png)

![image-20210706211451472](HTTP web.assets/image-20210706211451472.png)

![image-20210706211506693](HTTP web.assets/image-20210706211506693.png)

![image-20210706211514369](HTTP web.assets/image-20210706211514369.png)

- 서버가 유지하는 자원을 최소한으로 유지할 수 있게됩니다.
- HTTP는 기본적으로 연결을 유지하지 않는모델입니다.

![image-20210706211600799](HTTP web.assets/image-20210706211600799.png)

![image-20210706211723132](HTTP web.assets/image-20210706211723132.png)

![image-20210706211902525](HTTP web.assets/image-20210706211902525.png)

![image-20210706211950934](HTTP web.assets/image-20210706211950934.png)

![image-20210706212038544](HTTP web.assets/image-20210706212038544.png)

### 1.5. HTTP 메시지

- 모든 것이 HTTP다 ! 지금은 HTTP 시대!
- HTTP 요청메시지와 응답메시지는 약간 차이가 있습니다.

![image-20210706212320356](HTTP web.assets/image-20210706212320356.png)

![image-20210706212344411](HTTP web.assets/image-20210706212344411.png)

![image-20210706212500697](HTTP web.assets/image-20210706212500697.png)

- 시작라인
  - request-line / status-line
  - request-line = method SP(공백) request-target(패스) SP HTTP-version CRLF(엔터)

![image-20210706212534631](HTTP web.assets/image-20210706212534631.png)

- HTTP 메서드

![image-20210706212705410](HTTP web.assets/image-20210706212705410.png)

![image-20210706212747094](HTTP web.assets/image-20210706212747094.png)

![image-20210706212803130](HTTP web.assets/image-20210706212803130.png)

- 응답 메시지
  - status-line = HTTP-version SP status-code SP reason-phrase CRLF

![image-20210706212821261](HTTP web.assets/image-20210706212821261.png)

![image-20210706212929288](HTTP web.assets/image-20210706212929288.png)

![image-20210706213044184](HTTP web.assets/image-20210706213044184.png)

![image-20210706213150794](HTTP web.assets/image-20210706213150794.png)

![image-20210706213310772](HTTP web.assets/image-20210706213310772.png)

## 4. HTTP 메서드

![image-20210706220737746](HTTP web.assets/image-20210706220737746.png)

### 4.1. HTTP API를 만들어보자

- 명세에 회원 정보 관리 API를 만들라는 요청이 있을 때

![image-20210706220807702](HTTP web.assets/image-20210706220807702.png)

![image-20210706220834952](HTTP web.assets/image-20210706220834952.png)

![image-20210706221033578](HTTP web.assets/image-20210706221033578.png)

![image-20210706221041259](HTTP web.assets/image-20210706221041259.png)

- 리소스는 '회원등록'이 아니라 '회원'이라는 것 자체가 리소스입니다.

![image-20210706221052126](HTTP web.assets/image-20210706221052126.png)

![image-20210706221158198](HTTP web.assets/image-20210706221158198.png)

![image-20210706221221185](HTTP web.assets/image-20210706221221185.png)

![image-20210706221309726](HTTP web.assets/image-20210706221309726.png)

![image-20210706221400672](HTTP web.assets/image-20210706221400672.png)

- URI는 리소스만 식별
- 리소스와 해당 리소스를 대상으로 하는 행위를 분리ㅣ
  - 리소스 : 회원
  - 행위 : 등록, 삭제, 조회, 변경
- 행위(메서드)는 어떻게 구분?

### 4.2. HTTP메서드 - GET, POST

- HTTP메서드는 클라이언트가 서버에 요청을 할 때 뭔가 기대하는 행동
- HTTP 메서드 종류(주요 메서드)
  - GET : 리소스 조회
  - POST : 요청 데이터 처리, 주로 등록에 사용
  - PUT : 리소스를 대체, 해당 리소스가 없으면 생성
  - PATCH : 리소스 부분 변경
  - DELETE : 리소스 삭제
- 기타 메서드
  - HEAD : GET과 동일하지만 메시지 부분을 제외하고, 상태 줄과 헤더만 반환
  - OPTIONS : 대상 리소스에 대한 통신 가능 옵션(메서드)을 설명(주로 CORS에서 사용)
  - CONNECT : 대상 자원으로 식별되는 서버에 대한 터널을 설정
  - TRACE : 대상 리소스에 대한 경로를 따라 메시지 루프백 테스트를 수행

- GET
  - 리소스 조회
  - 서버에 전달하고 싶은 데이터는 query(쿼리 파라미터, 쿼리 스트링)를 통해서 전달
  - 메시지 바디를 사용해서 데이터를 전달할 수 있지만, 지원하지 않는 곳이 많아서 권장하지 않음

![image-20210706222100518](HTTP web.assets/image-20210706222100518.png)

- POST
  - 클라이언트에서 서버에 요청을 보낼 때 내가 데이터를 줄테니 너가 이 데이터를 처리해줘라는 것
  - 요청 데이터 처리
  - 메시지 바디를 통해 서버로 요청 데이터 전달
  - 서버는 요청 데이터를 처리
    - 메시지 바디를 통해 들어온 데이터를 처리하는 모든 기능을 수행한다.
  - 주로 전달된 데이터로 신규 리소스 등록, 프로세스 처리에 사용

![image-20210706222443712](HTTP web.assets/image-20210706222443712.png)

- POST 요청 데이터를 어떻게 처리한다는 뜻일까??
  - POST 메서드는 대상 리소스가 리소스의 고유 한 의미 체계에 따라 요청에 포함 된 표현을 처리하도록 요청합니다.(???)
  - POST기능의 예시를 확인하는게 이해가 빠릅니다.
  - HTML 양식에 입력 된 필드와 같은 데이터 블록을 데이터 처리 프로세스에 제공
    - HTML FORM에 입력한 정보로 회원 가입, 주문 등
  - 게시판, 뉴스 그룹, 메일링 리스트, 블로그 또는 유사한 기사 그룹에 메시지 게시
    - 게시판 글쓰기, 댓글 달기
  - 서버가 아직 식별하지 않은 새 리소스 생성
    - 신규 주문 생성
  - 기존 자원에 데이터 추가
    - 한 문서 끝에 내용 추가하기
  - 결국 이 리소스 URI에 POST요청이 오면 요청 데이터를 어떻게 처리할지 리소스마다 따로 정해줘야 한다.(정해진 것이 없음)
- 정리
  - 새 리소스를 생성, 등록
  - 요청 데이터를 처리
  - 다른 메서드로 처리하기 애매한 경우

![image-20210706223457397](HTTP web.assets/image-20210706223457397.png)

### 4.3 HTTP 메서드 - PUT, PATCH, DELETE

- PUT
  - **리소스를 대체**
    - 리소스가 있으면 '완전히' 대체
    - 리소스가 없으면 생성
    - 쉽게 이야기해서 덮어쓰기
  - **클라이언트가 리소스를 식별**
    - **클라이언트가 리소스 위치를 알고** URI 지정
    - POST와 차이점

![image-20210707141038591](HTTP web.assets/image-20210707141038591.png)

- PUT은 기존의 리소스를 수정하는 것이 아니라 '대체'한다고 생각해야 합니다. 그렇다면 수정은 뭘까..?
- PATCH
  - **리소스 부분 변경**

![image-20210707141309762](HTTP web.assets/image-20210707141309762.png)

- DELETE
  - 리소스 제거

![image-20210707141347870](HTTP web.assets/image-20210707141347870.png)

---

### 4.4. HTTP 메서드의 속성

![image-20210707141503428](HTTP web.assets/image-20210707141503428.png)

- 안전(Safe)

  - 호출해도 리소스를 변경하지 않는다.(GET은 안전하다고 볼 수 있다.)

  - Q. 그래도 계속 호출하다가 로그 같은게 쌓여서 장애가 발생하면 ?

    A. 안전은 해당 리소스만 고려한다. 그런 부분까지는 고려x

- 멱등(Idempotent)

  - f(f(x)) = f(x)
  - 한 번 호출하든 두 번 호출하든 100번 호출하든 결과가 똑같다.(GET은 멱등하다.)
  - 멱등 메서드
    - GET : 한 번 조회하든, 두 번 조회하든 같은 결과가 조회
    - PUT : 결과를 대체, 따라서 같은 요청을 여러번 해도 최종 결과는 같다.
    - DELETE : 결과를 삭제한다. 같은 요청을 여러번 해도 삭제된 결과는 똑같다.
    - POST : 멱등이 아니다! 두 번 호출하면 같은 결제가 중복해서 발생할 수 있다.

  - 활용
    - 자동 복구 메커니즘
    - 서버가 TIMEOUT 등으로 정상 응답을 못주었을 때, 클라이언트가 같은 요청을 다시 해도 되는가에 대한 판단 근거

  - Q. 재요청 중간에 다른 곳에서 리소스를 변경해버리면?

    - 사용자1 : GET -> username: A, age: 20
    - 사용자2 : PUT -> username: A, age: 30
    - 사용자1 : GET -> username: A, age: 30(사용자2의 영향으로 바뀐 데이터 조회)

    A. 멱등은 외부 요인으로 중간에 리소스가 변경되는 것 까지는 고려하지 않는다.(동일한 사용자가 여러번 요청하는 부분에 대해서 고려한다고 생각하면 될 듯)

- 캐시가능(Cacheable)
  - 응답 결과 리소스를 캐시해서 사용해도 되는가?
  - GET, HEAD, POST, PATCH 캐시가능(스펙상)
  - 실제로는 GET, HEAD 정도만 캐시로 사용
    - POST, PATCH는 본문 내용까지 캐시 키로 고려해야 하는데, 구현이 쉽지 않음

---

## 5. HTTP 메서드 활용

![image-20210707142728196](HTTP web.assets/image-20210707142728196.png)

### 5.1. 클라이언트에서 서버로 데이터 전송

- ''쿼리 파라미터''를 통한 데이터 전송
  - GET
  - 주로 정렬 필터(검색어)
- ''메시지 바디''를 통한 데이터 전송
  - POST, PUT, PATCH
  - 회원가입, 상품주문, 리소스 등록, 리소스 변경

---

- 클라에서 서버로 데이터를 전송하는 4가지 상황
  - 정적 데이터 조회
    - 이미지, 정적 텍스트 문서
  - 동적데이터 조회
    - 주로 검색, 게시판 목록에서 정렬 필터(검색어)
  - HTML Form을 통한 데이터 전송
    - 회원 가입, 상품 주문, 데이터 변경
  - HTTP API를 통한 데이터 전송
    - 회원 가입, 상품 주문, 데이터 변경
    - 서버 TO 서버, 앱 클라이언트, 웹 클라이언트(Ajax)

- 정적 데이터 조회

  - 쿼리 파라미터 미사용

  ![image-20210707143103029](HTTP web.assets/image-20210707143103029.png)

  - 이미지, 정적 텍스트 문서
  - 조회는 GET 사용
  - 정적 데이터는 일반적으로 쿼리 파라미터 없이 리소스 경로로 단순하게 조회 가능

- 동적 데이터 조회

  - 쿼리 파라미터 사용

  ![image-20210707143231740](HTTP web.assets/image-20210707143231740.png)

  ![image-20210707143405387](HTTP web.assets/image-20210707143405387.png)

- HTML Form 데이터 전송

  - POST 전송 - 저장

  ![image-20210707143726717](HTTP web.assets/image-20210707143726717.png)

  - GET 전송 - 저장

  ![image-20210707143825095](HTTP web.assets/image-20210707143825095.png)

  - GET전송 - 조회

  ![image-20210707143932518](HTTP web.assets/image-20210707143932518.png)

  - multipart/from-data 파일을 전송하기 위한 form

  ![image-20210707144027822](HTTP web.assets/image-20210707144027822.png)

  ![image-20210707144212688](HTTP web.assets/image-20210707144212688.png)

- HTTP API 데이터 전송

  ![image-20210707190225011](HTTP web.assets/image-20210707190225011.png)

  ![image-20210707190236308](HTTP web.assets/image-20210707190236308.png)

  - HTML에서 Form전송 대신 자바 스크립트를 통한 통신에 사용(AJAX)

### 5.2. HTTP API 설계 예시

![image-20210707190703792](HTTP web.assets/image-20210707190703792.png)

- 회원관리 시스템
  - /members를 하나의 컬렉션이라고 합니다.
  - 회원수정은 생각해야할 부분입니다. PUT은 기존의 내용을 덮어버리는 것, PATCH는 부분적인 수정 => 일반적으로 수정은 PATCH를 사용합니다.
  - 게시글 수정의 경우에는 수정한 전체 내용을 보내니까 PUT을 사용하기도 합니다.

![image-20210707190833722](HTTP web.assets/image-20210707190833722.png)

- POST - 신규 자원 등록 특징
  - 클라가 리소스 URI를 모른다
    - POST /members
  - 서버가 새로 등록된 리소스 URI를 생성
  - 컬렉션(Collection)
    - 서버가 관리하는 리소스 디렉토리
    - 서버가 리소스의 URI를 생성하고 관리
    - 여기서 컬렉션은 /members

![image-20210707191429582](HTTP web.assets/image-20210707191429582.png)

- 파일 관리 시스템
  - 파일등록

![image-20210707191802760](HTTP web.assets/image-20210707191802760.png)

- PUT
  - 클라가 리소스 URI를 알고 있어야 한다
    - PUT /files/star.jpg
  - 클라가 직접 생성될 리소스 URI를 생성
  - 스토어(Store)
    - 클라이언트가 관리하는 리소스 저장소
    - 클라이언트가 리소스의 URI를 알고, 관리
    - 여기서 스토어는 /files

![image-20210707192001419](HTTP web.assets/image-20210707192001419.png)

- HTML FORM 사용
  - HTML FORM은 GET, POST만 지원
  - AJAX 같은 기술을 사용해서 해결 가능
  - 여기서는 순수 HTML, HTML FORM 이야기
  - GET, POST만 지원하므로 제약이 있음

![image-20210707192443617](HTTP web.assets/image-20210707192443617.png)

![image-20210707193335226](HTTP web.assets/image-20210707193335226.png)

![image-20210707195107386](HTTP web.assets/image-20210707195107386.png)

![image-20210707195206445](HTTP web.assets/image-20210707195206445.png)

- 문서
- 컬렉션
- 스토어
- 컨트롤러(controller), 컨트롤 URI
  - 문서, 컬렉션, 스토어로 해결하기 어려운 추가 프로세스 실행
  - 동사를 직접 사용
  - /members/{id}/delete

## 6. HTTP 상태코드

![image-20210707213614174](HTTP web.assets/image-20210707213614174.png)

- 1xx(Informational) : 요청이 수신되어 처리중
  - 거의 사용하지 않으므르 생략
- 2xx(Successful) : 요청 정상 처리
- 3xx(Redirection) : 요청완료를 위해 추가 행동이 필요
- 4xx(Cllient Error) : 클라이언트 오류, 잘못된 문법등으로 서버가 요청을 수행할 수 없음
- 5xx(Server Error) : 서버 오류, 서버가 내부 오류 등으로 정상적으로 요청 처리를 하지 못함

![image-20210707213835028](HTTP web.assets/image-20210707213835028.png)

### 6.1. 2xx(Successful)

> 클라이언트의 요청을 성공적으로 처리

- 200 OK 

![image-20210707214625655](HTTP web.assets/image-20210707214625655.png)

- 201 Created

![image-20210707214639652](HTTP web.assets/image-20210707214639652.png)

- 202 Accepted

![image-20210707214752833](HTTP web.assets/image-20210707214752833.png)

- 204 No Content

![image-20210707214835329](HTTP web.assets/image-20210707214835329.png)

---

### 6.3. 3xx(Redirection)

> 요청을 완료하기 위해 유저 에이전트(웹 브라우저)의 추가 조치 필요

- 웹 브라우저는 3xx 응답의 결과에 Location 헤더가 있으면, Location 위치로 자동 이동한다.(리다이렉트)
- 예시 : /event를 썼다가 다음 이벤트에서 /new-event를 만들었는데 사용자가 /event로 들어오는 경우, 응답으로 301 Moved Permanently로 주면 자동 리다이렉트가 되어서 다시 새로 요청을 보내게 됩니다.

![image-20210707215644613](HTTP web.assets/image-20210707215644613.png)

- 리다이렉션의 종류로는 영구 리다이렉션, 일시 리다이렉션, 특수 리다이렉션이 있습니다

![image-20210707215912440](HTTP web.assets/image-20210707215912440.png)

- 영구 리다이렉션(301, 308)

  ![image-20210707220048898](HTTP web.assets/image-20210707220048898.png)

  - 리소스의 URI가 영구적으로 이동
  - 원래의 URL를 사용x, 검색 엔진 등에서도 변경 인지
  - 301 : 리다이렉트 요청 메서드가 GET으로 변하고, 본문이 제거될 수 있음

  ![image-20210707220231610](HTTP web.assets/image-20210707220231610.png)

  - 308 : 301과 기능은 같으나 리다이렉트시 요청 메서드와 본문을 유지함

  ![image-20210707220443411](HTTP web.assets/image-20210707220443411.png)

- 일시적인 리다이렉션(302, 307, 303)

  ![image-20210707220731790](HTTP web.assets/image-20210707220731790.png)

  - 리소스의 URI가 일시적으로 변경
  - 따라서 검색 엔진 등에서 URL을 변경하면 안됨
  - 302 Found : 리다이렉트시 요청 메서드가 GET으로 변하고, 본문이 제거될 수 있음
  - 307 Temporary Redirect : 302와 기능은 같으나 리다이렉트 요청 메서드와 본문 유지
  - 303 See Other : 302와 기능은 같음. 리다이렉트시 요청 메서드가 GET으로 변경

- PRG : Post / Redirect / Get(일시적인 리다이렉션)

  - POST로 주문후에 웹 브라우저를 새로고침하면?
  - 새로고침은 다시 요청이기 때문에 중복 주문이 될 수 있다.

![image-20210707221250042](HTTP web.assets/image-20210707221250042.png)

![image-20210707221257623](HTTP web.assets/image-20210707221257623.png)

![image-20210707221504120](HTTP web.assets/image-20210707221504120.png)

![image-20210707221603776](HTTP web.assets/image-20210707221603776.png)

![image-20210707221617652](HTTP web.assets/image-20210707221617652.png)

![image-20210707221834669](HTTP web.assets/image-20210707221834669.png)

![image-20210707221945662](HTTP web.assets/image-20210707221945662.png)

- 기타 리다이렉션(300, 304)

  - 304 Not Modified : 캐시를 목적으로 사용. 클라이언트에게 리소스가 수정되지 않았음을 알려준다. 따라서 클라이언트는 로컬PC에 저장된 캐시를 재사용한다.(캐시로 리다이렉트 한다.)

    따라서 304 응답은 응답에 메시지 바디를 포함하면 안된다.(로컬 캐시를 사용해야 하므로)

    조건부 GET, HEAD 요청시 사용

![image-20210707222145210](HTTP web.assets/image-20210707222145210.png)

- 300 Multiple Choices
- 301 Moved Permanently
- 302 Found
- 303 See Other
- 304 Not Modified
- 307 Temporary Redirect
- 308 Permanent Redirect

---

### 6.4. 4xx(Client Error), 5xx(Server Error)

![image-20210707222439593](HTTP web.assets/image-20210707222439593.png)

![image-20210707222619089](HTTP web.assets/image-20210707222619089.png)

![image-20210707222801788](HTTP web.assets/image-20210707222801788.png)

![image-20210707222947053](HTTP web.assets/image-20210707222947053.png)

![image-20210707223015122](HTTP web.assets/image-20210707223015122.png)

![image-20210707223145724](HTTP web.assets/image-20210707223145724.png)

![image-20210707223238965](HTTP web.assets/image-20210707223238965.png)

![image-20210707223254913](HTTP web.assets/image-20210707223254913.png)

5xx는 왠만하면 만들면 안됩니다. 정말로 서버가 문제가 생겼을 때 5xx가 나오도록 만들어야 합니다.