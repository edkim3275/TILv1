# django

김준호 교수님

4주간 장고를 배울겁니다!

![image-20210308090203940](16_django.assets/image-20210308090203940.png)

## 지난시간

![image-20210308090222590](16_django.assets/image-20210308090222590.png)

![image-20210308090230036](16_django.assets/image-20210308090230036.png)

![image-20210308090241155](16_django.assets/image-20210308090241155.png)

![image-20210308090255155](16_django.assets/image-20210308090255155.png)

![image-20210308090306544](16_django.assets/image-20210308090306544.png)

![image-20210308090336218](16_django.assets/image-20210308090336218.png)

![image-20210308090350535](16_django.assets/image-20210308090350535.png)

## 이번시간

![image-20210308090505507](16_django.assets/image-20210308090505507.png)

## django란..?

![image-20210308090537366](16_django.assets/image-20210308090537366.png)

다이나믹을 알기전에 스태틱 웹을 한번 봅시다

### Static web

![image-20210308090553099](16_django.assets/image-20210308090553099.png)

서버에 미리 사용자에게 보여질것들이 준비가 되어있고 사용자가 들오면 그것을 그대로 보여주는 웹.(어떠한 데이터처리가 이루어지지 않고 미리 준비 되어있는 것들을 보여주는 웹
)

### Dynamic web

![image-20210308090643443](16_django.assets/image-20210308090643443.png)

사용자의 요청에 따라 서버에서 작업읍 한 뒤에 사용자에게 제공되는 웹

이들을 만들어주는 프레임워크 중 하나가 django라는 프레임워크입니다.

![image-20210308090813575](16_django.assets/image-20210308090813575.png)

요청과 응답

서버 프레임워크를 django로 구축을할 것.

### What? Why? How?

> 파이썬으로 만들어진 웹 프레임워크 언어

![image-20210308090908894](16_django.assets/image-20210308090908894.png)

#### What

![image-20210308090931612](16_django.assets/image-20210308090931612.png)

![image-20210308090937022](16_django.assets/image-20210308090937022.png)

![image-20210308091014066](16_django.assets/image-20210308091014066.png)

![image-20210308091037316](16_django.assets/image-20210308091037316.png)

프레임워크 위에서 조금더 원활히 작업하도록 도와주는 프로그램

![image-20210308091106928](16_django.assets/image-20210308091106928.png)

#### Why

![image-20210308091118498](16_django.assets/image-20210308091118498.png)

![image-20210308091141840](16_django.assets/image-20210308091141840.png)

이름만 들어도 아는 세계적 기업들이 django를 사용한다 = django가 대규모 서비스에서도 충분히 잘 돌아가는 웹 프레임워크다!

![image-20210308121356395](16_django.assets/image-20210308121356395.png)

방대한 생태계! 또한 django를 사용하는 이유

![image-20210308091346429](16_django.assets/image-20210308091346429.png)

#### How

![image-20210308091443172](16_django.assets/image-20210308091443172.png)

![image-20210308091520808](16_django.assets/image-20210308091520808.png)

각각의 디자인패턴(MVC)

![image-20210308091605110](16_django.assets/image-20210308091605110.png)

django는 MTV방식(Model, Template, View)

![image-20210308091639101](16_django.assets/image-20210308091639101.png)

각각의 역할은

Model : 데이터베이스 관린

Template : 레이아웃(화면)

View : 중심 컨트롤러(심장)

![image-20210308091747323](16_django.assets/image-20210308091747323.png)

view가 model로부터 데이터를 받고 처리를해서 하나의 문서를 만들어서 http 응답을 보낸다

![image-20210308091903109](16_django.assets/image-20210308091903109.png)

## hello django

![image-20210308091954192](16_django.assets/image-20210308091954192.png)

- 수업에 앞서서 주소확인!

  ![image-20210308092124814](16_django.assets/image-20210308092124814.png)

### 장고설치

![image-20210308092327334](16_django.assets/image-20210308092327334.png)

