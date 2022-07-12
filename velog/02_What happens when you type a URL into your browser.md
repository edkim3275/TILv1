# [CS] What happens when you type a URL in the browser and press enter?

> **브라우저에 www.google.com을 입력했을 때, 어떤 일이 벌어지는지 설명해주세요.** 라는 면접 단골질문이 있는데 이에 대해서 먼저 생각이 난 키워드는 `URL`, `도메인`, `IP주소` 였다. 
>
> URL(U..? Resource Location)는 어떠한 리소스의 위치를 가리키는 것이기 때문에, 주소창에 무언가를 검색한다는 것은 무언가에 대한 '위치'를 인풋값으로 넣는 것이고, 해당하는 위치에 내가 찾는 무언가가 존재한다면 유저는 브라우저로부터 그것을 결과로 받게된다.
>
> 가 내가 생각한 답변이지만. 보다 명확히 이해해보기위해서 공부를 시작해보자. :pencil2:

웹페이지가 어떻게 불러와지는지 순서대로 정리를 해보자.

**1. www.google.com을 브라우저 주소창에 친다.**

**2. Browser는 캐싱된 DNS 기록들을 통해 www.google.com에 대응되는 IP주소가 있는지 확인한다.**

DNS(Domain Name System)는 URL들의 이름과 IP주소를 저장하고 있는 데이터베이스이다. 인터넷에 있는 모든 URL들에는 고유의 IP 주소가 지정되어있다. 이 IP주소를 통해서 해당 웹사이트를 호스팅하고있는 서버 컴퓨터에 접근을 할 수 있다. 예를들어, www.google.com의 IP주소를 알아보기 위해서는 `nslookup www.google.com`을 터미널에 작성하면 내가 접근이 가능한 해당 사이트의 IP주소를 알려준다.

![image-20220712230212273](02_Whay happens when you type a URL into your browser.assets/image-20220712230212273.png)

> 여기서 권한 없는 응답(non-authoritative answer)이란, name 서버가 도메인에서 만든 원본 소스 파일을 갖고 있지 않다는 뜻이다. 이 서버에는 다른 DNS들에서 얻어진 도메인의 파일을 캐싱형태로 갖고 있는 것이다.

DNS의 가장 큰 목적은 사람들에게 편리함을 주기 위해서이다. 사람들이 웹사이트 주소에 쉽게 접속할 수 있게 매핑을 해주는 역할을 한다. 

웹사이트 이름을 브라우저에 검색하면 브라우저는 DNS 기록을 4가지의 캐시에서 확인을 한다.

1. 가장 먼저 *브라우저 캐시*를 확인한다. 브라우저는 일정기간 동안(유저가 이전에 설정한)의 DNS 기록들을 저장하고 있다. DNS query가 이 곳에서 가장 먼저 실행이 된다.
2. 브라우저는 *OS 캐시*를 확인한다. 브라우저 캐시에 웹사이트 이름의 IP주소가 발견되지 않았다면, 브라우저는 systemcall을 통해서 OS가 저장하고 있는 DNS 기록들의 캐시에 접근한다.
3. 그 다음에는 *router 캐시*를 확인한다. 컴퓨터에 DNS 기록을 찾지 못하면 브라우저는 DNS 기록을 캐싱하고 있는 router와 통신을 해서 찾으려고 한다.
4. 그래도 못 찾는다면 마지막으로 *ISP 캐시*를 확인한다. ISP는 DNS 서버를 구축하고 있고 브라우저가 마지막으로 DNS 기록이 있기를 바라며 접근하게 된다.

왜 이렇게 많은 곳에서 캐시들을 저장하는가? 개인정보를 생각했을 때 정보가 여기저기에 캐싱된게 불편할 수 있지만, 캐시는 네트워크 트래픽을 조절하고 데이터 전송 시간을 줄이기 위해 매우 중요하다.

**3. 요청한 URL이 캐시에 없으면, ISP의 DNS 서버가 www.google.com을 호스팅하고 있는 서버의 IP 주소를 찾기 위해 DNS query를 날린다.**

www.google.com에 접속하고 싶으면 IP주소를 반드시 알아야 한다. DNS query의 목적은 여러 다른 DNS 서버들을 검색해서 해당 사이트의 IP 주소를 찾는 것이다. 이러한 검색을 `recursive search`라고 부른다. IP주소를 찾을 때까지 DNS 서버에서 다른 DNS 서버를 오가면서 반복적으로 검색하던지 못 찾아서 에러가 발생할 때까지 검색을 진행한다.

