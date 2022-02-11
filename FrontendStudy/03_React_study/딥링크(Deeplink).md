\#52e4dc

# 딥링크(Deeplink)

http 혹은 https로 시작하는 인터넷 주소는 모두 특정 서비스의 웹 페이지로 이동한다.

모바일 앱에서도 이와 유사한 기능을 하는 것이 존재하는데. 그것이 바로 딥링크(Deeplink)

딥링크는 특정 주소 혹은 값을 입력하면 **앱이 실행되거나 앱 내 특정 화면으로 이동시키는 기능**을 수행.

즉, 딥링크가 사용되면 광고에 반응한 이용자는 앱이 바로 실행되어 특정 화면으로 이동하는 경험을 하게된다. 혹은 앱 설치 후 실행화면 특정 화면으로 바로 이동하게 된다.(지연된 딥링크)

## 딥링크 방식

딥링크는 3가지 방식으로 구분됨

- URI 스킴 방식 : 앱에 URI 스킴(scheme) 값을 등록하여 딥링크 사용
- 앱링크(App Link) : Android 제공 - 도메인 주소를 이용한 딥링크 사용
- 유니버셜 링크(Universal Link) : iOS 제공 - 도메인 주소를 이용한 딥링크 사용

### 'URI Scheme'방식의 딥링크

가장 일반적으로 사용되는 딥링크 방식은 URI Scheme(URI 스킴) 방식

URI 스킴을 이용한 딥링크는 앱에 Scheme 값을 등록하는 형태로 앱을 구분한다. 스킴은 앱마다 등록할 수 있는 값으로 "특정 스킴값을 호출하면 특정 앱이 오픈된다."라는 약속을 실행한다. 예를들어 트위터 앱을 오픈하고자 한다면 twitter:// 라는 스킴값을 이용하면 된다. 이 스킴값은 앱 개발시 효율적인 앱 오픈을 위해 자체적으로 개발사에서 자신들만의 값으로 등록하게 된다.

앱 내에서의 특정 페이지는 'path'값으로 구분. 예를들어 트위터 앱의 회원가입 페이지를 오픈하고자 한다면 twitter://signup 이라는 값을 사용.

정리하면, URI 스킴 방식은 `Scheme://Path`라는 두개의 요소로 구성된다.

- `Scheme://Path`
- Scheme = 앱을 특정함(ex : 트위터)
- Path = 앱 내 페이지를 특정함(ex : 트위터 내 회원가입 페이지)

안드로이드의 경우 아래와 같이 `Androidmanifest.xml`이라는 파일에 스킴값을 등록.

```xml
<activity android:name=".MainActivity" android:launchMode="singleTask">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="mychat" android:host="deeplink"/>
    </intent-filter>
</activity>
```

[위 코드에서 `android:scheme`라고 적힌 항목이 스킴값 => mychat://deeplink가 딥링크로 설정된 것]

iOS의 경우 앱 정보 화면에서 URL Scheme 항목에 스킴값을 입력할 수 있다.

:grey_exclamation: URI 스킴 방식의 한계

앱의 수가 상대적으로 적었던 시기에 URI 스킴방식은 앱을 바로 실행시키기게 훌륭한 수단이었으나. 앱의 수가 늘어나게되면서 중복된 스킴값을 사용하는 앱들이 등장하기 시작한다.

구글플레이, OneStore, 삼성앱스토어 등의 오픈 마켓들이 marker:// 란 스킴 값을 사용하기 때문에 사용자가 선택해야하는 상황이 벌어지게 됨.

이러한 문제에 대한 고민끝에 나오게 된 것이 유니버셜 링크(iOS 제공)와 앱링크(Android 제공)

### 유니버셜 링크와 앱링크

**웹페이지 주소를 사용한 딥링크**

위의 문제에 대해서 개발자들은 도메인(Domain) 주소를 딥링크 실행값으로 사용하기로 결정. 예를들어 스마트폰 브라우저 앱 주소창에 http://naver.com을 입력하면 네이버 앱이 바로 오픈되어 사용할 수 있도록 한 것.

바로 이 기능을 iOS에서는 유니버셜 링크(Universal Link), Android에서는 앱링크(App Link)라고 부른다.

참고자료 1 : *[[Add Android App Links]](https://developer.android.com/studio/write/app-link-indexing.html)*

참고자료 2 : *[[Universal Links for Developers]](https://developer.apple.com/ios/universal-links/)*

안드로이드의 경우 `Androidmanifest.xml`라는 파일에서 아래와 같이 앱링크 도메인을 등록할 수 있다.

(아래 예시는 애드브릭스 트랙킹 링크의 유니버셜 링크, 앱링크 연동을 기준으로 작성)

```xml
<activity android:name=".MainActivity" android:launchMode="singleTask">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    <!-- 스킴 딥링크 -->
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="adbrixrm" android:host="main"/>
    </intent-filter>
    <!-- 안드로이드 앱링크 -->
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="voilw1qss0yxo1mes7swxg.adtouch.adbrix.io" />
    </intent-filter>
</activity>
```

iOS의 경우 Singing & Capabilities 에서 Associated Domains에서 등록할 수 있다.

:grey_exclamation: 유니버셜 링크와 앱링크의 한계

안타깝게도 유니버셜 링크와 앱링크또한 아직까지 완전하지는 않다. 모든 앱에서 유니버셜 링크와 앱링크 오픈을 지원하는 것이 아니기 때문.

앱링크는 구글에서 만든 앱에서만 동작하고, 구글 이외에 앱에서는 정상적으로 동작하지 않는다. 유니버셜 링크 역시 애플에서 만든 앱 이외에는 정상적으로 동작하지 않는다.

**앱링크 테스트 결과**

![image-20220211154110972](/home/myounjunkim/.config/Typora/typora-user-images/image-20220211154110972.png)

**유니버셜 링크 테스트 결과**

![image-20220211154205008](/home/myounjunkim/.config/Typora/typora-user-images/image-20220211154205008.png)