환경확인(현재 환경에 다운받아져있는 패키지들 확인 가능)

![image-20210308092441460](16_django.assets/image-20210308092441460.png)

![image-20210308092508523](16_django.assets/image-20210308092508523.png)

버전이 3.1 이상이면 ok!

### 장고규칙(앱생성, 등록)

> url -> view.py -> template 흐름으로 작성

![image-20210308103123610](16_django.assets/image-20210308103123610.png)

- `django-admin startproject 프로젝트이름`

  ![image-20210308092623631](16_django.assets/image-20210308092623631.png)

  ![image-20210308092638321](16_django.assets/image-20210308092638321.png)

  아무것도 뜨는건 없다. 하지만 우리가 사용하는 폴더에 firstpjt라는 폴더가 만들어져 있을 것

  이 폴더 안으로 들어와보면 firstpjt랑 manage.py라는 파일이 있습니다. 지금 이 위치에서 다시한번 git bash를 켜보고 django서버를 on해봅시다.

- `python manage.py runserver`

  ![image-20210308092839196](16_django.assets/image-20210308092839196.png)

  python으로 manage.py라는 파일을 열건데 runserver라는 키워드가 붙어있다라는 의미

  - 만약 안된다면?????

    ctrl+c로 서버를 끈다음에 vscode로 열어주세요. 

    같은 명령어를 vscode에 작성해보면 됩니다.

  ![image-20210308093129008](16_django.assets/image-20210308093129008.png)

  이렇게 뜨면 ok!!

