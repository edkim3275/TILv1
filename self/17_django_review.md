# Django_review

- 번외

윈도우 bash창에서 $ code .bashrc 누르고 시작

bashrc에는 git관련 설정들을 넣어줄수가 있다. 평소에 쓰던 명령어를 단축어로 만들어서 사용을 할 수 있다.

alias pyvenv='python -m venv venv' 하고나서 모두 끄고 다시 code를 열고 터미널에 pyvenv친다면??

venv 형성됨

![image-20210317184534644](17_django_review.assets/image-20210317184534644.png)

![image-20210317184609819](17_django_review.assets/image-20210317184609819.png)

- 기본세팅

- 앱 -> 모델

  제일처음해야 할거는 모델생성

  ![image-20210317185759903](17_django_review.assets/image-20210317185759903.png)

  urlpattern까지만 있으면 makemigrations가 가능해진다.

- .gitignore

  ![image-20210317190159903](17_django_review.assets/image-20210317190159903.png)

  /가있으면 일반적으로 디렉토리, 폴더로 명시하고 없다면 일반적으로 파일을 의미

- ![image-20210317192134151](17_django_review.assets/image-20210317192134151.png)

  render에 실제경로작성

  redirect name spacing이용하여 발생시킬 url의 님넥임을 작성

- ![image-20210317192753999](17_django_review.assets/image-20210317192753999.png)

- ![image-20210317193026567](17_django_review.assets/image-20210317193026567.png)

  위 두개의 차이. ModelForm은 Model과 연관이 있고, Form은 모델과 관련이 없다.

  중간에 BaseModel폼이 들어간다 ![image-20210317193437958](17_django_review.assets/image-20210317193437958.png)

  





- create.html

  ![image-20210317195712226](17_django_review.assets/image-20210317195712226.png)

- views.py
  - created

![image-20210317195914927](17_django_review.assets/image-20210317195914927.png)

- 