# Authentication

- bash

  ![image-20210322224153818](README.assets/image-20210322224153818.png)

  ```bash
  $vim .bashrc
  ```

  ![image-20210322224351983](README.assets/image-20210322224351983.png)

  원하는 작업을 한 후에 `:wq!`를 누르면 저장후 나가기

  ```bash
   $vim .gitconfig
  ```

  ![image-20210322224906864](README.assets/image-20210322224906864.png)

  ![image-20210322224922619](README.assets/image-20210322224922619.png)

  ```bash
  $git config --global user.name
  $git config --global user.email
  ```

  여기서 설정해준것이 gitconfig에 들어가 있다.

---

```bash
$python manage.py startapp accounts
```

내부적으로 django가 account라는 이름을 참고를 하기 때문에 accounts로 통일한다. 

settings.py에 출생신고 후 마스터앱에서 경로 지정

![image-20210322225420301](README.assets/image-20210322225420301.png)

가장 처음 배운것은 login에 관한 것. 거꾸로 생각해보는 방식으로 배워봅시다.

서비스 구성을할 건데 회원을 관리하고 싶은 상황

1. 회원목록관리 DB에서 관리 => model 에서 관리를 했었습니다 => user의 경우에는 조금 특별했습니다. model을 따로 만드는 것이 아니라 django가 제공하는 model을 사용.

   DB => model => django가 제공

2. 페이지 - 회원가입, 로그인페이지가 필요한데 그 과정에서 사용자로부터 입력을 받아야해! => forms.py ModelForm => django가 제공하는 것을 쓰겠다.

## views.py

### login

```python
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    """
    POST : 실제 로그인을 진행
    GET : 로그인 페이지를 랜더
    """
    if request.method == 'POST':
        pass
    else:
        form = 
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
```

![image-20210322230504244](README.assets/image-20210322230504244.png)

authentication에 관련된 form들이 모여있는 공간

- **`UserCreationForm`**

  ![image-20210322230944139](README.assets/image-20210322230944139.png)

![image-20210322230651368](README.assets/image-20210322230651368.png)

django 내부의 User라는 Model이 존재하는데 우리는 이 User라는 모델을 그대로 가져오는 것이 아니라

![image-20210322230716689](README.assets/image-20210322230716689.png)

`get_user_model()`을 사용해서 가져오게 될 것입니다.

![image-20210322230845910](README.assets/image-20210322230845910.png)

usercreation과정에서 save()를 사용할 것이고 return값(user)가 있다.

- **`AuthenticationForm`**

  ![image-20210322231040847](README.assets/image-20210322231040847.png)

  forms.Form을 받고있고, ModelForm이 아니기 때문에 class Meta부분(Model과의 연결부분)이 없다.

  ![image-20210322231210327](README.assets/image-20210322231210327.png)

  authentication과정에서 get_user()를 사용할 것이고 return값이 있다.

  함수 내부적으로 사용하고 있는 user_cache라는 곳에 user내용이 담기게 되고 그 것을 return하게 된다.

- `Authentication` vs `Authorization`

  Authentication(인증) : 서버가 봤을 때 누군지 모르는 상태이기 때문에 너 누구야? 하는과정

  Authorization(권한) : 서버가 누구인지는 알지만 너가 권한있는지 체크해봐야해 하는 과정