- 사용금지

  `` `, `_`, `내장함수이름` 등은 사용하면 안됩니다.

- `python manage.py startapp 앱의이름`

  ![image-20210308094041225](16_django.assets/image-20210308094041225.png)

  아무것도 에러는 뜨지않고

  ![image-20210308094104346](16_django.assets/image-20210308094104346.png)

  이처럼 좌측에 article라는 폴더가 생성됨

- admin.py는 관리를 하는 정보를 담은 파이썬파일

- apps.py는 절대로 수정하지 않는다

- models.py MTV(디자인패턴)중 model을 담당하는 파일

- test.py는 django의 테스트코드를 작성하는 곳. 정규수업에는 사용x

- views.py 이자인 패턴 3대장중 하나. MTV중 View의 역할을 하는 파일.

  - 우리가 만질 파일은 3가지!

    ![image-20210308094420168](16_django.assets/image-20210308094420168.png)

  - template은 조금 이따가 배울겁니다.

- 장고는 어플이 만들어져도 프로젝트입장에서는 어플리케이션이 만들어졌는지 알수 없습니다. 그렇기 때문에 어플리케이션을 만들었다는 '등록'과정을 거쳐야 합니다.

  firstpjt열고 settings.py 열어보면

  ![image-20210308094629172](16_django.assets/image-20210308094629172.png)

  django가 기본적으로 구동되는 데 필요한 기능을 하고있는 어플리케이션이 미리 등록이 되어있는 것

  우리가 만든것은 articles라는 앱이기 때문에 여기에 어플이름을 등로갷주면 됩니다.

  ![image-20210308094730487](16_django.assets/image-20210308094730487.png)

  articles를 밑에 두어도 상관은 없으나 일반적으로 위에 두게된다.

  ![image-20210308094818471](16_django.assets/image-20210308094818471.png)

local apps -> 3rd-party apps -> django apps 이러한 순서로 installed apps를 작성해주는 편입니다. 

​	![image-20210308094936282](16_django.assets/image-20210308094936282.png)

​	**trailing comma** 마지막 요소 뒤쪽에 콤마를 붙여준다.

- 하나의프로젝트에는 여러개의 작은 로컬프로젝트가 들어갈 수 있습니다. 

- setting.py에서..

  ![image-20210308100315344](16_django.assets/image-20210308100315344.png)

  이렇게 변경후 `python manage.py runserver` 명령어 입력을 해보면

  ![image-20210308100411729](16_django.assets/image-20210308100411729.png)

  서버 언어가 한글로 변경이 됩니다.

  - 시간대도 변경해봅시다.

  검색해서 database time zones에서 국제적약속을 확인해보면.. 

  ![image-20210308100513691](16_django.assets/image-20210308100513691.png)

  이러한 형식으로 작성을한다

  ![image-20210308100537486](16_django.assets/image-20210308100537486.png)

  작성을 하면 나중에 데이터베이스에 저장되어 출력되는 시간이 우리나라 시간기준에 맞춰집니다.

- .py 3대장 (중요하게 생각하면 됩니다.)

1. urls.py
2. views.py
3. models.py

### 요청-응답 사이클 경험해보기

요청을 가장 먼저 받는곳은 URLS(urls.py)입니다. 이러한 요청이 들어오면 어디로가야하는지 인식하고 적절한 함수를 찾아서 그 함수를 호출합니다. 이 역할을 urls.py에서 합니다.

`urls.py`는 `project`에 위치합니다. 

![image-20210308100853855](16_django.assets/image-20210308100853855.png)

기본적으로 admin/ 라는 주소가 들어가있는데 주소창에 이렇게 쳐보면

![image-20210308100916097](16_django.assets/image-20210308100916097.png)

![image-20210308100929583](16_django.assets/image-20210308100929583.png)

이미 admin이라는 주소가 생성되어있습니다. 기본적으로 django가 제공해주는 url

- 메인페이지로 들어오기위한 url을 작성

  `path('index/', )

  path함수의 2번째 인자는 어떤 View를 실행할지가 들어오게 됩니다.

  ![image-20210308101154872](16_django.assets/image-20210308101154872.png)

  

  articles앱에 `views.py`로가서 views함수들이 하나씩 작성이 되는 겁니다.

  **view함수의 첫번째인자는 반드시 `request`여야만 합니다. **

  request는 사용자로부터 받아온 요청

  ```python
  def index(request):  # 첫 번째 인자는 반드시 request
      return render(request, '템플릿경로')
  ```

  근데 템플릿은 일단 없습니다

  

  다시 urls.py로 돌아와서 articles 앱에 있는 views.py를 가져옵니다.

  ![image-20210308101745281](16_django.assets/image-20210308101745281.png)

  그리고나서 views.py의 index 함수를 사용한 것

  ![image-20210308101807414](16_django.assets/image-20210308101807414.png)

  그렇다면 views.py의 index함수가 실행되어 보여줄 템플릿이 보여지게되는것

  ![image-20210308101851883](16_django.assets/image-20210308101851883.png)

  이제 템플릿을 작성해봅시다. 템플릿은 앱에다가 작성을하는데 **약속이 하나 더 있습니다**. **템플릿은 반드시`templates`라는 폴더의 경로에서 만들어줘야합니다.**

  ![image-20210308102008885](16_django.assets/image-20210308102008885.png)

  articles 안에 `templates`라는 폴더를 만들고 그안에 `index.html`파일을 하나 만들어 놓습니다.(일반적으로 메인페이지는 index라는 이름을 사용합니다.)

  **django는 `templates`까지의 경로는 알고있다. 따라서 그 이후의 경로만 작성해주면 됩니다!!**

  ![image-20210308102205391](16_django.assets/image-20210308102205391.png)

![image-20210308102215912](16_django.assets/image-20210308102215912.png)

![image-20210308102632864](16_django.assets/image-20210308102632864.png)

### Template

![image-20210308102753924](16_django.assets/image-20210308102753924.png)

우리에게 보여지는 화면을 **표현하기위한 로직**을 작성하는 부분(데이터조작x 데이터조작은 view에서 합니다.)

DTL이라는 장고 템플릿에서 사용하는 언어가 따로 존재합니다.

#### DTL

![image-20210308102842532](16_django.assets/image-20210308102842532.png)

python이 html에 사용되는 것이아니라 python처럼 비슷한 구조라고 생각하면 됩니다. (파이썬이 실행되는 것은 아님)

#### DTL syntax

일단 작성순서는 url -> view.py -> template 흐름으로 작성