이 상황에서, ISP의 DNS 서버를 `DNS recursor`라고 부르고, 인터넷을 통해 다른 DNS 서버들에게 물어물어 도메인 이름의 올바른 IP주소를 찾는데 책임을 갖고 있다. 다른 DNS 서버들은 `name server`라고 불린다. 이들은 웹사이트 도메인 이름의 구조에 기반해서 검색을 하기 때문이다.

**4. Browser가 서버와 TCP connection을 한다.**

브라우저가 올바른 IP주소를 받게 되면 서바와 connection을 빌드하게 된다. 브라우저는 인터넷 프로토콜을 사용해서 서버와 연결이 된다. 인터넷 프로토콜의 종류는 여러가지가 있지만, 웹사이트의 HTTP 요청의 경우에는 일반적으로 TCP를 사용한다.

클라이언트와 서버간 데이터 패킷들이 오가려면 TCP connection이 되어야 한다. `TCP/IP three-way handshake`라는 프로세스를 통해서 클라이언트와 서버간 connection이 이루어지게 된다. 단어 그대로 클라이언트와 서버가 SYN과 ACK메세지들을 가지고 3번의 프로세스를 거친 후에 연결이 된다.

1. 클라이언트 머신이 SYN 패킷을 서버에 보내고 connection을 열어달라고 물어본다.
2. 서버가 새로운 connection을 시작할 수 있는 포트가 있다면 SYN/ACK 패킷으로 대답한다.
3. 클라이언트는 SYN/ACK 패킷을 서버로부터 받으면 서버에게 ACK 패킷을 보낸다.

이 과정이 끝나면 TCP connection이 완성된다.

**5. Browser가 웹 서버에 HTTP 요청을 한다.**

TCP로 연결이 되었다면, 데이터를 전송하면 된다.

클라이언트의 브라우저는 GET 요청을 통해 서버에서 www.google.com 웹페이지를 요구한다. 요청을 할 때 비밀 자료들을 포함하던지, form을 제출하는 상황에서는 POST 요청을 사용할 수도 있다. 이 요청을 할 때 다른 부가적인 정보들도 함께 전달이 된다.

- browser identification(User-Agent 헤더)
- 받아들일 요청의 종류(Accept 헤더)
- 추가적인 요청을 위해 TCP connection 유지를 요청하는 connection 헤더
- 브라우저에서 얻은 쿠키 정보
- 등등

**6. 서버가 요청을 처리하고 response를 생성한다.**

서버는 웹서버를 가지고 있다.(Apache, IIS ...). 이들은 브라우저로부터 요청을 받고 request handler한테 요청을 전달해서 요청을 읽고 response를 생성하게 된다. request handler란 ASP.NET, PHP, Ruby 등으로 작성된 프로그램을 의미한다. 이 request handler는 요청과 요청의 헤더, 쿠키를 읽어서 요청이 무엇인지 파악하고 필요하면 서버에 정보를 업데이트 한다. 그 다음에 response를 특정한 포맷으로(JSON, XML, HTML) 작성한다.

**7. 서버가 HTTP response를 보낸다.**

서버의 response에는 요청한 웹페이지, status code, compression type(Content-Encoding) - 어떻게 인코딩 되어 있는지, 어떻게 피이지를 캐싱할지(Cache-Control), 설정할 쿠키가 있다면 쿠키, 개인정보 등이 포함된다.

status code란 현재 response의 상태를 의미하고 총 5가지 종류가 있다.

- 1xx : 정보만 담긴 메시지라는 것
- 2xx : response가 성공적이라는 것
- 3xx : 클라이언트를 다른 URL로 리다이렉트함
- 4xx : 클라이언트 측에서 에러가 발생했음
- 5xx : 서버 측에서 에러가 발생했음

**8. Browser가 HTML content를 보여준다.**

브라우저는 HTML content를 단계적으로 보여준다. 처음에는 HTML의 스켈레톤(기본 틀)을 렌더링한다. 그 다음에는 HTML tag들을 체크하고 나서 추가적으로 필요한 웹페이지 요소들(이미지, CSS, 스타일시트, Javascript 파일 등)을 GET으로 요청한다. 이 정적인 파일들은 브라우저에 의해 캐싱이 돼서 나중에 해당 페이지를 재방문할 때 다시 서버로부터 불러와지지 않도록 한다. 그 다음에 비로소 www.google.com의 모습이 보이게 된다.

참고

https://devjin-blog.com/what-happen-browser-search/