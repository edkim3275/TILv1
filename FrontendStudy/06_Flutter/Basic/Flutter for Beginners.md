# Flutter for Beginners

> what we will learn in this course is not only the basics but also go from a complete beginner to being able to release our applications in apple's app store and google's play store.
>
> software engineers do not know all the answers you have to go and read documentation you have to practice practice practice and put time into it. countless countless hours you need to put into learning.

- vs code(IDE), firebase(backend), figma(design)

## 1. Developer Accounts

- developer account for apple and google. 기본적으로 개발한 앱을 애플스토어 혹은 구글플레이 스토어에 올리기위해서는 해당 플랫폼의 Developer account가 필요하다.

- every application needs to have an identifier(reverse domain identifier)

### iOS

- iOS - What is a dev account?

  what is a developer account and why we need it?

  - 애플, 구글에 등록하고 스토어에 deploy하기위한 리소스들을 얻기위함

-  iOS - Different dev accounts

  Individual / company (liability,책임)

  - 개인, 회사 계정 차이는 서비스에 대한 책임관련한 부분이 크다. 예를들어 어떤 사용자가 우리 서비스가 데이터를 부당한 곳에 사용하고, 불안전한 방식으로 보관한다고 생각할 경우, 혹은 데이터 저장 관련한 약관을 공개하지않고 저장을 하는 경우 사법문제가 발생할 수 있다.

  - 회사 계정의 경우 사용자에게 발생할 수 있는 손해에 대해 개인이 책임을 지거나 지지 않을 수 있다.(이번 course의 목표는 go through an application and create an application that can store users notes can be quiet personal)

  - personal company account

    you are personally liable for that company and you can also create a company that it's like an umbrella basically sits on top and then there are people who are directors of the company and etc. so you're not personally liable and that is the same structure that you can find it many other countries

  - How to register

    https://developer.apple.com/programs/enroll/

    ![image-20230125125909567](https://user-images.githubusercontent.com/77393619/215478336-4909bdb9-3067-4c34-a488-a654012c985f.png)

- iOS - D.U.N.S Number for organizations

  https://developer.apple.com/support/D-U-N-S/

  - organization account 생성할 경우 D.U.N.S라는 걸 세팅해야한다.
  - 기업신용정보 제공기관인 dun&bradstreet(D&B)로 부터 인증된 기관이여야만 organization account생성이 가능하다. 따라서 D&B로 부터 먼저 D.U.N.S number를 받아야함.

  - identifier for your company that you either have been assigned to already
  - 없을 경우 D&B 웹사이트에서 해당 기업이 DUNS number를 요청하여 그것을 받고 진행을 해야한다.

  - iOS의 경우

    organiazation account 생성시 본인 웹사이트가 없을 경우(혹은 웹사이트 도메인이 있더라도 콘텐츠가 없을 경우) 요청이 거절될 수 있다.

    you will need a hosting service or a domain provider(website) because they're not the same thing if you have a host and you have a domain provider it still doesn't mean that you have content on your web page.

- iOS - Long Process and not free

  This process sometimes can take weeks for organizations

  account 생성하기 까지 process 속도가 오래걸린다는 점을 유의하자.

- iOS - selling

  if you're registering and you want to well applications then you will have to provide some banking and tax information so they need to ensure that the stuff that you're selling in different countries the money that is then being sent to you bank account will be accounted for when you're paying your taxes

  so if you're trying to sell apps on the app store then you will have to fill in some forms with the u.s tax offices(Internal Revenue Service, IRS). have to send the forms to them then they will come back with some sort of identifier to you and then you will need to use that identifier on apple's website in order to basically say that yeah i know I'm selling stuff in the u.s I'm selling stuff in japan ... but I'm gonna pay taxes for them here in my country and that's what the forms says.

  ![image-20230125133002361](https://user-images.githubusercontent.com/77393619/215478363-40b94db3-e34c-4032-bf8b-5538efca05a4.png)

### Android

- playstore의 경우 apple보다는 간단하다.

  similar to App Store Connect for releasing Android apps

- Android - Sign up for dev account

  https://play.google.com/console/u/O/signup

  ![image-20230125133411310](https://user-images.githubusercontent.com/77393619/215478385-f4e2fa6f-253f-4f45-9377-26af36480e72.png)

  - when we actually submit our apps to app store and play store. there are a few key data points that you have to provide to both stores. one is a **privacy policy url** and the other one is a **support url**. and there are also two other emails you have to provide. the emails the first one is the **support email** and the other one is a **contact email**. and if you're if you're setting up a business account then i really suggest that you actually set up a website
  - developer account를 생성하기위해서 웬만하면 자신(회사)만의 웹사이트를 보유한 상태에서 생성하는 것이 좋다.

- flutter

  flutter can be deployed on a windows machine, macintosh or collectively called as desktop, web, android, ios five platforms.

  window환경에서는 iOS 서비스는 개발불가. it's just apple's fault for locking down their build systems and all their tools to macintosh so they haven't made the conscious decision to bring their tool system and tooling to windows or linux.

## 2. Setup

- install flutter

  Flutter is a rich **UI framework** developed by Google

- framework

  set of tools provided to you as a sortware developer so you can use to produce some output

- What is Dart

  Dart is the language that powers Flutter

- DartPad

  DartPad allows you to test your Dart code right in the browser

  https://dartpad.dev/?

- add path

  we need to expose flutter's binary files to our system

  flutter as an sdk or a toolkit or a framework it has a lot of bits and pieces of software in it and some of these bits are more important in that sense that they're actually executable in that on you computer.

  these are programs and flutter comes also with its own built-in programs.

- install xcode

- install Android Studio and Android SDK

  ios and android also provide you with sdk in order to write native applications. so we need to download android studio so we get acceess to the sdk manager and we can install an android sdk.

- extensions
  - Error Lens
  - Bracket Pair Colorizer
  - Flutter + Dart
  - bloc

## 3. Introduction to Dart

- Getting started

  ```bash
   $ flutter create project_name
  ```

- keywords

  https://dart.dev/guides/language/language-tour#keywords

- data types

  https://api.dart.dev/stable/2.14.4/dart-core/dart-core-library.html

- constants

  constant is value cannot be changed

  - compile-time constatnts vs. run-time constants

    writing program or running program. 

    compile is where you take the program that 

- functions

  hold your logic

## 4. Dart control statements and collections

- if & else

  ```dart
  const name = 'foo';
  if (name == 'foo') {
      print('yes this is foo');
  } else if (name == 'boo') {
      print('this is boo');
  } else {
      print('I don\'t know what this is');
      print("I don't know what this is");
  }
  ```

- operators

  prefix, infix,, suffix operators

  ```dart
  var age = 20;
  // infix : need two parameteres
  final halfOfAge = age / 2;
  final doubleTheAge = age * 2;
  // prefix : comes before whatever it has to do its work on
  // in this case it takes the value that comes after it. it decreases that value by one and then it return its result back to the left-hand side
  final ageMinusage = --age;
  ```

- Lists in Dart

  List of homogenous "things" lists are zero based.

  ```dart
  List<String> list1 = ['foo', 'bar', 'baz'];
  String foo = list1[0];
  final length = list1.length;
  list1.add('boo');
  ```

- Sets in Dart

  List of unique "things"

  ```dart
  final names = {'foo', 'bar', 'baz'};
  names.add('foo');
  print(names); // {foo, bar, baz}
  ```

- Maps in Dart

  Maps are used to hold key-value pairs of information

  ```dart
  const person = {
      'age': 20,
      'gender': 'male',
      'name': 'foo',
  };
  person['lastName'] = 'Kim';
  ```
## 5. Null-safety

concept that is available in most modern languages such as dart, rust, swift ... it is better to try to utilize it so that we can write better code.

- null value

  https://dart.dev/null-safety

  the concept of the absence of a value. variable can sometimes during its lifetime contain nothing. this nothingness is the concept that is know as null.

- nullable

  use the question mark after the data type such as `String?`

  ```dart
  const String? name = null;
  String? name = null;
  // only nullable list
  List<String>? names = ['foo', 'bar'];
  // nullable list & nullable values
  List<String?>? names = ['foo', 'bar', null];
  ```

  it means that variable can sometimes contain null

- cherry-picking non-null values

  use the `??`(null aware operator) mark

  ```dart
  const String? firstName = null;
  const String? middleName = 'bar';
  const String? lastName = 'baz';
  
  // old way
  if (firstName != null) {
      print("first name is the first non-null value")
  } else if (middleName != null) {
      ...
  } else if (lastName != null) {
      ...
  }
  
  const firstNonNullValue = firstName ?? middleName ?? lastName;
  ```

  `??` : if the value on my left side is null I'm gonna pick the value on my right. but the left one is not null I'll pick you. 

- null-aware assignment operator

  use `??=` mark

  ```dart
  double number = 2.0;
  number = null;
  number = 3.0;
  print(number); // 3.0
  ```

  if the value on the left side is null then change the value by the right side

- conditional invocation

  use the `?.` syntax to conditionally invoke a method or property

  ```dart
  List<String>? names = null;
  final lengthOfNames = names.length;
  ```

  ![image-20230126105505107](https://user-images.githubusercontent.com/77393619/214823429-5b6464c8-e2a4-497d-a213-f30f47c98608.png)

  ```dart
  List<String>? names = null;
  // old way
  final int lengthOfNames;
  if (names != null) {
      final lengthOfNames = names.length;
  } else {
      lengthOfNames = 0;
  }
  
  // better way(?.)
  // if the names List is present then grab its length. otherwise take the value of zero.
  final lengthOfNames = names?.length ?? 0;
  ```

## 6. Dart enumeration and objects

- Enumerations

  Named list of related items

- switch statement

- classes

  grouping of various functionalities into one packageable piece of data. grouping of related things is done with a class.

  ```dart
  class PascalCasePerson {
      void run() {
          print('running');
      }
      void breathe() {
          print('breathing');
      }
  }
  
  final person = PascalCasePerson();
  person.run();
  ```

  - instantiation

    instances are objects and objects are created from classes. every class can be instantiated meaning that the dart compiler will create a copy of that exact class with its data its functions its properties and give that copy to you
    
- Inheritance and subclassing

- abstract classes

  use the `abstract` modifier to define an abstract class - a class that can't be instantiated. Abstract classes are **useful for defining interfaces**, often with some implementation.

  ```dart
  abstract class ... {
      
  }
  ```

- factory constructors

  can return instances that are not of the same class

  it's the speed at which you can create an instance of a class that the factory constructor shines at

  ```dart
  class Cat {
      final String name;
      Cat(this.name);
      factory Cat.meow() {
          return Cat('meow');
      }
  }
  
  final cat = Cat.meow();
  ```

- custom operators

  you can define custom operators on your own classes in Dart. you can override particular operator at the language level only for your class.

  an object internally already defines an operator called `==` that returns boolean.

  ```dart
  class Cat {
      @override 
      bool operator ==(covariant Cat other) => other.name == name;
  
      @override
      int get hashCode => name.hashCode;
  }
  ```

  covariant tells dart that forget what the super class which is object defines as the parameter type for this parameter.

  :bulb: hashcode

  hashcode is a special number or a special identifier that you assign to your instance of classes 

## 7. Advanced Dart

- extensions

  adding logic to existing classes. extend or add functionality to an existing class.

  ```dart
  class Person {
      final String firstName;
      final String lastName;
      Person(this.firstName, this.lastName);
  }
  
  extension FullName on Person {
      String get fullName => '$firstName $lastName';
  }
  ```

  you're extending class `Cat` with a new functionality that is called `Run`. this is not the name of the function itself it's just the name of your extension. and you don't have to really know about the name right now so much it's just when you can go and become more advanced in dart and you for instance create libraries for yourself and people who use your libraries then they can in basically include specific extensions that you've included in your library in their code or they can exclude them.

  just know that it's just a name on the extensions so it doesn't mean so much right now. extensions are great tool for you to use if you believe that there is a functionality that you're adding to an existing class which it doesn't really belong in that class itself but it may for instance belong in the current source file that you're working with.

- Future

  Data to be returned in the future, as its name suggets.

  :bulb: synchronous vs. asynchronous

  synchronous task is a task that happens when you ask for it and it returns with the data that you ask for immediately. asynchronous task is basically a task that whose result are not returned immediately. 

- async / await

  mechanism for controlling asynchronous flow of data

- Stream

  an asynchronous "pipe" of data

  ```dart
  Stream<String> getName() {
    return Stream.value('foo');
  }
  
  void test() async {
    await for (final value in getName()) {
        print(value);
    }
  }
  ```

- generator

  for generating "iterables", marked with sync* and async*

  ```dart
  Iterable<int> getOneTwoThree() sync* {
      yield 1;
      yield 2;
      yield 3;
  }
  for (final value in getOneTwoThree()) {
      print(value); // 1 2
      if (value == 2) break;
  }
  ```

  `sync*` it is a generator function that returns a list of things but it calculates that list of things asynchronously. `async*` is equivalent of the `sync*` it does the same thing but it returns Stream which means it's asynchronously calculating its result.

  :bulb: List vs. Iterable(lazy collection)

  list in dart is an already packaged list it means that it's as if like you go to a supermarket and then you buy ready to go food that's already packaged 30 packs of that. however Iterable is like restaurant. it listens to orders of its customers and then it generates the food based on the orders.

  Iterable is a list of like things that gets calculated on the go on the fly.

- generics

  to avoid re-writing similar code

  ```dart
  class PairOfIntegers {
      final int value1;
      final int value2;
      PairOfIntegers(this.value1, this.value2);
  }
  
  class Pair<A, B> {
      final A value1;
      final B value2;
      Pair(this.value1, this.value2);
  }
  
  final names = Pari('foo', 'bar');
  ```
## 8. Basic Project Setup

- create project

  ```bash
  $ flutter create --org xxx.domain appname
  ex) $ flutter create --org se.pixelity mynotes
  ```

  `--org` : create app as an organization

  `xxx.domain` : domain name like `se.pixelity`. we need to think this is like reverse domain identifer. so this domain name will be `pixelity.se` **your org needs to be the reverse of that. so reverse identifier.**(만약 원하는 도메인 이름이 `hello.com`일 경우 프로젝트 생성시에는 `--org com.hello`로 작성해준다. 도메인이 없을 경우에는 우선 원하는대로 작성해주자.)

  `appname`

  the main properties of flutter project is identifier. identifier is what **defines that applications as unique as on the app store **where ios users and ipad os users can download applications. so identifiers are kind of like **reverse domain identifier**. so if your website is `foobar.com` and your application is callbed `baz` then your reverse domain identifier for your application will become `dot foobar.baz`.

  it's kind of like you take your domain name and reverse it so if `foobar.com` becomes `com.foobar` and then you put dots after that and then you put your actual application name.

  so these identifiers need to be unique. if a developer on the ios app store or google play store is already gone and registered the reverse basically that item identifier.com.foobar.bass for any of their applications so they said okay here's my application called image gallery but it has a completely random identifier of `com.foobar.baz`.

  then you as a new developer even if you want to do the same funky deployment to the app store you can't register that name anymore because it is already taken. so think of the identifier of your project as what is gonna carry on from the start of where you create your project all the way through to the app stores.

- upgrade flutter

  ```bash
  $ flutter upgrade
  ```

- quick look around

  flutter creates the skeleton or the scaffold of your flutter project but pretty much everything necessary for you to be able to run that project

  ![image-20230130103921433](https://user-images.githubusercontent.com/77393619/215477037-76577f9b-d51a-4378-9639-62011f21f61b.png)

  flutter outputs a native binary on your phone a native fat binary basically for your ios application and it just puts one view on the screen and then it graphically renders all its contents using metal.

- ios

  ![image-20230130110123719](https://user-images.githubusercontent.com/77393619/215477130-ea1c4601-9311-46cf-845a-9b094c8da9f4.png)

  there are various tool available for ios developers to be able to bring in dependencies for web for instance if you're writing a node application you will just use npm(node package manager) if you're using swift you will probably just bring in for instance spm(swift package manager) or cocoapods. or android you will use gradle for bringing in external dependencies

  every ios or android or web application can bring with itself dependencies. and dependency is a way for your application to bring in code from other people in order to be able to achieve special functionalities

  flutter sits on top of these(ios, android, web) so it can control all the small bits and pieces for these platforms to be able to be packed inside one flutter application which sits on top. and all these different platforms down here can have their own dependency management so the dependency managements kind of sit under one layer under so flutter then talks with these dependency managers and says okay you need to install this dependency for me to be able to work.

- test

  ![image-20230130111029621](https://user-images.githubusercontent.com/77393619/215477157-1ce42b09-987f-49dc-8bb2-a45da58dc34b.png)

  test folder is where you create your tests. automatically run a series of tests against their own code to make sure that everything is functioning as the programmer intended.

  integration tests, widget tests, unit tests etc inside.

- android

  ![image-20230130111243943](https://user-images.githubusercontent.com/77393619/215477199-b0005891-3f93-4fdd-988b-e55482364f6a.png)

  it is putting all the necessary files and folders that is required for your android project to be hosting your flutter application. so just know that flutter kind of is a series of tools is like a mobile kind it's like a sdk that gets injected into these native applications and natively also renders its content. 

  just like we had a host ios application, you will alose have an android folder which contains all the bits and pieces required for your application to be run natively on android phones and tablet. 

- web

  ![image-20230130111806053](https://user-images.githubusercontent.com/77393619/215477243-84c6e343-bf14-4144-96ed-95a8589a1124.png)

- analysis

  ![image-20230130111934035](https://user-images.githubusercontent.com/77393619/215477277-a553411f-b3aa-4aa6-9e0f-a1aff08fde9c.png)

  think of analysis as a way for a flutter to be able to have a look at the code that you write. it allows you to basically define the roles that make sense for your project.

- **pubspec.yaml**

  ![image-20230130112237450](https://user-images.githubusercontent.com/77393619/215477314-83bbe805-cb81-4604-a26b-81ca9a64093d.png)

  this is a file that you'll need to know about flutter and the basic structure that it creates for you is that there are tons of documentations(information provided by the developers who created the tool for you in order to help you get better at that tool)

  - version

    ![image-20230130142502549](https://user-images.githubusercontent.com/77393619/215477341-5e9382fc-baed-4341-8991-1f4d92d9fba2.png)

    major, minor, build number

  - sdk(software development kit)

    ```bash
    $ flutter --version
    ```

    ![image-20230130143121308](https://user-images.githubusercontent.com/77393619/215477379-f38dcfdb-39cb-4e2a-864a-344c240edf33.png)

    if you share your source code with some other developer if they get your source code and they want to for instance be able to test this application on a simulator or emulator on a real device then they are required to have flutter sdk version this or less than this

  - dependencies

    ways for you as a software developer to bring in code that other people have written in order to make your application function better

  - search for dependencies : pub.dev

  - dev_dependencies

    that will bring into your project which are useful only under development. normal dependencies will get linked to your project and then they will be shipped with your application whereas dev dependencies are only dependencies that under the development time you will use in order to make your sortware better

- adding our dependencies

  - firebase

  ![image-20230130144717623](https://user-images.githubusercontent.com/77393619/215477405-9394dbf4-6b8f-4701-8caf-bf3b0ac2a6d1.png)

  ```bash
  $ flutter pub add firebase_core
  $ flutter pub add firebase_auth
  $ flutter pub add cloud_firestore
  $ flutter pub add firebase_analytics
  ```

  firebase is a computer in the cloud just think of that is written by google so you control it with simple commands on your computer but it controls your data so your client your flutter application can connect to it and grab the data and read the data and manipulate the data on the client side.

  we've brought in four dependencies.

  `firebase_core` : the kernel the main important parts of firebase which is what we're going to use as our server where all the nodes for all users are going to sit

  `firebase_auth` : for authentication is where our users will be able to register log into our application and log out and also get email confirmations to send to their emails in order to be able to verify the account

  `cloud_firestore` : is used for when we actually store a logged in users notes in the firebase backend

  `firebase_analytics` : if you use firebase analytics when you basically set up your firebase backend you will get some free analytics in for instance which screen did the user go to which button did they press and you can have a look at these analytics.

## 9. iOS App Setup

- we installed our Flutter app on a real iOS device

- Developer account

  in order to release the app for iOS and iPadOS you need a development account

- profiles cetificates appids ...(5:51:00)

- Certificates and Profiles

  certificates identifies you, profiles identifies your app.

- account walkthrough

  https://developer.apple.com/acocunt

- ~6:59:30

## 10. Android App Setup

setting up for running my application on a real phone or a real device

- android emulator

  emulator is quite different from a simulator in that an emulator as its name indicates it tries to emulate everything about the operating system and the device. it's a lot closer to the actual physical device

- **Scrcpy**

  https://github.com/Genymobile/scrcpy

  we will be using scrcpy to mirror a real Android device on the screen. it's open source and free.

  안드로이드 디바이스 화면을 미러링하기위해서 Scrcpy라는 앱을 받자. scrcpy를 사용하면 컴퓨터에서의 작용이 실제 디바이스에 적용된다는 장점이 있다.

  your computer will be able to mirror your android phone on your computer's screen. scrcpy allows you to interact with your phone from your computer screen.(예를들어, 컴퓨터화면상에서 휴대폰 버튼을 클릭하면 실제 디바이스의 버튼을 누르는 효과를 볼 수 있다.)

- **ADB(Android Debug Bridge)**

  `brew install --cask android-platform-tools`

  Scrcpy설치전에 먼저 ADB를 설치해줘야한다.(Scrcpy가 디바이스에 명령을 전달하기 위해서 ADB를 사용하기 때문.) `android-platfrom-tools`내에 ADB가 존재하기 때문에 `android-platfrom-tools`를 설치해주면된다. 

  it actually stands for Android  debugger or something is great tool if you want to for instance be able to talk with your android telephone all from the command line so you can send it a message. so you basically **send commands to your android telephone or tablet through your terminal.**

  having adb install your computer then you can actually install scrcpy which uses adb in order to talk to your telephone and send commands to it and recieve images from it etc.

  ADB를 설치했다면 Scrcpy를 설치해주자. https://github.com/Genymobile/scrcpy

- USB Debugging(07:11:50)

  scrcpy를 실행시키기 전에 안드로이드 디바이스를 우선 컴퓨터와 연결시켜줘야한다.(개발자모드)

  you will need to enable USB debugging to mirror your screen

  `scrcpy`를 실행하면 연결된 디바이스를 확인할 수 있다.

  ![image-20230201103633896](https://user-images.githubusercontent.com/77393619/216038189-6d5538d5-6fc3-4729-b593-6684a3970e6b.png)

  :bug: `adb server version (41) doesn't match this client (39); killing...`에러가 확인되어 [검색](https://forum.qt.io/topic/123945/qtcreator-wifi-debugging-error-adb-server-version-41-doesn-t-match-this-client-39-killing/2)후 아래와같이 진행

  ```
  adb kill-server
  sudo cp ~/Android/Sdk/platform-tools/adb /usr/bin/adb
  sudo chmod +x /usr/bin/adb
  adb start-server
  ```

  하지만 여전히 오류발생하여 좀 더 [검색](https://github.com/Genymobile/scrcpy/issues/527)진행

  ![image-20230201104846178](https://user-images.githubusercontent.com/77393619/216038226-55d41cca-9032-4b13-8361-5955939c72f4.png)

  ```
  여러 adb 버전이 실행 중입니다. 시스템의 무언가가 adb 41로 서버를 시작합니다. 그리고 scrcpy는 adb 39를 사용합니다. adb 41 바이너리가 있는 위치를 찾고 강제로 실행할 수 있습니다.
  ```

  adb version을 확인해보니 41로 확인된다

  ![image-20230201104425385](https://user-images.githubusercontent.com/77393619/216038260-2f62ad81-8bdf-4d47-a35b-371cd67b973d.png)

  `ADB=/path/to/some/adb scrcpy`에 대한 추가설명

  ![image-20230201105039074](https://user-images.githubusercontent.com/77393619/216038286-2cc515f8-90c4-4c61-85d0-c44aa1a949e4.png)

  adb 경로

  ![image-20230201105629037](https://user-images.githubusercontent.com/77393619/216038331-f5fd2268-3d32-48fd-8869-de7e74132f1a.png)

  시스템의 서로 다른 ADB 버전으로 인해 발생하는 문제. 하나는 `/usr/bin`에 있고, 다른 하나는 sdk 도구 폴더에 있으므로 `/usr/bin`에 존재하는 adb를 삭제하고 sdk platform-tools에 존재하는 adb로 바꾼다.

  아직해결이 안됨.. 찾아본 사이트만 우선 남겨둠

  - https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#conflicts-between-adb-versions

  - https://github.com/Genymobile/scrcpy/issues/527

- Android Mirroring

- Disable screen sleeping

  연동되어있는 디바이스가 lock되면 개발하는데 문제가생길 수 있으므로 disable시켜준다.

  You can disable the feature so you don't have to turn the screen on all the time

  screen > system > developer options > stay awake 활성화

## 11. Firebase Backend Setup

setting up our project on firebase for our backend(7:31:50)

- firebase

  it is kind of like severless so it is a server without you.

  simplicity so that we can get the backend working up and running without so much work

- FlutterFire initialization

  https://firebase:flutter.dev/docs/overview

- install FlutterFire CLI

  ```bash
  # Install the CLI if not already done so
  dart pub global activate flutterfire_cli
  
  # Run the `configure` command, select a Firebase project and platforms
  flutterfire configure
  ```

  ![image-20230131152554322](https://user-images.githubusercontent.com/77393619/215763386-ea646fb8-b064-431c-bdf4-ab3f8030e1cd.png)

  - make sure the path is updated(PATH를 지정해주어야만 global에서 flutterfire 명령어 사용이 가능해진다. 리눅스의 경우 `.bashrc`파일에 추가해주면 됨.)

    ![image-20230131153031970](https://user-images.githubusercontent.com/77393619/215763422-c219b58e-082a-4141-8cb9-306dea91ad9f.png)

    `vim ~/.zshrc => export PATH ="$PATH":"$HOME/.pub-cache/bin"`

- what is Firebase CLI

  a CLI to help us interact with Firebase right from our terminal.

- install or update Firebase CLI

  you need to have a look at this documentation on how you can install the firebase CLI on your computer whether you're using mac, linux, windows...

  https://firebase.google.com/docs/cli#install-cli-mac-linux or `curl -sL firebase.tools | upgrade-true bash`

- Login / Logout

  you need to log in into your account using that firebase cli

  firebase integrate를 위해서 firebase console이라고 불리는 firebase project를 생성해야한다.

  this project is pretty much the configuration of your firebase backend on firebase's console on their website so you need to configure a backend so what we need to do here is now before we can actually configure it back in your terminal you need to tell firebase what user you have. because firebase projects are linked to your google accounts.

  in order for our firebase cli to understand where it needs to create the project you need to tell it to log in with an account.

  `firebase login`

  ![image-20230131155258957](https://user-images.githubusercontent.com/77393619/215763460-fcf06340-6142-4cd7-ad58-f405103a52fe.png)

  `firebase logout`
  
- Configuring our backend

  need to configure a firebase project. we do that with the flutter fire cli(which we installed in using command `dart pub global activate flutterfire_cli`)

  - issue the flutter fire configure command

    `flutterfire configure`

    ![image-20230201082331827](https://user-images.githubusercontent.com/77393619/216038355-13d42b08-9637-4d67-886a-f11f721d023e.png)

    위 명령어 사용전 firebase console 페이지로 이동하여 프로젝트를 생성해야한다.

    globally하게 동일한 아이디로 이미 프로젝트가 만들어져있다면 아래와같은 에러가 발생한다.

    ![image-20230201082457525](https://user-images.githubusercontent.com/77393619/216038378-e6d26a45-63a1-495a-9acd-4885abf20bd7.png)

    순차적으로 진행시

    ![image-20230201083224525](https://user-images.githubusercontent.com/77393619/216038400-ec8c6391-e27f-4850-bad9-d862acc81574.png)

    안드로이드, iOS앱의 identifier확인이 가능하다.

    ```
    android   1:1060967167971:android:fd1d4ef3faf3f8529852d6
    ios       1:1060967167971:ios:338382e9e8b83ec79852d6
    ```

    ![image-20230201083519795](https://user-images.githubusercontent.com/77393619/216038440-ee28f5e0-7f66-46c6-a924-14c928f3be95.png)

- App IDs

  make sure these identifiers are correct and that the bundle identifier that we provided to the cli is also placed in the configuration file correctly.

  - identifier 검색시(`firebase_options.dart`)

    ![image-20230201083851276](https://user-images.githubusercontent.com/77393619/216038453-ba5cbe5f-6202-43ee-b8a4-16df4f5d63fd.png)

    iOS identifier 혹은 안드로이드 identifier검색해보면 위처럼 검색결과를 확인할 수 있는데, this is where android and ios are configured

    ![image-20230201084138409](/home/myounjunkim/TIL/Flutter for Beginners.assets/image-20230201084138409.png)

    위의 정보들은 프로젝트참여자들끼리만 공유되어야함.

## 12. Basic register user screen

- 8:01:30 ~

- hot reload vs. hot restart

  actually looking the changes that we don't have to press any publish button.

  보통의 경우 hot reload가 작동하지만, changes가 so drastic하거나 너무 클경우 hot restart를 해야한다. rebuild your application(hot restart)

- MaterialApp inside runApp & HomePage widget

- Stateless and Stateful

  what kind of widget do we need?

  Stateful widget can keep that information so it has state and it keeps hold of that data. and upon this data being changed it can redraw itself. so stateful widget is something that is on the screen and it can contain data upon who's changing it can redraw itself.

  stateless widget wouldn't necessarily be able to redraw itself to contain any mutable data. it means even stateless widgets can be redrawn depending on what you're trying to do but they **cannot contain mutable variables**. it can only contain read-only data.

  정리하자면, stateful widget은 유저 상호작용으로 변동될 수 있는 데이터를 가질 수 있는 위젯이고, stateless widget은 변동될 수 없는 조회만 가능한 데이터를 가질 수 있는 위젯이다.

- Scaffold

  we need a Scaffold inside our HomePage widget

  Scaffold it itself is a stateful widget and also appBar it itself is a stateful widget.

  so the main widget we're returning from our build function it should return a widget.

  Text widget which is stateless widget it means internally its state can't change and it doesn't have any mutable variables.

  you need to kind of try to stick to stateless widget(stateless 위젯을 고수하려고 노력해야 합니다. 08:22:30)

- login button

  Button on home page in the center to register

  ```dart
  class HomePage extends StatelessWidget {
      const HomePage({Key? key}) : super(key: key);
      @override
      Widget build(BiildContext context) {
          return Scaffold(
          	appBar: AppBar(
              	title: const Text('Register'),
              ),
              body: Center(
                  child: TextButton(
                      onPressed: () {}, 
                      child: const Text('Register')
                  ),
              ),
          );
      }
  }
  ```

   you can go and wrap your widgets with other widgets

- Login upon button press

  Change onPressed to async

  버튼이 눌리면, 유저를 firebase에 등록해야함(asynchronous한 작업)

  ```dart
  TextButton(
  	onPressed: () async {
          ...
      }
  )
  ```

- Firebase sign in methods

  https://firebase.flutter.dev/docs/auth/usage/#other-sign-in-methods

  firebase allows you to enable various sign-in methods for your users.

  ![image-20230201212714073](https://user-images.githubusercontent.com/77393619/216047785-5e89031f-88e7-4248-ae06-32f1913b1301.png)

  fierbase has a concept of anonymous users.

- Column with 2 text field

  Let's add username and password text fields

  ```dart
  class HomePage extends StatelessWidget {
      const HomePage({Key? key}) : super(key: key);
      @override
      Widget build(BiildContext context) {
          return Scaffold(
          	appBar: AppBar(
              	title: const Text('Register'),
              ),
              body: Column(
                  children: [
                      TextField(),
                      TextField(),
                      TextButton(
                          onPressed: () {}, 
                          child: const Text('Register')
                  	),
                  ],
              ),
          );
      }
  }
  ```

  ![image-20230201213213833](https://user-images.githubusercontent.com/77393619/216047807-928ff6e7-32d2-49b6-b3fd-2a54658d1dd3.png)

  you need to pass information from this text field. and the way to do that is using something called a text controller or a text editing controller is kind of like a proxy.

- Stateless -> stateful(convert to stateful widget)

  we need to grab the text from our controllers

  ```dart
  class _HomePageState extends State<HomePage> {
      ...
  }
  ```

- TextEditingController

  We need 2 of them for email and password text fields

  ```dart
  class _HomePageState extends State<HomePage> {
      
      late final TextEditingController _email;
      late final TextEditingController _password;
      
      @override
      void initState() {
          _email = TextEditingController();
          _password = TextEditingController();
          super.initState();
      }
      
      @override
      void dispose() {
          _email.dispose();
          _password.dispose();
          super.dispose();
      }
      
      @override
      Widget build(BiildContext context) {
          return Scaffold(
          	appBar: AppBar(
              	title: const Text('Register'),
              ),
              body: Column(
                  children: [
                      TextField(
                      	controller: _email,
                      ),
                      TextField(
                      	controller: _password,
                      ),
                      TextButton(
                          onPressed: () {}, 
                          child: const Text('Register')
                  	),
                  ],
              ),
          );
      }
  }
  ```

  late is keyword in dart that tells your program that although this variable has no value right now but I promise to assign a value to it before it is used. so it's kind of like a contract.

- stateful widget(08:38:20)

  you need to also know something about stateful widgets. it will have two great functions one is called **init state** and the other one called is **disposed**.

  init state will be called by flutter automatically when it creates your home page.

  now whenever this homepage then dies and goes out of the memory or it's trying to go out the memory it will also get a function called dispose.

- Hint on text fields

  To help the user understand what the text fields are for.

  hint will automatically be removed as soon as the user types at least one character on that text field

  ![image-20230202013347062](https://user-images.githubusercontent.com/77393619/216258363-c5b76eab-66e1-4034-a49f-25046636a1c3.png)

- Let's do authentication

  import `package:firebase_auth/firebase_auth.dart`

- Button click

  버튼을 누르면 컨트롤러에 있는 이메일과 비밀번호 데이터를 가져와야한다. we're going to our email and password controllers and grabbing their text which is the latest text that the user entered in those field.

- create the user

  `FirebaseAuth.instance.crateUserWithEmailAndPassword`

  ```dart
  TextButton(
      onPressed: () async {
          final email = _email.text;
          final password = _password.text;
          await FirebaseAuth.instance.createUserWithEmailAndPassword(
              email: email, password: password);
      },
      child: const Text('Register'))
  ```

  this function return the Future of a user credential

  ![image-20230202014253986](https://user-images.githubusercontent.com/77393619/216258423-d80de38f-f5d5-4e65-bca2-20c70522098e.png)

  바로 확인을 해보면 아래와 같은 에러가 나온다. `No Firebase App '[DEFAULT]' has been created ...`

  ![image-20230202014449724](https://user-images.githubusercontent.com/77393619/216258468-bedbfb7c-e752-4cb0-a01d-ce22de3b558b.png)

  발생이유를 살펴보면 firebase configure을 했을 때 `lib > firebase_options.dart`파일이 생긴게 생각날 것이다. you've created this configuration but you've never actually told me about it

  - Firebase needs initialization before other calls to Firebase

    `Firebase.initializeApp`

    ```dart
    onPressed: () async {
        await Firebase.initializeApp(
            options: DefaultFirebaseOptions.currentPlatform,
        );
        final email = _email.text;
        final password = _password.text;
    
        final userCredential = await FirebaseAuth.instance
            .createUserWithEmailAndPassword(
            email: email, password: password);
        print(userCredential);
    },
    ```

  이번에는 다른 에러가 발생[CONFIGURATION_NOT_FOUND]

  ![image-20230202021043787](https://user-images.githubusercontent.com/77393619/216258514-19a5ea29-09f4-4af6-8136-6d1d52829a9e.png)

  이유 : firebase에서는 다양한 등록방법을 제공하는데 어떠한 방법을 사용할 것인지 정하지 않았기 때문에 발생한 에러. firebase console 사이트에서 설정해줘야 한다. we haven't enabled email/password sign in combination

  ![image-20230202021757575](https://user-images.githubusercontent.com/77393619/216258572-de332dcd-94da-44c7-982c-db933611b05f.png)

  해결 : https://stackoverflow.com/questions/41124178/com-google-firebase-firebaseexception-an-internal-error-has-occurred-configu

  이제 다시 register해보면 userCredential을 반환받는 것을 확인할 수 있다.

  ![image-20230202021900572](https://user-images.githubusercontent.com/77393619/216258604-14bac1ce-a6d4-4998-a416-b10d19d02f66.png)

- Make our password text field secure

  obscureText: true, 

  enableSuggestions: false, - as you're typing in a text field depending on your operating system it will provide you suggestions.

  autocorrect: false - when you try to type something you're disabling autocorrect based on your password field

  ```dart
  TextField(
      controller: _email,
      enableSuggestions: false,
      autocorrect: false,
      keyboardType: TextInputType.emailAddress,
      decoration: const InputDecoration(
          hintText: 'Enter your email here',
      ),
  ),
  TextField(
      controller: _password,
      obscureText: true,
      enableSuggestions: false,
      autocorrect: false,
      decoration:
      const InputDecoration(hintText: 'Enter your password here'),
  ),
  ```

- Enabling widget binding before Firebase.initializeApp

  https://docs.flutter.dev/resources/architectural-overview#architectural-layers

  initializing you firebase application before you start with everything else on your screen and phone so what we need to do is take advantage of something called widgets flutter binding

  firebase needs to kick start its process before everything else is rendered on the screen and in order for that to happen it needs to have some sort of that like the core flutter engine to be in place. and so that it can make its call to the core flutter engine and say that I'm done with my work so in order to do that then you need something called widgets flutter binding

  ```dart
  await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
  );
  ```

  버튼을 누를 때 위 작업을 하는 것이 아니라 다른곳에서 이 작업을 하자. 그 작업을 위해서 we have to first take care of this widget binding.

  ```dart
  void main() {
    WidgetsFlutterBinding.ensureInitialized();
    runApp(const MyApp());
  }
  ```

- **FutureBuilder**

  HomePage can initializeApp using a FutureBuilder

  ```dart
  onPressed: () async {
      await Firebase.initializeApp(
      	options: DefaultFirebaseOptions.currentPlatform,
      )
  }
  ```

  what you need to do is kind of like you want to tell flutter to **not build Column before it has finished doing that Future** and the way to do that is using flutter's FutureBuilder widget

  it takes a **future**, it performs the future and once this future has succeeded or it has failed doing its work it will give a call back and in that callback it asks you to produce a widget you want to display to the user depending of the state of that futures result.

  futurebuilder doesn't have an actual future to perform. 

  ```dart
  FutureBuilder(
  	future: Firebase.initialzieApp(
      	options: DefaultFirebaseOptions.currentPlatform,
      ),
      builder: (context, snapshot) {
          return Column()
      }
  )
  ```

  :bulb: ctrl + space 하면 vs code에서 작성가능한 코드를 추천해주므로 코드가 기억안날 때 사용해보자.

- Loading screen while waiting

  we can use **connection states** to determine the state of a Future

  we told future builder to perform a future. the future was firebase initialize app. 

  now if you look at the builder, we're returning from it now is a Column. the second parameter that gets passed your builder is something called a **snapshot** of data type async snapshot. an **async snapshot of an object is the state of the object right now**. so that object itself is actually the result of you future in this case firebase app. so this snapshot is an async snapshot of your firebase app.

  so one thing you do need in this snapshot is its **state you see a future** has a start point it has a line where it processes its information and it has an end point. it either ends successfully or it fails. now the snapshot is your way of getting the results of your **future whether it has it started, is it processing, is it done or did it fail**.

  ```dart
  FutureBuilder(
  	future: Firebase.initializeApp(
      	options: ...,
      ),
      builder: (context, snapshot) {
          switch (snapshot.connectionState) {
              // future가 완료된 경우
              case ConnectionState.done:
                  return ...;
              // future가 끝나지 않은경우
              default:
                  return ....;
          }
      }
  )
  ```

  4가지 상태가 존재. `ConnectionState.none`, `ConnectionState.waiting`, `ConnectionState.active`, `ConnectionState.done`

- We have a basic Firebase set up now

  We now need to do refactoring and work on login/register views

## 13. Login View

- simple register view

  But nothing more. Let's devide logics into register and login views.

- create a stateful registerview widger

  this will be used as the base of our register view

  stateful widget생성하기위해 `stf`을 쳐주면 된다.

  ```dart
  // base of our register view
  class RegisterView extends StatefulWidget {
    const RegisterView({super.key});
  
    @override
    State<RegisterView> createState() => _RegisterViewState();
  }
  
  class _RegisterViewState extends State<RegisterView> {
    @override
    Widget build(BuildContext context) {
      return Container();
    }
  }
  ```

- HomePage is going to become LoginView

  Rename HomePage to LoginView. `f2`키를 눌러서 변경하거나, 해당 위젯 이름에 커서를 대고 우클릭 `Rename Symbol`로 변경하면된다.

- Move LoginView into its own file

  `lib/views/login_view.dart`로 코드를 옮겨준다. 이때 import관련하여 빨간줄이 여러개 뜨게 되는데 `ctrl + .`을 활용하여 해당 코드에 대한 라이브러리 등을 가져와주자.

  ![image-20230202095340320](https://user-images.githubusercontent.com/77393619/216258688-abf6c68b-faed-422b-a14b-519d5a4ba329.png)

- LoginView code goes into RegisterView

  Grab the source code from LoginView and paste it inside RegisterView

- Login instead of register in LoginView

  Chnage `createUserWithEmailAndPassword` to `signInWithEmailAndPassword`.

  `signInWithEmailAndPassword` also return the Future which has user credentials

  ![image-20230202100749880](https://user-images.githubusercontent.com/77393619/216258742-e2b30d97-f508-4edf-8d06-9784ff5ed34f.png)

- LoginView, Handling **user-not-found**

  `e.code == 'user-not-found'`

  로그인시에 등록되지 않은 사용자의 경우 아래와 같은 에러를 뱉어준다.

  `[firebase_auth/user-not-found] There is no user record corresponding to this identifier. The user may have been deleted.`

  ![image-20230202101110302](https://user-images.githubusercontent.com/77393619/216258772-b9be4611-d0a3-45a4-a680-f9c12b4f9085.png)

  we need to handle a thing called an exception(try - catch문으로 예외처리를 해줘야함)

  ```dart
  try {
      final userCredential = await FirebaseAuth.instance
          .signInWithEmailAndPassword(
          email: email, password: password);
      print(userCredential);
  } catch (e) {
      print("something bad happened");
  }
  ```

  `e.runtime` gives you information about which class of exception this is. `FirebaseAuthException`

  ![image-20230202101722348](https://user-images.githubusercontent.com/77393619/216258776-1eccec48-f93e-4d45-9e53-5a784d7680cb.png)

  and we will handle the FirebaseAuthException not just any exception. there's a format of catching specific exceptions you prefix your catch statement with the keyword `on`. and now we can use `e.code` for FirebaseAuthException.

  ```dart
  try {
      ...
  } on FirebaseAuthException catch (e) {
      print(e.code); // user-not-found
  }
  ```

- LoginView, Handling **wrong-password**

  `e.code == 'wrong-password'`

  ```dart
  try {
      ...
  } on FirebaseAuthException catch (e) {
      if (e.code == 'user-not-found') {
          print('User not found');
      } else {
          print('Something else happend');
          print(e.code); // wrong-password
      }
  }
  ```

  one of those erros is wrong password. 이메일을 맞추고 비밀번호를 틀려보면 아래와같은 에러가 발생한다.

  ![image-20230202104132869](https://user-images.githubusercontent.com/77393619/216258779-d905f44c-4831-4d6e-b573-51d4d95a3ed4.png)

  ```dart
  try {
      ...
  } on FirebaseAuthException catch (e) {
      if (e.code == 'user-not-found') {
          print('User not found');
      } else if (e.code == 'wrong-password') {
          print('Wrong password');
      }
  }
  ```

- RegisterView, handle **weak-password**

  `e.code == 'weak-password'`

  there are some default security rules set up on firebase for credentials. 비밀번호를 너무 간단하게 설정할 경우 `e.code`가 `weak-password`가된다.

  ![image-20230202104825424](https://user-images.githubusercontent.com/77393619/216258780-765cea25-158d-4b88-bf91-3de1a9cbf0a7.png)

- RegisterView, handle **email-already-in-use**

  `e.code == 'email-already-in-use'`

  이미 사용된 이메일이라면 발생하는 코드.

  ![image-20230202130500188](https://user-images.githubusercontent.com/77393619/216258785-0c509a4f-c8d1-489a-ae1f-eb1d60b59916.png)

- RegisterView, handle **invalid-email**

  `e.code == 'invalid-email'`

  유효하지 않은 이메일을 작성할 경우 발생하는 에러코드

  ![image-20230202130747292](https://user-images.githubusercontent.com/77393619/216258788-ab0e84e1-0cae-49c5-85bc-067a5a6086a1.png)

- show error message to user

  upcoming chapters

- Ensure we are logged in

  We need this login-session before next chapter

  ```
  사용자가 로그인을 한 이후에도 그대로 loginView에 있게되면 이상하다. 실제 로그인관련 state를 핸들링함으로써 서비스를 이용하도록 해주어야한다.
  ```

  make sure that we are logged in to the application. you can be a logged in user but still end up being in a login view so if you send a login user to a loginView doesn't mean that the user logged in. instead it means well that user is logged in but may want to log in as a different user so that is the case in our application as well we have a register screen a login view but I personally don't know what the state of the application at the moment is. 

  next chapter, we're working on seperating the app initialization from the login and register screen because you can see at the moment we have this futureBuilder that is initializing firebase and it is doing lots of work comes with snapshots stay done etc. and we're doing the exact same thing in two views.(loginView and RegisterView) so what we need to do is kind of like seperate that logic and ensure that we display the correct view depending on what the state of the application is. and before we start, we need to make sure that the user the current user is logged in. 

- Ensure we are logged in

  this ensures that the firebase instance that is running in this application right now is going to cache that information locally on ios is going to cache that information in a secure storage called keychain and on android it's called shared preferences or st. so that information is going to be securely stored now on that telephone which is an android telephone right now and when we restart the application whenever if I like shut down my telephone restart it the telephone come back up that information is already saved on that telephone so my user is logged in. so just ensure that before we continue with the next chapter that you've registered the user first and that you've logged in with that user from your application so that information is cached inside the applicaiton.

## 14. Seperating app initialization from login/register

- seperate the app initialization from the login and register screen (9:53:00)

  At the moment app initialization is bound to our widgets

- Widgets that are doing app initialization

  This is usually not a good idea, we need to clean this up.

  we will just have one initialization and bring the register view in its own file

- RegisterView needs its own file

  Move RegisterView into `views/register_view.dart`

- Dedicated HomePage stateless widget

  This widget needs to do the initialization. 

  dedicated homepage does the app initialization and depending on whether the user is logged in or logged out or if the user is verified or not then it's going to display the correct widget on the screen.

  just to explain that a little bit more is that you see in your main function in `main.dart`

  ```dart
  void main() {
      // main function
      runApp(
      	MaterialApp(
          	title: '...',
              theme: ThemeData(
              	primarySwatch: Colors.blue,
              ),
              // first you're going to LoginView
              home: const LoginView(),
         	)
      )
  }
  ```

  that when your application run, it runs you're telling it to go to loginView but why are we saying go to loginView. we have no logic at the moment that says are you logged in then show the loginView or if you're not logged in show the registerView. that's we're going to do with our homePage.

  so the HomePage is kind of being the manager of the different routes that your application can manage.(조건에 따라서 각각의 다른 view를 제공하는 역할을 하는 HomePage)

  조건에 따라 다른 view를 라우팅해주므로 개발자마다 이름칭하는게 조금씩 다르다. routePage라고 불리기도함.

- Use HomePage in main function

  Instead of going directly to another widget.

  - it needs to initialize firebase. 

    FutureBuilder를 사용하는 모든 View마다 firebase를 initialize하는 것은 너무 비효율적이기 때문에 이를 한번에 해주기위해서 HomePage를 활용한다.

- Non-null and verified user

  Let's see the properties of the user

  **make sure that the user is not null** and that also the user is verified. under some rare circumstances with firebase such as when you haven't initialized your firebase applicaiton using  initialize app the user that is stored in the firebase code or in the instance of firebase running inside you application may actually be null.

  what we need to do is to ensure that the current user in the application is non-null meaning that it should be present and also that the user's email should be verified.

- Email verificaiton

  why email verification is important for a user's email to be verified. the reason

  what we need to do in our applicatoin is to make sure that whenever someone comes and registers a user using the email address and a password of their choosing then **we're gonna send a real email using firebase to that email address** and say hey you just registered a user here make sure that you click on this link that says verify blah blah to actually verify your user with our application or with our file with our applicatoins firebase instance that sits on firebase clud.

  so let's then check the current user actually is logged into the application.(https://stackoverflow.com/questions/54000825/how-to-get-the-current-user-id-from-firebase-in-flutter)

  ```dart
  FirebaseAuth.instance.currentUser
  ```

  ![image-20230202142535975](https://user-images.githubusercontent.com/77393619/216258790-548e9491-07db-48d3-ba17-39b92180ec35.png)

  :bulb: anonymous user is a user who hasn't really logged into the application yet

  emailVerified로 로그인 유무를확인하려고하는데 아래와 같이 붉은줄이 나온다. 이유는 받아오려는 user가 null이 될 수 있기때문에(`User?` 즉, optional user라는 것). if something goes wrong and firebase can't calculate your current user for instance if you disable anonymous users then firebase will be saying oops null user. the user is absent and I don't know who this user is.

  ![image-20230202143216840](https://user-images.githubusercontent.com/77393619/216258794-2358f9a0-d4fc-4346-bf82-b0660486486d.png)

  that is firebase API telling your application that if you're using my API then you need to handle this case you can't just ask me if the email is verified because the user may actually be null the user may be absent.

  그래서 여기서 제안하는 방식은 you can conditionally access that property using the `?.` but as you do that you see you'll get another problem. it means ok you're asking me to compare an optional boolean with an actual boolean because remember if conditions need to resolve into a true or false.

  ![image-20230202143827390](https://user-images.githubusercontent.com/77393619/216258796-12ddfc91-1944-4511-a107-2c454b9430ce.png)

  위의 경우는 조건에 boolean이 들어가야하므로 조건문을 만들기 전에 따로 boolean을 받을 변수를 만들어주어야한다.

  ![image-20230202144156887](https://user-images.githubusercontent.com/77393619/216258798-2b9f6764-7d3f-4dbe-82a4-f2cc9cd1fcef.png)

## 15. Git and GitHub

- (10:19:48~)

- Git and GitHub

  Version control and why we need it

  store you code in a safe place and always retrieve it later

- Git

  piece of software on your computer that allows you to manage various changes that you make to a code base  such as our project at different times keeping track of the date those changes were made the person who made the changes and the changes themselves. and also it will be able to provide you the difference between your recent changes and what was already provided in the or what was already committed into this git repository.

  **git repository** is an empty bucket initially where there is nothing in there and as you interact with your source code then you'd be like okay now I want to turn this source code that I've written into a bucket so then there's a bucket created around your source code called a git repository which keeps track of all the changes that you're making or anybody else that works on the same source code is making to the code and it will allow you to save snapshots of those changes at specific times of your choosing.

- practice

  - `mkdir testing`

  - `cd testing`

  - `ls -la` 폴더내 파일확인

  우선 git 활용전에 git 사이트로가서 설치해야한다.

  - `which git` 설치된 git 위치 확인(윈도우에서는 그냥 `git`이라고 치면됨)

  - 원하는 폴더에서 `git init .` tell the git that this current directory in itself is a git's repository.(루트폴더에서 하면 안된다 !)

    `.git`파일이 생기는데 이것은 keeps track of its internal like the changes to this directory and like what you save when you save it who is it that saved the work etc.

    이렇게 되면 이제 you can issue various diff git commands such as `git status`

  - `git status` will give you the current status on this directory

  - git whenever you're working git doesn't just save your work automatically. you need to tell git to save your work. those points where you save your work there are call **commmits**

  - tracked files vs. untracked files

    tracked file is a file that you've told git about before. so it's tracking the changes being made to that file.

    untracked file is a file that you have not told git before about. so it says oh here's a file you're doing something with it but i'm not gonna even look at it i'm not gonna keep track of it because you don't you didn't tell me to do so.

  - a file basically can be in 3 states in git right now. tracked, untracked and staged

  - `git add <file>` to include in what will be committed. commit means that you're going to save this work in git.

    `git rm --cached <file>` to unstage

  - `git commit -m "message"` 

  - `git log` if you want to see the commit that you just made. and you can see all the commits that were made and who they were made by and also be able to see the date that were made and the commit message. and there's the email of the person who basically did that commit

  - `git config --global` or `git config` how you tell get who you are (user information)

- Git

  so it is a piece of software that allows groups of people work on the same piece of code without losing their changes.

- GitHub

  It's our Git provider in simple words. it is simply said a cloud service for storing your git repositories.

  it's not the same thing with git. git is a software that actually manages all your commits and etc but github is the cloud service that holds on these things in repositories for you.

  - register a github account

    https://github.com/signup

  - set up git on linux, mac and windows

    we need git in the terminal

  - SSH keys

    Google "github ssh keys"

    로컬 컴퓨터에서 커밋을 하기위해 SSH키가 필요하다. 그렇지않으면 커밋을 항상 github interface를 사용하여 해야하는 번거로움.

    you can actually commit your work without setting up ssh keys on your computer you can always go to github and actually commit your work right on github itself like you can write some text and then change that text right in the github interface like the web interface. so then they will do all of that work for you because they will commit it from kind of like their key their own ssh keys. but if you on your computer want to be able to commit your work from your hard disk or your ssc or whatever into github you will need something called ssh keys.

    ssh keys are cryptographically signed pieces of signature that will **allow you to identify yourself as a person or as a committer**. 

    so ssh key is a piece of key that is a signature that you as a developer or a committer of code create on your computer and whenever you make a commit and you wanna send that commit then to github then github knows who you are. so you need your ssh key set up.

    https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

- SSH Keys vs. GPG Signature

  One is to authenticate against GitHub, the other is to sign a commit.

  GPG(GNU Privacy Guard) was new privacy piece of software that you download on your computer.

  when you sign your commits with you ssh key with your private key and then you push your changes to github and github just verifies okay this commit is comming from someone who has access to this repository. when you create your GPG keys and then you sign your commits with the GPG keys then that actually verifies that you are who you say you are. so a lot of software developers are still continuing with ssh keys and to be honest with you that's not good enough because anybody getting a hold of your ssh keys can literally just do anything they want with your commits and change anything they want but with the GPG keys you'll ensure that you are who you are and anyone else even if they have hold of like your ssh keys their commits won't be signed as you.

- GPG and why you need it

  https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

  ```
  Git은 암호학적으로 안전하지만 완벽하지는 않습니다. 인터넷에서 다른 사람의 작업을 가져오고 커밋이 실제로 신뢰할 수 있는 소스에서 온 것인지 확인하려는 경우 Git에는 GPG를 사용하여 작업에 서명하고 확인하는 몇 가지 방법이 있습니다
  ```

  - gpg download

    https://gnupg.org/download/

    ![image-20230202155541920](https://user-images.githubusercontent.com/77393619/216258802-d92ab904-c39c-4686-b0bc-375da215e2dc.png)

- Set up GPG for GitHub

  https://docs.github.com/en/authentication/managing-commit-signature-verification

  ![image-20230202155717409](https://user-images.githubusercontent.com/77393619/216258808-89637797-b56e-4339-a207-13383b899b54.png)

- GitHub repo for our project

  Let's create a repository for our project's code

  `.gitignore` is a file that dictates to get on your computer or on the computer of whoever has cloned your repository about what files shuold not be committed to your git repository.

  - `git init .` make our local repository a Git repository

  - `git push` 하기전에 push 목적지를 설정해주어야 한다.

    `git remote add <name> <url>` and then push using the remote name `git push <name>`

    `git remote add origin <복사한 레포주소>`를 하고 `git push`를 하면되는데

    `git push --set-upstream origin main`을 해주면 this main branch which is on your local computer is actually mapping to the main branch on github. you don't have to do this complicated code you could actually say `git push -u origin HEAD` and that will do the same thing for you.
- Tagging

  `git tag "step-1"` 

  `git push --tags` push to tags to github server

- Verify that our commit it signed

  gpg키 사용하면 github에서 인증배지 확인이 가능(현재는 인터페이스 변경되었을 수 있음)

## 16. Email verification view

- Pushing VerifyEmailView into the screen

  Push the View into the stack with MaterialPageRoute(causes an error we will fix soon)

  ![image-20230207104647769](https://user-images.githubusercontent.com/77393619/217169217-c2effe6f-9782-4048-a96e-8cc840fa94ff.png)

  builder function is in itself a widget that performs a future and once that future is done or errors out or whatever then it calls the builder function and the builder function it is expected to return that builder function itself is expected to return a widget

- CTA Button and text

  Display Column, Text and a TextButton to send verification email

  ```dart
  TextButton(
      onPressed: () async {
          final user = FirebaseAuth.instance.currentUser;
          await user?.sendEmailVerification();
      },
      child: Text('Send email verification')),
  ```

  클릭시 가입했던 이메일로 인증을위한 메일이 전송된다.

- Change LoginView and RegisterView

  They shouldn't return a Scaffold, that's the of HomePage

- Return LoginView in HomePage

  if user is not logged in, return LoginView

## 17. Link between login and register views

- We need to go between views

  right now they are not linked and need manual display.

- Register button on login view

  Add a TextButton to login view to send us to register view

- Named routes

  https://docs.flutter.dev/cookbook/navigation/navigation-basics

  anonymous routes are not as reusable

- Define login and register routes

  in main.dart, define /login/ and /register/

- Go from login to register view

  Using `Navigator.of(context).pushNamedAndRemoveUntil`

  ![image-20230207130850798](https://user-images.githubusercontent.com/77393619/217169220-0134737a-7502-4967-92de-25d268e6ad74.png)

  error for lack of scaffold. 이동하려는 페이지가 Scaffold구조로 이루어져있어야한다.

- Move verify email view to its own file

  lib/views/verify_email_view.dart

## 18. Logout View

- Main UI of the app

  https://api.flutter.dev/flutter/material/AppBar-class.html

- Return NotesView in HomePage

  We shouldn't have any print in HomePage
- We need popup items enumeration(soon)

  An enumeration that describes our popup menu items

- PopupMenuButton vs. PopupMenuItem

  They are usually used together

- PopupMenuItem has a value

- Add your popup menu button

  ```dart
  enum MenuAction { logout }
  ```

  `PopupMenuButton<MenuAction>`

  ```dart
  PopupMenuButton<MenuAction>(
      onSelected: (value) {},
      itemBuilder: (context) {
          return const [
              PopupMenuItem<MenuAction>(
                  value: MenuAction.logout, child: Text('Log out'))
          ];
      },
  )
  ```

  ![image-20230208134034035](https://user-images.githubusercontent.com/77393619/217567749-321fb4c8-c946-4e69-8a95-d5fa6f8c7a3d.png)

- print vs. log(12:45:00)

  print is usually called a poor man's debugger. 디버거 자체가 속도가 너무 느리거나 디버깅 자체에 시간이 지체되는 경우 미봉책으로 할 수 있는 방안이 print라고 볼 수 있는데 poor man's debugger라고 불리는 이유는 it actually place in your code so sometimes print isn't the desirable thing to do. in banking applications for instance you should be extremly careful what you print.

  다른 방법으로 log가 존재.

  ```dart
  import "dart:developer" as devtools show log;
  
  devtools.log(value.toString());
  ```

  more trustworthy and more even configurable version of print.

  `show log` : 해당 패키지에서 특정 기능만을 사용하기위해서 사용(이경우엔 `log` 기능만 특정지어서 사용하기위해서 `show` 키워드를 사용)

  `as devtools`  : 해당 프로젝트 내부에서만 임의로 이름을 정해서 사용할 경우 `as`를 쓸 수 있다.(이 경우에는 dart:developer 패키지에서 가져오는 기능을 devtools 이름을 쓰면서 사용하겠다는 의미) 따라서 `devtools.log`와 같이 사용할 수 있다.

- Tapping on "sing/log out" should display dialog

  We can use showDialog and AlertDialog

- Let's display our dialog upon logout

  Using our PopupMenuButton.onSelected callback and await on our dialog

- Log out from firebase

  `await FirebaseAuth.instance.signOut();`

  and go back to login view upon logging out `Navigator.of(context).pushNamedAndRemoveUntil('/login/')`

## 19. New route for NotesView

- add a new route

  called `'/notes'` that goes to NotesView

  :bulb: **the main function does not get recompiled when you do a hot reload** 따라서 main.dart를 수정할 경우 **hot restart**해줘야한다. 

- Avoid hardcoding everywhere(13:36:00)

  What is hardcoding and why programmers don't like that

  so let's put our route names in one file `lib/constants/routes.dart`

  Define 3 constants, loginRoute, registerRoute and notesRoute

## 20. Error handling in login view

- We need a generic dialog function

  `future<void> showErrorDialog(context, String text)`

  what we need to do is create dialog and then display it.

- Handle other Firebase authentication example

  You can use `e.code` to get the error code

- handle other errors that might arise

  Use `e.toString()` and call the same function

- commit and tag

  ```
  git add --all
  git commit -m "step-6"
  git tag "step-6"
  git push
  git push --tags
  ```

## 21. Error handling in register view

we need error handling in register view and go to next screen after registration

- Use showErrorDialog instead of log

- We need to confirm email

  After every registration, we need to confirm the user's email

- show confirm view(push, don't replace)

  After successful registration, show verifyEmailRoute

- Let's send confirmation email after registration

  In register_view, directly after registering, send a verification email

  ```dart
  try {
      final userCredential = await FirebaseAuth.instance
          .createUserWithEmailAndPassword(
          email: email, password: password);
      final user = FirebaseAuth.instance.currentUser;
      await user?.sendEmailVerification();
      Navigator.of(context).pushNamed(verifyEmailRoute);
  }
  ```

- Add restart button

  Add restart button to end of verify email view and sign the user out with `FirebaseAuth.instance.signOut()`

  and send user to register page by `Navigator.of(context).pushNamedAndRemoveUntil()`

- login

  We can login with a user who hasn't confirmed thefir email (we will fix this soon)

## 22. Confirming Identity Before Going to Main UI

- Users need to verify email before going to the main UI

- Check if user is verified

  Add an if-statement in login_view right after signInWithEmailAndPassword

## 23. Auth Service

- Auth provider and auth service

  We need an auth provider abstract class and AuthService

- Let's clean up our exceptions first

  Create file `lib/services/auth/auth_exceptions.dart`

- UserNotFoundAuthException

  Add it in `lib/services/auth/auth_exceptions.dart`

- Create auth userdart file

  `lib/services/auth/auth_user.dart`

- Import the Firebase user

  `import 'package:firebase_auth/firebase_auth.dart' show User;`

- AuthUser class

  AuthUser with isEmailVerified field

  ```dart
  @immutable
  class AuthUser {...}
  ```

  `@immutable` : like an annotation telling that this class and any subclasses of this class are going to be immutable meaning that their internals are never going to be changed upon initialization.

  해당 키워드를 사용한 클래스 혹은 클래스의 하위클래스는 immutable하다는 것. immutable한 field만 가질 수 있다.

- We need a factory initializer(15:17:00)

  facotry `AuthUser.fromFirebase(User user) => AuthUser(user.emailVerified)`

  we need a factory constructor that creates our auth user from a firebase user and factory constructors  are really useful for this purpose

  ```dart
  @immutable
  class AuthUser {
      final bool isEmailVerified;
      const AuthUser(this.isEmailVerified);
  
      factory AuthUser.fromFirebase(User user) => AuthUser(user.emailVerified);
  }
  ```

- We also need an auth provider

  `lib/services/auth/auth_provider.dart`

  It can provide us with the current user now. Remember that we've abstracted away the firebase user with our own auth user which we just created(방금 생성한 자체 인증 사용자를 사용하여 firebase 사용자를 추상화했습니다.)

  and import our auth user

  `import 'package:learningdart/services/auth/auth_user.dart';`

- We shoulb be able to get the current user

  `AuthUser? get currentUser;`

- We need a login function

  `Future<AuthUser> login()`

- We also need a function to create a new user

  `Future<AuthUser> createUser()`

- we should be able to log out as well

  `Future<void> logOut()`

- we also need to be able to send a verification email

  `Future<void> sendEmailVerification()`

- Now we implement a concrete class of our auth providier

  `lib/services/auth/firebase_auth_provider.dart`

  then we create our class

  `class

- Implementing sendEmailVerification

  `Future<void> sendEmailVerification() async`

- We need an auth service

  Our auth service should implement AuthProvider

- Create the basic AuthService class

  `class AuthService implements AuthProvider`

  why ? It relays the messages of the given auth provider, but can have more logic

- From AuthService, delegate to AuthProvider

  We might then need additional logic later on our auth service

## 24. Migrating to Auth Service

we need to migrate our existing code to using our own auth service

- AuthService.firebase

  we need this so we don't have to instantiate it everywhere

- Add firebase factory to Auth Service

  `  factory AuthService.firebase() => AuthService(FirebaseAuthProvider());`

- We need to clean up MenuAction and NotesView

  They are just in main.dart right now

- Moving MenuAction

  Move MenuAction enum to `lib/enums/menu_action.dart`

## 25. Unit Testing our Auth Service :star2:

- Why do we need unit tests(16:37:00 ~)

  Our auth service has no tests. We need to guard ourselves against unintentional edits.

- TDD(Test Driven Development)

  Tests need to always be written before code, not the other way around

- Time limits

  We aren't going to go too deep into tests because of time limits. basic한 부분한 진행할 예정

- Different types of tests

  **Unit, widget and integration tests**

- widget test

  some sort of like an end to end test. `ui > service > provider > firebase > firebase backend > services > ...`

- mocking

- dev dependencies

  Not used in the final product. 즉, 개발시에만 사용되고 실제 배포되는 product 상에는 포함되지않는 dependencies

- We need our test dependencies

  `flutter pub add test --dev`

- Delete existing tests

  Delete `test/widget_test.dart` and create `test/auth_test.dart`

- Main function of tests

  In `auth_test.dart` add `void main() {}`

- Let's recompile

  when you bring in a new dependency in your project you need to always ensure that you rebuild your project.

- Make `isEmailVerified` required

  Go to AuthUser and make the isEmailVerified required beause it's not otherwise clear when we construct it.

- We need a mock auth provider

  Why do we use mocks

- Add MockAuthProvidier

  In `test/auth_test.dart`

  - Mock createUser

    `Future<AuthUser> crateUser`

  - Mock currentUser(17:10:00)

    `AuthUser? get currentUser => _user;`

  - Mock initialize

    `Future<void> initialize() async`

  - Mock login

    `Future<AuthUser> login`

  - Mock logOut

    `Future<void> logOut() async`

  - Mock sendEmailVerification

    `Future<void> sendEmailVerification() async`

- test groups

  For grouping together similar tests

  you can actually group your test functionalities into a group that has a name and then you can ask flutter to run that entire group of tests for you.

  - Create your mock provider

    Do this in the main() function of your tests

    ```dart
    void main() {
        group('desc', () {});
    }
    ```

    we're gonna create an instance of our mock Auth provider

  - Testing `provider.isInitialized`

    Provider shouldn't be initialized to begin with

  - Test logging out before initialization

    The provider should throw a NotInitializedException

  - Testing provider initialization

    `provider.isInitialized`

  - Testing null user to begin with

    The user should be null upon initialization

  - Testing time required to initialize

    We can user timeouts in this case

  - Test creating a user

    And Test all edge cased that might occur

  - Test email verification

    A logged in user should be able to send email verificaiton

  - Test logging out and in again

    This is a normal scenario that should just work.

  - Now run your tests

    `flutter test test/auth_test.dart`

## 26. CRUD Local Storage

We need a database to store user notes before we use Firebase for storage(17:43:40 ~ )

- What is SQLite

  database or a library created in C that allows us to see as a language c that allows to store data inside a file.

  just think of SQLite as the databse engine that we're going to use in our application and it's not something that is built in inside flutter we will have to use a so-called plug-in for it. but that's okay I mean not many languages have support for talking with a database and natively so but we'll get to that point.

  how we're actually going to integrate with sqlite and to start with.

- DB Browser

  Let's download DB Browser for SQLite

  a free program called DB Browser for SQLite. If you think of SQLite has different components first you have your database which is just a file that sits on a disk and then you will have the sqlite engine that can read from this file and write to this file so that's the engine and then this engine should run somewhere so it's either going to run inside an application such as the one here a DB Browser for SQLite. so SQLite's like baked into that applicaiton or you can also bring SQLite into your terminal so that you can actually talk with SQLite databases from within your terminal.

  SQLite is the engine that talks to the SQLite files which are your databases but then it this engine should run somewhere. it's not just an executable that like you say here take this file you now have some sort of a container where the SQLite engine basically resides.

  we're going to bring this engine into the flutter application so our app can talk with that database. but for now we're going to look at a program called db browser for SQLite.https://sqlitebrowser.org/

- Creating our user table

  `CREATE TABLE IF NOT EXISTS "user" ...`

  ![image-20230215153753301](https://user-images.githubusercontent.com/77393619/218953348-bef94e1b-4067-4d45-87b5-fee327caaefd.png)

  `NN` : Not Null. this field should always be present. it should never allow the value emptiness of the value or the absence of a value to be present there.

  `PK` : Primary Key. it is the key using which is a unique key in this table using which we should be able to then easily query different users from this table.

  `AI` : Auto Increment. it is a great functionality in SQLite and many other databases that allows you as the name suggests and the name indicates that by you creating for instance a user with a specific email and you insert that user into the database in this table and you don't even have to assign an id to that user you just say here is the user email 'boo' put it in the database then SQLite is smart enough to oh but I need an id field as well you haven't provided it and then it looks at the field and says oh id is auto increment so it's going to create that id for you and increment the previously generated id and assign the new id to your object. for instance if you have no objects inside this table and then you add a new user then it automatically gets the id of zero. and then if you generate the next user and put it in there then it will get the id of one.

  ![image-20230215154354163](https://user-images.githubusercontent.com/77393619/218953362-cbb6d5e6-94ac-4b4f-97f8-d873d0fbcca1.png)

  `U` : Unique. this filed needs to be unique. but if you indicate something as primary key implicitly it is a unique field.(18:00~)

- creating note table

  user_id는 user table id field와 bind된다. foreign key

  ![image-20230217100313397](https://user-images.githubusercontent.com/77393619/219594346-b6c3933b-6643-4d06-a2b0-23ddadcef9e4.png)

  `is_synced_with_clud`가 0(기본값)이라면 sync되지 않은 것.

  ![image-20230217100605965](https://user-images.githubusercontent.com/77393619/219594356-6da2ddd1-1746-4dd3-9de5-cc31167bd3fc.png)

- Creating these programmatically

  We need to create this programmatically otherwise we have to move it to docs folder manually

  we have a file called testdb. it has the database for our application with some tables. however we need to able to create these tables programmatically if they don't exist inside our application. now this testDB has absolutely nothing to do with our flutter application. and you could drag this db into your flutter application and then copy it to the right place when the application is executed in the user's telephone on the tablet and then try to read from that database it is possible.

  이러한 과정을 flutter application에서 진행해볼거다. how can you integrate with sqlite inside your flutter application.

- We need a few dependencies

  그러기위해서는 dependencies를 받아줘야하는데. `flutter pub add => sqflite, path_provider, path`

  - `sqflite` : For storage of our data.

    it is a package it's a third party package that we need to add to our application in order for our flutter application to be able to talk with sqflite.

    so it is a **actual storage and talking with the database**

  - `path_provider` : To get our app's documents directly for database storage.

    path is used for us to be able to grab the applications documents folder so that we can actually create a file inside a documents folder and place our data inside that file just like we placing the data for note and user inside the testDB file.

    path_provider **allows us to grab the applications documents folder**. if you're not familiar with mobile application development, you may not know this but applications that sit on an android phone etc they have their own file structure. so every application in itself has a document directory so whereas on your computer you have a documents folder that other applications that run on your operating system could get access to. so it's one documents folder every application can request access to and store information in it and read from it. But that's not the same concept in mobile devices and on tablets in that every application runs inside something called sandbox.

    sandbox is like a cage inside where the application resides and all the application data resides in that sandbox. so every application can request access from the operating system to read its own documents folder.

    it **allows to find our applications documents folder**

  - `path` : It has a useful "join" function

    `path_provider`를 통해서 application documents folder에 접근하면 we want to create a file in this documents folder and get the full path of this file documents folder/file.  and that's what we need the path package because **it has a great function called `join`  that allows us to take the path of a directory or folder** and join that path with a file name and it gives us the entire path back so we can access the file.

  - 모두 pub dev를 통해 받아주고 `pubspec.yaml`파일에서 확인해보자.

    `flutter pub add sqflite`

    `flutter pub add path_provider`

    `flutter pub add path`

    ![image-20230217102943199](https://user-images.githubusercontent.com/77393619/219594361-b451a7db-466b-4b0c-a74b-66e131bd8f09.png)

- Create our `notes_service.dart` file

  `lib/services/crud/notes_service.dart`

  이걸로 basically grab a hold of our database it is **the primary service that is gonna work with our sqlite database**. it's gonna grab users, create new users, delete users, find users, create notes, delete notes, update notes ... everything we need from our user interface this notes service is going to facilitate(가능하게 하다) that for us

- import our dependencies

  Import all 3 dependencies in `notes_service.dart`

  ```dart
  import 'package:sqflite/sqflite.dart';
  import 'package:path_provider/path_provider.dart' show getApplicationDocumentsDirectory;
  import 'package:path/path.dart' show join;
  ```

- We need to construct our db path

  User `path` and `path_provider` to do that

  we need to **grab a hold of our current database path**. every application that you develop with flutter for mobile devices such as android, ios, ipad os they have their own documents directory and we're going to create and get the path the documents directory and then we're going to join that using `path` dependency with a name that we are going to specify for our database.

- We need database users

  Create `DatabaseUser` class inside `notes_service.dart`

  ```dart
  @immutable
  class DatabaseUser {
    final int id;
    final String email;
  
    const DatabaseUser({
      required this.id,
      required this.email,
    });
  
    // this is a row inside the user table
    // Map<String, Object?>
    DatabaseUser.fromRow(Map<String, Object?> map)
        : id = map[idColumn] as int,
          email = map[emailColumn] as String;
      /*
    covariant allows you to change the behavior of your input parameters so that they do
    not necessarily confirm to the signature of that parameter in the super class.
    we're doing override here meaning that there this functionality operator is already defined
    at the object level.
    so if you don't put covariant in here you'll get an error from the analyzer.
    in here we're saying that we're going to compare our class with == and instance of our class with ==
    and we're going to compare with another user of the same class.
    이후 covariant는 지워준다.
   */
      @override
      bool operator ==(covariant DatabaseUser other) => id == other.id;
  }
  
  const idColumn = "id";
  const emailColumn = "email";
  ```

  covariant 삭제시

  ![image-20230217105604859](https://user-images.githubusercontent.com/77393619/219594363-971c56ef-1385-4c1c-8ae4-03f175b0084e.png)

  ```dart
  /* error saying that accoring to object == should compare the current object with another object
    but using covariant you're telling dart that hey I'm not comparable with other objects of any other class
    I'll only comparable with database user instances so make that happen.
    so then after you implement == you have to also implement hascode as is suggetsted by the analyer. */
  @override
  bool operator ==(DatabaseUser other) => id == other.id;
  ```

  ![image-20230217105640779](https://user-images.githubusercontent.com/77393619/219594364-0e208669-7690-49a4-b543-cc05aa18e41e.png)

  ```dart
  @override
  bool operator ==(covariant DatabaseUser other) => id == other.id;
  
  /*
    we're just going to return our id's hashcode
    this basically the id is becoming the primary key of this class using which it will hash itself
    so it can be placed inside maps or hash node
  */
  @override
  int get hashCode => id.hashCode;
  ```

- We also need a class for our notes

  Create `DatabaseNote` class inside `notes_service.dart`

  만들기전 table field확인

  ![image-20230217110109097](https://user-images.githubusercontent.com/77393619/219594368-4dbcd5ae-da13-4758-a0cc-0d77ac2d0541.png)

  :star: SQLite convention은 field 이름에 camelCase를 사용하지않고 `user_id`와 같이 작성한다. 다만 flutter에서 해당 변수를 사용할 경우 `userId`와 같이 받아온다.

  ```dart
  class DatabaseNote {
      final int id;
      final int userId;
      final String test;
      // remember we're not going to user this input cloud it's just for you to understand we create different fields in the database.
      final bool isSyncedWithCloud; 
  
      DatabaseNote(this.id, this.userId, this.test, this.isSyncedWithCloud);
  }
  ```

  override, initialize

  ```dart
  class DatabaseNote {
      final int id;
      final int userId;
      final String text;
      final bool isSyncedWithCloud;
  
      DatabaseNote({
          required this.id,
          required this.userId,
          required this.text,
          required this.isSyncedWithCloud,
      });
      DatabaseNote.fromRow(Map<String, Object?> map)
          : id = map[idColumn] as int,
      userId = map[userIdColumn] as int,
      text = map[textColumn] as String,
      isSyncedWithCloud =
          (map[isSyncedWithCloudColumn] as int) == 1 ? true : false;
  
      @override
      String toString() => 'Note, Id = $id, userId = $userId, isSyncedWithCloud = $isSyncedWithCloud, text = $text';
  
      @override
      bool operator ==(covariant DatabaseNote other) => id == other.id;
  
      @override
      int get hashCode => id.hashCode;
  }
  
  const idColumn = "id";
  const emailColumn = "email";
  const userIdColumn = "user_id";
  const textColumn = "text";
  const isSyncedWithCloudColumn = "is_synced_with_cloud";
  ```

- Let's make sure we have all our constants in place

  DB name, column and table names

  ```dart
  const dbName = "notes.db";
  const noteTable = "note";
  const userTable = "user";
  ```

- Let's open our DB

  `Future<void> open() async`

  ```dart
  Future<void> open() async {
      if (_db != null) {
          throw DatabaseAlreadyOpenException();
      }
      try {
          final docsPath = await getApplicationDocumentsDirectory();
          final dbPath = join(docsPath.path, dbName);
          final db = await openDatabase(dbPath);
          _db = db;
          // create the user table
          await db.execute(createUserTable);
          // create the note table
          await db.execute(createNoteTable);
      } on MissingPlatformDirectoryException {
          throw UnableToGetDocumentDirectory();
      }
  }
  const createUserTable = '''CREATE TABLE IF NOT EXISTS "user" (
    "id"	INTEGER NOT NULL,
    "email"	TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT)
  );
  ''';
  
  const createNoteTable = '''CREATE TABLE IF NOT EXISTS "note" (
    "id"	INTEGER NOT NULL,
    "user_id"	INTEGER NOT NULL,
    "text"	TEXT,
    "is_synced_with_cloud"	INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("user_id") REFERENCES "user"("id")
  );
  ''';
  ```

- Closing the DB

  `Future<void> close() async`

  ```dart
  Future<void> close() async {
      final db = _db;
      if (db == null) {
          throw DatabaseIsNotOpen();
      } else {
          await db.close();
          _db = null;
      }
  }
  ```

- Convenience function for getting current DB

  `Database _getDatabaseOrThrow() {}`

  ```dart
  Database _getDatabaseOrThrow() {
      final db = _db;
      if (db == null) {
          throw DatabaseIsNotOpen();
      } else {
          return db;
      }
  }
  ```

- Allowing users to be deleted

  `Future<void> deleteUser({required String email}) async`

  ```dart
  Future<void> deleteUser({required String email}) async {
      final db = _getDatabaseOrThrow();
      final deltedCount = db.delete(
          userTable,
          where: 'email = ?',
          whereArgs: [email.toLowerCase()],
      );
      if (deltedCount != 1) {
          throw CouldNotDelteUser();
      }
  }
  ```

- Allowing users to be created

  `Future<DatabaseUser> createUser({required Stirng email}) async`

  ```dart
  Future<DatabaseUser> createUser({required String email}) async {
      final db = _getDatabaseOrThrow();
      final results = await db.query(
          userTable,
          limit: 1,
          where: 'email = ?',
          whereArgs: [email.toLowerCase()],
      );
      if (results.isNotEmpty) {
          throw UserAlreadyExists();
      }
  
      final userId = await db.insert(userTable, {
          emailColumn: email.toLowerCase(),
      });
  
      return DatabaseUser(id: userId, email: email);
  }
  ```

- Ability to fetch users

  `Future<DatabaseUser> getUser({required String email}) async`

  ```dart
  Future<DatabaseUser> getUser({required String email}) async {
      final db = _getDatabaseOrThrow();
      final results = await db.query(
          userTable,
          limit: 1,
          where: 'email = ?',
          whereArgs: [email.toLowerCase()],
      );
      if (results.isEmpty) {
          throw CouldNotFindUser();
      } else {
          return DatabaseUser.fromRow(results.first);
      }
  }
  ```

- Allow creation of new notes

  `Future<DatabaseNote> createNot({required DatabaseUser owne}) async`

  ```dart
  Future<DatabaseNote> createNote({required DatabaseUser owner}) async {
      final db = _getDatabaseOrThrow();
  
      // make sure owner exists in the database with the correct id
      final dbUser = await getUser(email: owner.email);
      if (dbUser != owner) {
        throw CouldNotFindUser();
      }
      const text = '';
      // create the note.
      final noteId = await db.insert(noteTable, {
        userIdColumn: owner.id,
        textColumn: text,
        isSyncedWithCloudColumn: 1,
      });
  
      final note = DatabaseNote(
        id: noteId,
        userId: owner.id,
        text: text,
        isSyncedWithCloud: true,
      );
      return note;
    }
  ```

- Allow notes to be deleted

  `Future<void> deleteNote({required int id}) async`

  ```dart
  Future<void> delteNote({required int id}) async {
      final db = _getDatabaseOrThrow();
      final deltedCount = await db.delete(
          noteTable,
          where: 'id = ?',
          whereArgs: [id],
      );
      if (deltedCount == 0) {
          throw CouldNotDelteNote();
      }
  }
  ```

- And ability to delete all notes

  `Future<int> deleteAllNotes() async`

  ```dart
  Future<int> deleteAllNotes() async {
      final db = _getDatabaseOrThrow();
      return await db.delete(noteTable);
  }
  ```

- Fetching a specific note

  `Future<DatabaseNote> getNote({required int id}) async`

  ```dart
  Future<DatabaseNote> getNote({required int id}) async {
      final db = _getDatabaseOrThrow();
      final notes = await db.query(
          noteTable,
          limit: 1,
          where: 'id = ?',
          whereArgs: [id],
      );
      if (notes.isEmpty) {
          throw CouldNotFindNote();
      } else {
          return DatabaseNote.fromRow(notes.first);
      }
  }
  ```

- Fetching all notes

  `Future<Iterable<DatabaseNote>> getAllNotes() async`

  ```dart
  Future<Iterable<DatabaseNote>> getAllNotes() async {
      final db = _getDatabaseOrThrow();
      final notes = await db.query(noteTable);
  
      return notes.map((noteRow) => DatabaseNote.fromRow(noteRow));
  }
  ```

- Updating existing notes

  `Future<DatabaseNote> updateNote`

  ```dart
  Future<DatabaseNote> updateNote(
      {required DatabaseNote note, required String text}) async {
      final db = _getDatabaseOrThrow();
  
      await getNote(id: note.id);
  
      final updatesCount = await db.update(noteTable, {
          textColumn: text,
          isSyncedWithCloudColumn: 0,
      });
      if (updatesCount == 0) {
          throw CouldNotUpdateNote();
      } else {
          return await getNote(id: note.id);
      }
  }
  ```

- Let's put all our CRUD exceptions in one file

  `lib/services/crudcrud_exceptions.dart`

  and just import and change existing code

  ```dart
  class DatabaseAlreadyOpenException implements Exception {}
  class UnableToGetDocumentDirectory implements Exception {}
  class DatabaseIsNotOpen implements Exception {}
  class CouldNotDelteUser implements Exception {}
  class UserAlreadyExists implements Exception {}
  class CouldNotFindUser implements Exception {}
  class CouldNotDelteNote implements Exception {}
  class CouldNotFindNote implements Exception {}
  class CouldNotUpdateNote implements Exception {}
  ```

- next chapter

  now we need a stream of notes to display in our app UI

  we've done a lot of work on the data so we need to fuse it together with our UI. and in order to do that we need to talk about streams and stream controllers.

## 27. Working with Streams in Notes Service

- Caching data

  We need the stream and stream controller to cache data.

  - `stream` is just a point of time or basically an entity that controls data. just something that keeps hold data. then you perform things on it like add this data, remove this data .. so it keeps hold of its data and it has a timeline so it starts at some point manipulates its data and then it either errors out at the end saying that I can't do this and it just dies.

    so just think of streams as **pipes of data types of information** that you can manipulate and you can also perform operations on.

  - `stream controllers` is your interface to your streams. stream controllers를 통해서 stream의 data를 수정하고 가져올 수 있다. 

- Local list of fetched notes

  `List<DatabaseNote> _notes = [];`

  goal for the note servers to be able to expose a list of notes that the ui can then render on this on the user screen. if the user goes and presses the plus button then that plus button is then gonna send a message here to our note servers we're going to then go to this function createNote and  this function internally is then gonna manipulate that list of notes inside note service hey here's a new note add that and then our ui is going to listen to a list of these notes available in note service and if things change in that list then the ui is just going to automatically update itself. and this interface between the ui and the note servers is going to be done through a stream.

- StreamController(19:41:00 ~)

  `final _notesStreamController = StreamController<List<DatabaseNote>>.broadcast();`

  what we need is for the note service to be able to control a stream of notes. so when the list of this notes changes we need to tell our stream in the note servers that hey some element got added, deleted ... then the ui can then reactively listen for these changes in the note service and we that through the our stream controller 

  ```dart
  final _notesStreamController =
      StreamController<List<DatabaseNote>>.broadcast();
  ```

  broadcast : it's okay for us to create new listeners that listen to the changes to this stream controller.

- Reading and caching notes

  `Future<void> _cacheNotes() async`

  read all the available notes from our database and then cache them inside both the notes cache right here and our controller.

  so you see what our goal in this chapter is to make sure that this is the source of truth that our notes list contains all the notes for for instance the current user. then the `stream controller` is our **interface to the outside world. the UI is going to be listening to changes that occur in this stream controller.**

  so whenever you see **`_notes`, this is not something that's going to be read from the outside**. **everything's going to be read from the outside through `_notesStreamController`.**

  ![image-20230217162650829](https://user-images.githubusercontent.com/77393619/219594537-48b1062e-a7f0-45e6-991f-fb82e78de5b5.png)

  - so we create function called `_cacheNotes`

    its purpose is just to read all the notes from the database and place it both in here internally and in our note stream controller which is going to be read externally.

    ```dart
    Future<void> _cacheNotes() async {
        final allNotes = await getAllNotes();
        // iterable to list
        _notes = allNotes.toList();
        _notesStreamController.add(_notes);
    }
    ```

- Read all notes upon opening DB

  In open(), call _cacheNotes

  ```dart
  Future<void> open() async {
      if (_db != null) {
          throw DatabaseAlreadyOpenException();
      }
      try {
          // ...
          await _cacheNotes();
      } on MissingPlatformDirectoryException {
          throw UnableToGetDocumentDirectory();
      }
  }
  }
  ```

- Cache note in createNote

  In createNote, add the new note to _notes and _notesStreamControlller

  ```dart
  Future<DatabaseNote> createNote({required DatabaseUser owner}) async {
      // ...
      _notes.add(note);
      _notesStreamController.add(_notes);
  
      return note;
  }
  ```

- Delete note from cache in deleteNote()

  `_notes.removeWhere((note) => note.id == id);`

  ```dart
  Future<void> delteNote({required int id}) async {
      // ...
      if (deltedCount == 0) {
          throw CouldNotDelteNote();
      } else {
          _notes.removeWhere((note) => note.id == id);
          _notesStreamController.add(_notes);
      }
  }
  ```

- Invalidate cache upon deleteAllNotes()

  `Future<int> deleteAllNotes() async`, delete cache as well

  ```dart
  Future<int> deleteAllNotes() async {
      final db = _getDatabaseOrThrow();
      final numberOfDeletions = await db.delete(noteTable);
      _notes = [];
      _notesStreamController.add(_notes);
      return numberOfDeletions;
  }
  ```

- Update cache in getNote({required int id}) (19:54 ~)

  Remove old note with same id and add the new one and update stream

  ```dart
  Future<DatabaseNote> getNote({required int id}) async {
  	// ...
      if (notes.isEmpty) {
          throw CouldNotFindNote();
      } else {
          final note = DatabaseNote.fromRow(notes.first);
          _notes.removeWhere((note) => note.id == id);
          _notes.add(note);
          _notesStreamController.add(_notes);
          return note;
      }
  }
  ```

- Update the cache in updateNote()

  `Future<DatabaseNote> updateNote`, update _notes and stream

  ```dart
  Future<DatabaseNote> updateNote(
      {required DatabaseNote note, required String text}) async {
      final db = _getDatabaseOrThrow();
  
      // make sure note exists
      await getNote(id: note.id);
  
      // update DB
      final updatesCount = await db.update(noteTable, {
          textColumn: text,
          isSyncedWithCloudColumn: 0,
      });
  
      if (updatesCount == 0) {
          throw CouldNotUpdateNote();
      } else {
          final updatedNote = await getNote(id: note.id);
          _notes.removeWhere((note) => note.id == updatedNote.id);
          _notes.add(updatedNote);
          _notesStreamController.add(_notes);
          return updatedNote;
      }
  }
  ```

- Get or create user in notes_service.dart

  `Future<DatabaseUser> getOrCreateUser({required String email}) async`

  ```dart
  Future<DatabaseUser> getOrCreateUser({required String email}) async {
      try {
          final user = await getUser(email: email);
          return user;
      } on CouldNotFindUser {
          final createdUser = await createUser(email: email);
          return createdUser;
      }
  }
  ```

- next chapter

  Upon logging in , we need to call our getOrCreateUser() function and have the user ready
  
## 28. Preparing Notes View to Read All Notes

- We have almost everything in place

  so we can strat reading notes in our UI

- Our AuthUser doesn't have an email

  we need an email field to create the user in our DB

- Email in AuthUser

  Add `final String? email;` to AuthUser

- Read current user's email field in notes_view.dart

  `String get userEmail => AuthService.firebase().currentUser!.email!;`

- open DB

  `void ininState() in notes_view.dart`

  ```dart
  @override
  void initState() {
      _notesService = NoteService();
      _notesService.open();
      super.initState();
  }
  ```

- close DB

  `void dispose() in notes_view.dart`

  ```dart
  @override
  void dispose() {
      _notesService.close();
      super.dispose();
  }
  ```

- We need the DB to be open

  Before any operation on the DB, it should be open

- Add check in notes_service for db opening

  `Future<void> _ensureDblsOpen() async`

- Use _ensureDbIsOpen()

  Make sure all operations use `_ensureDbIsOpen`

- FutureBuilder and AsyncSnapshot

  `FutureBuilder` subscribes to a future that wil return its value in the future if you're familiar with javascript then you'll know it as promises.

  so FutureBuilder allows you to submit a future and it will allow you to submit a builder meaning that it takes that chunk of code that produces a value as a future.

  FutureBuilder that subscribes itself to the value that is returned by function and then it will tell us about various updates. and these various updates are going to be provided to us as something called an AsyncSnapshot.

  `AsyncSnapshot` is a wrapper as a snapshot around an asynchronous functionality.

- Return FutureBilder in notes_view.dart

  FutureBuilder of _notesService.getOrCreateUser(email: userEmail)

- We need a way of grabbing all notes

  we can achieve this with our stream controller

- Get all notes in notes_service.dart

  `Stream<List<DatabaseNote>> get allNotes => _notesStreamController.stream`

- StreamBuilder inside FutureBuilder

  In notes_view.dart, user StreamBuilder to display all notes

- What are .waiting and .done flags? Stream vs. Future

  ![image-20230218142840295](https://user-images.githubusercontent.com/77393619/219849228-8cde9d80-b272-4026-9ba3-e57e94a2c6b4.png)

  both a stream builder and a future builder work with something called an async snapshot.

  ![image-20230218142939478](https://user-images.githubusercontent.com/77393619/219849229-b9971d72-7cd9-493d-a62f-a3f93f1a3e91.png)

  if you're waiting for a future or a stream then you're gonna get `waiting` flag. and it `done` is gonna happen for your a future that has completed its task. but a stream usually it just keeps living so you can't like hook into or you shouldn't hook into the done event for a stream but you should actually hook into your waiting connection state.

  connectionstate for a future and a connection state are waiting for the stream.

- NotesService should be a singleton

  what is a singleton and why do we need it now?

  instance를 여러번 만들어질 수 있지만 App내에서 **단 한번만** 사용되어야하는 instance도 존재한다. 이 경우 재생성되지않도록 코드를 작성해주어야하는데 이러한 방법을 싱글톤패턴이라고 한다.

  **a pattern used in software development where you create a service for instance or a class instance where that class instance is only one inside the entire application.** for instance, note service should only exist as one copy in the entire application. it shouldn't be like made new copies of this note service over and over again. that's what a **singleton** is and what we're going to do with our note service.

- Make NotesService a singleton

  `static final NotesService _shared = NotesService._sharedInstance();`

  ```dart
  // create a private constructor
  static final NoteService _shared = NoteService._sharedInstance();
  NoteService._sharedInstance();
  factory NoteService() => _shared;
  ```

- next chapter

  we are done with the basics of the notes_view but we have no data.

## 29. Preparing to Create New Notes

- Change title of notes_view.dart

  Let's change title to "Your Notes"

  ![image-20230218145018474](https://user-images.githubusercontent.com/77393619/219849232-62ee216c-9a54-4234-9a5c-95935d6f20f3.png)

- Adding a `+` button to our menu

  We can either add + to menu or next to menu

- Adding is an important action

  The + button will sit next to our menu, and not in it.

  중요한 작업이기 때문에 한번에 제 역할을 할 수 있도록 ... 메뉴 옆에 위치시키도록하자. 

  - Create a new file for our view

    `lib/views/notes/new_note_view.dart`

  - Move NotesView

    Move `note_view` under our new folder as well

    ![image-20230218145509226](https://user-images.githubusercontent.com/77393619/219849233-bd966965-ea9d-401a-b04d-77101c166b80.png)

  - Our tests are broken

    We've broken the test since we introduced email into AuthUser, let's fix that.

    ```dart
    // auth_user.dart
    @immutable
    class AuthUser {
      final String? email;
      final bool isEmailVerified;
      const AuthUser({
        required this.email,
        required this.isEmailVerified,
      });
    
      factory AuthUser.fromFirebase(User user) => AuthUser(
            email: user.email,
            isEmailVerified: user.emailVerified,
          );
    }
    ```

    Add email to our tests and run `flutter test test/auth_test.dart` to make sure they still work.

    ![image-20230218145849291](https://user-images.githubusercontent.com/77393619/219849234-61ced949-dc46-4599-9041-f5da0ba54cb4.png)

    ![image-20230218145923675](https://user-images.githubusercontent.com/77393619/219849235-1e50a0ec-f9a8-4677-9508-119c25f26301.png)

  - Add a new route for NewNoteView

    In `main.dart` routes, add newNoteRoute: (context) => const NewNoteView(), and don't forget to import

    ```dart
    // routes.dart
    const newNoteRoute = '/notes/new-note';
    ```

    ```dart
    // main.dart
    void main() {
        WidgetsFlutterBinding.ensureInitialized();
        runApp(MaterialApp(
            title: 'MyApp',
            home: HomePage(),
            routes: {
    			// ...
                newNoteRoute: (context) => const NewNoteView(),
            },
        ));
    }
    ```

    ```dart
    // new_note_view.dart
    import 'package:flutter/material.dart';
    import 'package:flutter/src/widgets/container.dart';
    import 'package:flutter/src/widgets/framework.dart';
    
    class NewNoteView extends StatefulWidget {
      const NewNoteView({super.key});
    
      @override
      State<NewNoteView> createState() => _NewNoteViewState();
    }
    
    class _NewNoteViewState extends State<NewNoteView> {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: const Text('New Note'),
          ),
          body: const Text('Write your new note here...'),
        );
      }
    }
    ```

  - Showing our new widget

    In notes_view.dart, onPressed of icon button show new_note_view

    ```dart
    IconButton(
        onPressed: () {
            Navigator.of(context).pushNamed(newNoteRoute);
        },
        icon: const Icon(Icons.add)),
    ```

- next chapter

  we have the view now, let's create the logic inside it.

## 31. Creating New Notes

- 21:00:18

- what we gonna do

  create an actual note and modify its text and then be able to go back to the main user interface

- Let's first fix our notes_view.dart

  We have to make sure notes_view listens for `ConnectionState.active` as well as  `.waiting`. now we're only listening for the connection state `waiting`. 

  ![image-20230218151439347](https://user-images.githubusercontent.com/77393619/219849236-cd880c14-98e3-41c0-94fe-23462fb5fac0.png)

  if you look at our stream, stream of all notes can either be empty in the beginning or it could contain some notes. let's go with the stream being empty. when the stream is empty meaning that the user hasn't created any notes yet that have been populated in a note service then the connection state of that stream will be **waiting** because dart is now waiting for that stream to return the first value.

  ```dart
  // notes_view.dart
  StreamBuilder(
      stream: _notesService.allNotes,
      builder: (context, snapshot) {
          switch (snapshot.connectionState) {
              case ConnectionState.waiting:
              case ConnectionState.active:
                  return const Text('Waiting for all notes...');
              default:
                  return const CircularProgressIndicator();
          }
      });
  ```

  as soon as the stream actually returns one value then its connection state is gonna be **active** and what we've done is just we waited for waiting state but as soon as it goes to active then we're showing a circular progress indicator and that's not the right logic. so we need to fix that.

  - Keep hold of our current note in new_note_view.dart

    `DatabaseNote? _note;`

    여기서 실제 note를 생성하고 DB에 저장하는 로직을 작성할 건데 로직작성중 저장(Ctrl + s)를 하게되면 hot reload가 되면서 build function을 재실행하기 때문에 매저장시마다 note를 생성하게되므로 이를 막아줘야한다.

    what we're going to do in this new note view upon coming to the screen we are **actually going to create a new note for you.** and keep hold of that new note

    the goal for our new_note_view here is to use future builder inside the body of the function. we're going to say as soon as this new note view state has been created then it also needs to crate a new note in the database.

  - Keep reference to NoteService

    `late final NotesService _notesService;`

    what we also need is to keep hold of our note service 

    ```dart
    class _NewNoteViewState extends State<NewNoteView> {
      DatabaseNote? _note;
      late final NoteService _noteService;
      
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: const Text('New Note'),
          ),
          body: const Text('Write your new note here...'),
        );
      }
    }
    ```

    we need a text editing controller to keep track of the text changes.

  - We also need to track text changes

    `late final TextEditingController _textController;`

  - Let's create a new note

    `Future<DatabaseNote> createNewNote() async {}`

    첫번째로 해야할 것은 have we created this note before inside the `_note` variable에 대한 확인이다. if we have created this note before then we don't have to create it again. we just return. but if we haven't created it then we go to the note service and say create the note and then get that note back to us.

    ```dart
    Future<DatabaseNote> createNewNote() async {
        final existingNote = _note;
        // already have a note
        if (existingNote != null) {
            return existingNote;
        }
        final currentUser = AuthService.firebase().currentUser!;
        final email = currentUser.email!;
        final owner = await _noteService.getUser(email: email);
        return _noteService.createNote(owner: owner);
    }
    ```

  - Upon disposal, we need to delete the note if text is empty

    `code => void _deleteNoteIfTextIsEmpty() {}`

    when this view is disposed of meaning that for instance the user presses the back button on this view, we need to ensure that the current note in the database gets deleted if there is no text entered for that note.

    ```dart
    void _deleteNoteIfTextIsEmpty() {
        final note = _note;
        if (_textController.text.isEmpty && note != null) {
            _noteService.deleteNote(id: note.id);
        }
    }
    ```

  - And also save the note if text is not empty

    `void _saveNoteIfTextNotEmpty() async {}`

    ```dart
    void _saveNoteIfTextNotEmpty() async {
        final note = _note;
        final text = _textController.text;
        if (note != null && text.isNotEmpty) {
            await _noteService.updateNote(
                note: note,
                text: text,
            );
        }
    }
    ```

  - Take care of our view's disposal

    `void dispose() {}`

    now we have to put these functions in use.

    ```dart
    @override
    void dispose() {
        _deleteNoteIfTextIsEmpty();
        _saveNoteIfTextNotEmpty();
        _textController.dispose();
        super.dispose();
    }
    ```

  - Let's take care of the init function

    `void intiState() {}`

    ```dart
    @override
    void initState() {
        _noteService = NoteService();
        _textController = TextEditingController();
        super.initState();
    }
    ```

  - Update our current note upon text changes

    `void _textControllerListener() async {}`

    ```dart
    void _textControllerListener() async {
        final note = _note;
        if (note == null) {
            return;
        }
        final text = _textController.text;
        await _noteService.updateNote(
            note: note,
            text: text,
        );
    }
    ```

  - Let's hook our text field changes to the listner

    `void _setupTextControllerListener() {}`

    we also need to have a function that first removes this listener from our text editing controller if it has already been added and then it adds it again.

    ```dart
    void _setupTextControllerListener() {
        _textController.removeListener(_textControllerListener);
        _textController.addListener(_textControllerListener);
    }
    ```

- Let's program the main UI of new_note_view.dart

  We need a simple text field on the screen

  ```dart
  body: FutureBuilder(
      future: createNewNote(),
      builder: (context, snapshot) {
          switch (snapshot.connectionState) {
              case ConnectionState.done:
                  _note = snapshot.data as DatabaseNote;
                  _setupTextControllerListener();
                  return TextField(
                      controller: _textController,
                      keyboardType: TextInputType.multiline,
                      maxLines: null,
                  );
              default:
                  return const CircularProgressIndicator();
          }
      },
  ),
  ```

- next chapter

  we have new notes, we now need to display them on notes_view

## 32. Displaying Notes in Notes View

- 21:35:45

- Our notes are not populated in the stream controller

  In notes_service.dart, our broadcast controller doesn't get populated with default values

  ![image-20230218162121471](https://user-images.githubusercontent.com/77393619/219849237-52cf901a-4a10-421d-9d82-04aa36478090.png)

  noteservice parenthesis then they're actually not creating any instance of noteservice but they're going through this factory initializer which in turn calls this `_shared` static final which in turn calls this internal or private constructor. that means we've created a singleton. **so creating a new noteService over and over again is not gonna create a new instance. it's just gonna get the same shared instance.**

  ![image-20230218162558715](https://user-images.githubusercontent.com/77393619/219849238-acc29eb2-5934-44b6-93a0-38c0e1fc3ce0.png)

  and then whoever then starts talk reading or allNotes here properly allNotes is delegating its responsibility to the notesStreamController or stream. 

  ![image-20230218162656228](https://user-images.githubusercontent.com/77393619/219849239-e56c4bfe-980e-4c34-b3ab-e15768c43664.png)

  however our `notesStreamController` is a broadcast stream controller. and what that means is that a stream controller that doesn't really hold on to its current value for new listeners so let's say you have a stream controller that is sitting here and you start listening to events to that stream controller from one place and then an event comes into the stream controller and stream controller says oh I have one listener right here I'm gonna delegate this information to that's listener.

  however after the propagation of this event into the stream controller the stream controller is not going hold on to this value when a new listener comes in from another side so any new listener to your broadcast stream controller is not gonna be informed of the current information which is populated in that stream controller.

  - Late final variable(21:41:00)

    Make _noteStreamController a late final value

    we need to remedy that and the way to do that is just to move the initialization of note stream controller to our

    ![image-20230218163412256](https://user-images.githubusercontent.com/77393619/219849242-1177cd1a-50c8-4267-a648-966e5d561cc8.png)

    to

    ```dart
    late final StreamController<List<DatabaseNote>> _notesStreamController;
    ```

    now it is our responsibility to ensure that this noteStreamController is actually initialized upon constructor upon constructing a new instance of our noteService.

  - Populate notes in our stream controller

    Move creation of _noteStreamController into the _sharedInstance() function and add _notes to the controller

    ![image-20230218163738798](https://user-images.githubusercontent.com/77393619/219849243-0075e720-9120-42a1-a413-2b04e6f6c0ab.png)

    this ensures anyone who starts listening to our to this property allNotes which in turn uses the notesStreamController if it's a new subscriber then it's gonna the onListen callback is gonna get called and then we're gonna populate our stream controller a stream with those notes that we've already read from the database.

- We shouldn't close the DB upon hot reload

  After opening DB, we shouldn't close it otherwise upon every reload it gets closed.

  - No more dispose for now

    Remove dispose() in notes_view.dart

- Let's build our tiles

  We can use ListView.builder for this

  what we need to do is to make sure that we have a list that we can grab the data that comes from our stream builder and now we're just saying waiting for all notes

  ![image-20230218164351199](https://user-images.githubusercontent.com/77393619/219849244-349c35a6-a06a-43e9-b77f-ff7b4a559c1d.png)

  we're gonna change that and instead we're actually gonna start using something called a ListView.

  `ListView` in flutter is an amazing widget. it has some great funtionality that it exposese using is builder. first how many items it has to render on the screen `itemCount`. and for itemCount we need to actually listen for snapshots data.

  StreamBuilder가 현재 `allNotes`를 listening하고있고, 말인즉슨 snapshot의 정보는 allNotes에서 오는 정보라는 것. 따라서 snapshot에 data가 있는지 먼저 확인후 반환을 한다.

  ![image-20230218165255562](https://user-images.githubusercontent.com/77393619/219849247-6339441b-14aa-43f3-8195-726c2279aaa5.png)

  - Let's build our tiles

    We can use ListView.builder for this

    ![image-20230218165727235](https://user-images.githubusercontent.com/77393619/219849249-20c74f17-722c-4cd2-8b96-092552bff9cf.png)

    `note.text` : allNotes 배열내부의 하나를 가져와서 해당 text data를 가져오기위함

    `maxLines` : 최대 text line을 설정. `null`로 지정하면 계속 줄이 늘어날 수 있다.

    `softWrap : true`, `overflow: TextOverflow.ellipsis` : content가 너무 길어서 우선 생략을 했는데 뒤에 내용이 더 있다는 것을 사용자에게 알려주기 위해서(UX향상) 설정하는 property

    ![image-20230218170002053](https://user-images.githubusercontent.com/77393619/219849250-996c4220-62c8-4f90-a278-ded3539541bc.png)

- Let's demo

  We can now see that all notes are displayed on the screen

- next chapter

  we will work on deleting existing notes
  
## 33. Deleting Existing Notes in Notes View

- Delete dialog

  Remember that we already have an error dialog? Can we make this generic?

- Let's get rid of our error dialog

  Delete `lib/utilities/show_error_dialog.dart`

- Remove showLogOutDialog

  Remove showLogOutDialog from NotesView since we are going to have a generic one.

- And we use our NotesListView

  Use the new NotesListView in NotesView

  ![image-20230218194844105](https://user-images.githubusercontent.com/77393619/219865004-3553d427-f0f5-4f84-8c0e-9334621d07e4.png)

  `trailing` is a property of list tile that as its name indicates it's going to **allow you to specify a widget that needs to be displayed at the end or the trail of every list tile** and this is where we're going to use an icon button. so to display our little trash can.

  ![image-20230218195139673](https://user-images.githubusercontent.com/77393619/219865005-af1a986d-3bee-40d3-bb04-9c3c785cd39b.png)

  onPressed we need to take care of the displaying of a dialogue.

  ![image-20230218195416632](https://user-images.githubusercontent.com/77393619/219865006-a8d72d97-09df-4705-ade5-722478319884.png)

- Our own generic dialog

  `lib/utilities/dialogs/generic_dialog.dart`

  ![image-20230218195601246](https://user-images.githubusercontent.com/77393619/219865007-0df7d9e6-48ba-4ccc-8a79-36062e6f98a5.png)

  여러가지 dialog를 통합하기위한 dialog.

- Generic error dialog

  `lib/utilities/dialogs/error_dialog.dart`

  - Let's use error dialog everywhere

    We have a few places where we are displaying error dialogs

- And reuse again for log-out dialog

  `lib/utilities/dialogs/logout_dialog.dart`

  ![image-20230218203142454](https://user-images.githubusercontent.com/77393619/219865009-abbbd943-584c-4c93-8ea8-b2d6d06f6e87.png)

  remember on some platforms you're able to dismiss your dialogs without actually responding to any of the options presented in the dialog. in those platforms **you actually need to guard yourself against that case by returning a default value.** in this case, you can say `then` so if we get this value which is an optional bool then we say either return that or just return false.

  - Put the log out dialog to use

    We removed the old code, now we should bring the new one in

- Put NotesListView to use

  Let's bring it to NotesView

  ![image-20230218203912168](https://user-images.githubusercontent.com/77393619/219865012-d9909916-a97e-4e2f-bc41-51e975cfbae1.png)

- 이제 삭제가 가능하다

  ![image-20230218204148290](https://user-images.githubusercontent.com/77393619/219865014-95bbfee5-592b-4fc7-9972-b30d44b159d7.png)

  먼저 휴지통을 클릭하여 삭제를 할 경우

  ![image-20230218204241882](https://user-images.githubusercontent.com/77393619/219865015-4cfb641d-d77b-4e7f-b21b-eaa7740ea061.png)

  and our note_view is getting notified of that information from its StreamBuilder 

  ![image-20230218204340284](https://user-images.githubusercontent.com/77393619/219865016-86736231-1a63-42ca-8924-e4d020e06007.png)

  because remember notes_service(`lib/services/crud/notes_service.dart`) and upon deleteNote it actually removes it from its array of notes and it notifies the stream controller

  ![image-20230218204517512](https://user-images.githubusercontent.com/77393619/219865018-455c653b-146c-4336-b843-b4724b6ca4dc.png)

- next chapter

  We will talk about updating existing notes

  











  



    



  
  