![image-20210308103015917](16_django.assets/image-20210308103015917.png)

##### `Variable`

![image-20210308103743181](16_django.assets/image-20210308103743181.png)

![image-20210308103807381](16_django.assets/image-20210308103807381.png)

- `urls.py`에서 실행할 함수와 연결해주기

  ![image-20210308103246019](16_django.assets/image-20210308103246019.png)

  이러면 에러가 뜨는데

  ![image-20210308103301904](16_django.assets/image-20210308103301904.png)

  이것은 아직 함수를 만들어주지않았기 때문에 당연한것

  

  `views.py`로 돌아와서 함수를 만들어줍니다

  ![image-20210308103442157](16_django.assets/image-20210308103442157.png)

  views.py에서 전달해야하는 그것은 세번째 인자로 들어가게됩니다. 딕셔너리 형태로.

  ![image-20210308103525946](16_django.assets/image-20210308103525946.png)

  views함수가 하나의 템플릿을 만들건데 {}내의 데이터와 함께 들어가게 될 것

  

  `templates`폴더에 `greeting.html`을 만들어주면서 데이터에 접근하기위해 key값을 활용합니다

  ![image-20210308103927583](16_django.assets/image-20210308103927583.png)

  

  좀 더 활용해봅시다. views.py에서

  ![image-20210308104304093](16_django.assets/image-20210308104304093.png)

  웬만하면 key, value값은 맞춰서 보내는 것이 일반적입니다.

  왼쪽의 key값들은 greeting.html 라는 장고 템플릿에서 사용하게 됩니다.

  이제 greeting.html로 돌아가서

  ![image-20210308104416658](16_django.assets/image-20210308104416658.png)

  ![image-20210308104524317](16_django.assets/image-20210308104524317.png)

  ![image-20210308104532657](16_django.assets/image-20210308104532657.png)

  이중 하나에 접근하고 싶다면?? 리스트의 경우에는 인덱스로 접근하게 됩니다.

  ![image-20210308104607848](16_django.assets/image-20210308104607848.png)

##### Filter

![image-20210308104804783](16_django.assets/image-20210308104804783.png)

앞에있는 변수를 수정해줄때 사용해줍니다. django built in filters에서 확인가능

서로 나열이 되는 필더라면 chain이 가능 30자 까지 제한을 걸어줄 수도 있다.



이번에는 저녁데이터를 받아와 봅시다

우선 url에서 요청을 받아와서 view를 불러옵니다.

![image-20210308110549490](16_django.assets/image-20210308110549490.png)

templates폴더에 `dinner.html` 을 만들어줍니다.

![image-20210308111008039](16_django.assets/image-20210308111008039.png)

이렇게 작성하면 아래와 같이 보여집니다. length와 같은 함수는 django built in filters에서 확인가능

![image-20210308110754763](16_django.assets/image-20210308110754763.png)



![image-20210308111000270](16_django.assets/image-20210308111000270.png)

##### tag

![image-20210308111152094](16_django.assets/image-20210308111152094.png)

단독적으로 쓰는tag도 있지만 열린태그와 닫는태그가 존재하는 tag또한 있습니다.

![image-20210308111422990](16_django.assets/image-20210308111422990.png)

```html
{% for iterator in iterators %}
	<li>{{ food }}</li>
{% endfor %}
```

tag는 출력은 되지 않습니다.

##### Comments

![image-20210308111832502](16_django.assets/image-20210308111832502.png)

```django
{# 이것은 주석입니다 #}
{% comment %}
	<p>1</p>
{% endcomment %}
```

### 정리

오후시간 : 탬플릿 상속

- app 이름은 ''**복수형**''으로 맞춰서 사용
- app은 **생성(startapp) 후 등록**

## 웹엑스시간

- 웹서버, 소프트웨어를 만드는 이유? 쓸려고, 편하려고! 다양한 사람이 사용하기 위해서 나혼자 쓰려고?? ㄴㄴ 다 같이 쓰려고
- 프로젝트구성 project route

