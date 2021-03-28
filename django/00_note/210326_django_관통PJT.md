# 관통PJT

- GIT을 사용하는 2가지 이유

  버전관리, 협업

![image-20210326090558281](210326_django_관통PJT.assets/image-20210326090558281.png)

좌 : 원격저장소, 우 : 로컬저장소

git push, pull 서로하기전에 양쪽에서 수정한 경우

양쪽에서 둘다 . 만 써서 양쪽둘다 커밋을 한다면??

![image-20210326090716091](210326_django_관통PJT.assets/image-20210326090716091.png)

`$git log --oneline`해보면 양측간의 history가 달라짐을 알 수 있다

![image-20210326091020979](210326_django_관통PJT.assets/image-20210326091020979.png)

`$git push origin master`를 해보면

![image-20210326091224208](210326_django_관통PJT.assets/image-20210326091224208.png)

이 상황을 git pull해서 해결해보려고하는데 `git pull`을 해보면

![image-20210326091532275](210326_django_관통PJT.assets/image-20210326091532275.png)

<<와 >> 그리고 == 으로 구분이 되어있는 상태

![image-20210326091640888](210326_django_관통PJT.assets/image-20210326091640888.png)

![image-20210326092214987](210326_django_관통PJT.assets/image-20210326092214987.png)

![image-20210326092430431](210326_django_관통PJT.assets/image-20210326092430431.png)

이번에는 revert를 해보겠스빈다

![image-20210326092503318](210326_django_관통PJT.assets/image-20210326092503318.png)

과거돌이가기 reset, 실제 내용만 과거의 내용으로 고치는 것이 revert

---

![image-20210326092925467](210326_django_관통PJT.assets/image-20210326092925467.png)

![image-20210326093133656](210326_django_관통PJT.assets/image-20210326093133656.png)

![image-20210326093146167](210326_django_관통PJT.assets/image-20210326093146167.png)

스위치라는 결국 head가 가리키는 방향을 변경해주는 것

![image-20210326094431461](210326_django_관통PJT.assets/image-20210326094431461.png)

---

웹엑스 시간

AUTH

![image-20210326130559036](210326_django_관통PJT.assets/image-20210326130559036.png)

signup login logout

review - article

comment - 댓글

---