웹서비스는? 남들이 쓰기 위해서. 다른방법은 없느냐? 있다! 앱스토어에서 받는 어플 같은것들 하지만 웹을 왜 쓰느냐?? 무엇보다 쉽다. 다른사람에게 효용을 주기 원활하다. 

![image-20210308124135658](16_django.assets/image-20210308124135658.png)

우리가 지금 배우는건 *부분(특정, 다른 컴퓨터에서 data 받아오기(다운로드)) 즉, 내컴퓨터가 아닌 다른 컴퓨터에서 받아오기

수많은 주소들 중에서 127.0.0.1 이라는 것이 있는데 이것은 바로 '나' 를 의미한다.

우리 컴퓨터는 서버가 되본적이 없다(즉 남에게 줘본적이없다.) 지금부터 누구에게 주고싶다! 라고 한다면 남에게 주는 순간 서버가 된다.

![image-20210308124521926](16_django.assets/image-20210308124521926.png)

내 컴퓨터가 남에게 주기위해서 안달이 난 상태인데 생태계는 반드시 요청을 받아야 응답을 보내줄 수가있다.

IP주소는 까여도 된다.(사실 클릭한번으로 보여지는것이 주소) 문제는 현관문이 열리질 않아야 한다. 즉, 다른 사람이 요청보내는것에 응답을 보내면 안된다

![image-20210308124832757](16_django.assets/image-20210308124832757.png)

이 상황은 내가 클라이언트면서 내가 서버인 상황. 어쨌든 요청을 보낼때 필요한 것은 컴퓨터주소(IP.../.../..)인데 그러면 google.com....은 뭔가? 도메인으로 불리는 이것은 사람들에게 통용되는 주소. 즉, IP는 필수지만 도메인은 없을 수도없다.

즉, 서버에 접근하기위해서는 IP로 접근을해야하고 IP뒤에는 port라는 것이 숨어있습니다.

기본적으로 모든 IP뒤에는 port가 붙어있습니다. 

컴퓨터 하나에 요청을 보낼수있는 창구가 하나라면 너무 답답할 것. 다른 용도로 사용되는 창구들이 존재합니다. 이러한 모든 문들을 'port'라고 합니다.

![image-20210308125653357](16_django.assets/image-20210308125653357.png)

IP는 주소 port는 창구 이 두가지가 있어야만 접근할 수 가 있습니다. 

접근 방법생각해보면

![image-20210308125817566](16_django.assets/image-20210308125817566.png)

밖에 네트워크에 요청을 보내고 그 네트워크에서 다시 내컴에 요청을 보내는 경우. 이것은 다른 네트워크에서 내게 요청을 보낼때 block당함

두번쨰로

![image-20210308125850393](16_django.assets/image-20210308125850393.png)

![image-20210308125940818](16_django.assets/image-20210308125940818.png)

창구의 번호는 내가 지정하는 것. 

aws 에져 gcp가 부동산 임대업하는 곳인데

![image-20210308130614899](16_django.assets/image-20210308130614899.png)

내 컴퓨터가 아닌 서버에서 원하는 작업을 하고싶은데 서버에서 내가 빌린 임대한 곳은 현재  텅 빈상태. 근데 또 내 컴퓨터에 존재하는것은 침대, 소파 등등.. 너무 많은 것들 중에서 그 중에서 카페에 필요한 물건들이 섞여져있다. 그렇다면 이중에 서버에서 필요한 것들은 뭔지 어떻게 고를 것인가.  너무 어렵다. 내 집에있는 모든 것들을 카페에 다 가져갈 수는 있지만 그러는 사람은 없을 것이다.

![image-20210308130913726](16_django.assets/image-20210308130913726.png)

이중에서 어케 골라내 ㅎㄷㄷ;

그래서 필요한 프로젝트가 있을때마다 그 환경에서 필요한 것들만 뽑아내어서 사용한다. 이것을 파이썬에서 '가상환경venv(virtual environment)'이라고 한다.

![image-20210308131149343](16_django.assets/image-20210308131149343.png)

핵심은 프로젝트마다 다른 가상의 파이썬pip을 구축해서 사용하겠다.

하나의 프로젝트는 하나의 가상환경(1pjt == 1venv == 1git repo)

![image-20210308131431707](16_django.assets/image-20210308131431707.png)

### 해봅시다

![image-20210308132016665](16_django.assets/image-20210308132016665.png)

프로젝트는 각각의 파이썬이 필요합니다.

![image-20210308132227170](16_django.assets/image-20210308132227170.png)

파이썬아 venv(가상환경) venv(폴더명)를 만들어줘

![image-20210308132333605](16_django.assets/image-20210308132333605.png)

아직 파이썬 위치를 물어보면??

![image-20210308132403415](16_django.assets/image-20210308132403415.png)

그대로 나온다. 파이썬 위치를 물어보면 가상환경을 말하기로 아직 안정해줬기때문

`source venv/Scripts/activate` 를 하게 되면 활성화!

![image-20210308132539148](16_django.assets/image-20210308132539148.png)

이제 이 터미널은 venv안의 파이썬을 보겠다는 명명이다! 맥의 경우 `source venv/bin/activate`

![image-20210308132658819](16_django.assets/image-20210308132658819.png)

이제부터 글로벌의 파이썬이 아니라 가상환경의 파이썬을 가져오게 된다. pip list를 활용해보면 

![image-20210308132804177](16_django.assets/image-20210308132804177.png)

깔끔해집니다.

![image-20210308133604264](16_django.assets/image-20210308133604264.png)

위치확인해보는거고

![image-20210308133649377](16_django.assets/image-20210308133649377.png)

![image-20210308134403284](16_django.assets/image-20210308134403284.png)



반드시 ignore를 만들어서(venv와 같은 층에다가) 다시 한번 `source venv/Scripts/activate` 를 해줘야한다.



앞으로 뭔가 좀 이상하다 싶으면

1. venv가 있나요(가상환경이 활성화 되어있나요)

## Template 상속

![image-20210308142329081](16_django.assets/image-20210308142329081.png)



가장 먼저 기본이 되는 `base template`을 만들어 볼 것입니다.  지금까지는 `articles`라는 앱에 작성을 했습니다. 하지만 이번에는 프로젝트에서도 사용되도록 project에 만들어 봅시다.

`firstpjt`폴더에 `templates`폴더를 만들고 그안에 `base.html`파일을 만들어 봅시다.

bootstrap CDN을 가지고 온 후 block을 만들어 줍니다.

![image-20210308140836737](16_django.assets/image-20210308140836737.png)

![image-20210308141709012](16_django.assets/image-20210308141709012.png)

BASE_DIR / 'firstpjt' / 'templates'로 새로운 경로를 만들어준 것. 여기서 base_dir란 articles, firstpjt를 포함한 하나의 프로젝트를 의미한다. 절대경로의 시작점으로 지정해준 것.

![image-20210308141859781](16_django.assets/image-20210308141859781.png)



![image-20210308142612189](16_django.assets/image-20210308142612189.png)

표현과 로직을 분리해라! 표현 : 탬플릿(Template), 로직 : 뷰(View)



## HTML form

![image-20210308143153647](16_django.assets/image-20210308143153647.png)

![image-20210308143330503](16_django.assets/image-20210308143330503.png)

서버의 입장에서는 데이터의 키에 접근해야하는데 이 키값의 역할을 하는 것이 인풋 태그의 name속성

네이버를 보면

![image-20210308143521381](16_django.assets/image-20210308143521381.png)



## URL

![image-20210308151514181](16_django.assets/image-20210308151514181.png)

django는 URL의 dispatcher역할을 한다

## 웹엑스 시간

django PJT == Σapp(앱들의 모임)

python manage.py startapp : 폴더가 하나 생기는 것

INTRO는 프로젝트 그 안에 관련된 모든 폴더들 articles앱 intro앱 venv.... 이들은 모두 앱으로 보자! 다만 intro는 조금 특별하다. `settings.py`를 들고있다. `settings.py`를 들고 있는 폴더, 모든 앱중에서 가장 쌘 앱인 `master app`이라고 부르겠습니다.

![image-20210308165852644](16_django.assets/image-20210308165852644.png)

자 이제 `articles`라는 아기 앱을 만들었다. 해야할 것은??? 출생신고! 출생신고를 `settings.py` 33번째줄에 앱적기

![image-20210308170031857](16_django.assets/image-20210308170031857.png)

이제 `urls.py`를 훑어봅시다

![image-20210308170302945](16_django.assets/image-20210308170302945.png)

여기서 주목할 점은 `Function Views`, `Including another URLconf`부분



java - spring, python - django ... 이렇게 사용되는데 MVC

- design pattern이라는 것이 무엇이냐,.?

  SW공학에서 알고리즘이 개인 사격술이면 디자인패턴은 전략이라고 볼 수있다.  내가 총잘쏘고엄청 쌔면 그것이 알고리즘(개인능력)이라고한다면 디자인패턴은 전략(숲을보는개념, 설계적인 부분)

  그래서 design pattern이 무엇이냐

  ![image-20210308170948961](16_django.assets/image-20210308170948961.png)

  태초에 완전 처음에 길을 개척했다면 점점 많은 사람들이 가는 길이 생겼을 것. 

  ![image-20210308170905188](16_django.assets/image-20210308170905188.png)

  이렇게 많은 사람들이 겪어보니 가장 좋은 구조가 MTV(Model Template View), MVC 구조.

  해보니까 이건 이럴때 좋고, 저건 저럴때 좋더라~를 배우는 것

- 세상은 요청과 응답으로 이루어져있다. 

  ![image-20210308171329931](16_django.assets/image-20210308171329931.png)

  처음 요청을한것은 받아주는 부분이 바로 `urls.py` 저기요 저 뭐 하고싶은데 라는 요청이 들어오면 아 그거? 그거 저리로 가시면 됩니다.(포워딩)라는 기능

  ![image-20210308171514537](16_django.assets/image-20210308171514537.png)

  이렇게 되면 실제로 업무를 처리하는 곳에서 요청을 받게 되는데 그것이 `views.py` 야 뭐 하래라는 것이 들어오게되면 그 작업을 수행하고 일을 다 했으면 와 일 끝났다~ 가 아니라 '무조건' 응답을 해주는것(Response) 99%는 HTML로 응답한다.

  ![image-20210308171613658](16_django.assets/image-20210308171613658.png)

  ![image-20210308171733188](16_django.assets/image-20210308171733188.png)

  요청은 브라우저 주소창의 영역, 응답또한 브라우저의 영역
  우리가 할꺼는 urls.py와 views.py뿐

  

![image-20210308172550249](16_django.assets/image-20210308172550249.png)

​	무조건 여기에 있는 패키지에서  view라는 파일을 가져온다. 그리고나서 test함수를 실행한다.

​	![image-20210308172630749](16_django.assets/image-20210308172630749.png)

​	함수의 인자로서 들어오는 함수.

## 보충

django : DB를 불러와서 다른 사람에게 서비스를 할 수 있는 것들을 배워볼 것

우리가 알고있는 웹 프로토콜은 요청과 응답으로 구성되어있다. django에 들어오면서 요청에 들어오면서 가장 중요한것 1 url 2 method 이 두가지의 조합으로 요청이 간다. 응답은 html양식의 template으로 응답이 간다.

framework는 훈수를 남이 나한테 두는건데 그 훈수를 착착 들으면 좀 더 수월하게 웹을 구성할 수 있게 된다. 그러기 위해서는 조금의 암기가 필요하다. 그 framework중 하나가 django

- how?

  - django에서는 MTV(Model-Template-View) 디자인 패턴을 따르고 있다. 통상적으로는 MVC 구성

  - ![image-20210308184833216](16_django.assets/image-20210308184833216.png)
  - views.py : 어떤작업(특정동작)을 할지를 정하고 그것을 template에게 넘겨줘서 
  - template : 사용자에게 보여줄 것을 구성(표현)

- django프로젝트 시작을 위해서 필요한것??

  시작은 django라는 프로그램 `python -m venv venv`를 통해 가상환경을 형성을 하고 가상환경을 적용시켜서 글로벌이 아니라 부분적으로 사용하는 방식 `source venv/script/activate` 라는 명령어를 통해서 (venv)를 만들게 된다. 그렇게 되면

  ![image-20210308185418070](16_django.assets/image-20210308185418070.png)

  이런식으로 pip list가 비워진 상태가 된다. 이건 조만간 배울거임

  

  `python -m django startproject repeat_first_pjt`  또는 `django-admin startproject repeat_first_pjt`하면  이제 django를 만든것!

  vs code로 들어와서 `python manage.py runserver`를 하면 서버를 확인할 수 있게됨.

  ![image-20210308190610800](16_django.assets/image-20210308190610800.png)

  vs code에 들어가서 좌측상단을 보면 이제 django의 기본틀을 확인 할 수 있다.

  ![image-20210308190226739](16_django.assets/image-20210308190226739.png)

​	

​	프로젝트의 온갖 설정을 하는 `settings.py`

​	![image-20210308190324502](16_django.assets/image-20210308190324502.png)

​	![image-20210308190431747](16_django.assets/image-20210308190431747.png)

​	이런식으로 설정들을 변경할 수 있다. 위의 경우는 I18N(Internationaliztion국제화) L10N(Localization 현지화) USE_TZ(타임존을 사용할꺼냐 여부)

​	![image-20210308190709122](16_django.assets/image-20210308190709122.png)

에러페이지를 보기위한 DEBUG설정



이제 앱을 만들어봅시다

`python manage.py startapp articles` 명령어를 통해서 기능별로 여러가지 앱을 생성. 예를들어 유저관련정보, article, 영상, 판매광고 .. 이러한 기능별로 분류를 해서 작성을 하게된다.

이렇게 생성하면 까먹지말고 바로해야하는것은 등록! 장고관련한 파이썬 모듈들을 설치를 새로운 라이브러리를 등록하면 그것을 사용하는데 장고관련된 라이브러리를 3rd party app들로 구분해서 사용하게 됩니다 .

앱을 생성하고 들어가는것 

![image-20210308191108656](16_django.assets/image-20210308191108656.png)



그 다음은 앱에 관련된 urls.py를 만들어주는 것

**요청이 오면 main의 urls.py로 이동하게된다.** `urls.py`의 목적은 url과 views함수를 연결하는 것!

![image-20210308191355999](16_django.assets/image-20210308191355999.png)



![image-20210308191953292](16_django.assets/image-20210308191953292.png)

request와 template_name은 반드시 넘겨줘야하는 대상

Articles Index

- 2단계

  main url과 sub url로 넘기는 과정

  sub url에서 view함수에서 연결해서 view함수에서 template으로 넘겨주는 단계

- url 분리를 할때 include를 사용한다.

- 

## Review

![image-20210309010927701](16_django.assets/image-20210309010927701.png)

- `__ init __.py` : firstpjt디렉토리를 하나의 패키지로 인식할 수 있도록 해주는 것
- `asgi.py` : django3버전에서 새로 생긴 신생파일. 나중에 비동기적인 웹서버와 사용할때 사용하는데 우리는 안건들꺼임 
- `settings.py` : django 사이트 모든 설정을 포함하고 있는 파일. 우리가 만들 어플이 등록되거나, 파일들의 위치, DB세부사항, 보안관련 등 모두 여기에 저장되어있다.
- `urls.py` : 이것도 중요, requests 가장 먼저 만나는 친구. 사용자 요청을 가장 먼저 맞닿뜨리는 곳
- `wsgi.py` : asgi와 비슷한 역할. 배포할 때 도움을 주는 친구인데 지금은 사용 x

