# NFC

> a **wireless** technology for **short-range** communication

## NFC?

근거리 무선 통신(NFC)란 무엇일까? Near Field Communication는 13.56MHz의 *대역*을 가지며, **아주 가까운 거리**(접촉 및 근접 비접촉 모두 포함)의 **무선 통신**을 하기 위한 기술이다. 현재 지원되는 데이터 통신 속도는 424kB/s이다. 교통(transportation), 티켓, 지불(payment), 출입 등 여러 서비스에서 사용할 수 있다.

>  :bulb: 대역?
>
> 여기서 말하는 대역은 주파수 대역(Radio Band)을 의미한다. 여러 기관에서 정한 표준에 따라서 그 종류가 나뉜다. 통신용으로 규정된 주파수 대역인 ITU표준 대역이 있고 이외에 IEEE 표준과 NATO, EU, 미국 표준 대역이 있다.
>
> | 밴드 | 주파수         | 파장범위   |
> | ---- | -------------- | ---------- |
> | VLF  | 3 ~ 30 kHz     | 100 ~ 10km |
> | LF   | 30 ~ 300 kHz   | 10 ~ 1km   |
> | MF   | 300 ~ 3000 kHz | 1 ~ 0.1km  |
> | HF   | 3 ~ 30 MHz     | 100 ~ 10m  |
> | VHF  | 30 ~ 300MHz    | 10 ~ 1m    |
> | UHF  | 300 ~ 3000MHz  | 1 ~ 0.1m   |
>
> 이름 짓는 법은 간단하다. LF는 Low Frequency, MF는 Medium Frequency, HF는 High Frequency이고 VHF, UHF ...는 Very, Ultra, Super, Extremely, Tremendously HF 순으로 나눠져있다.
>
> 살펴볼 NFC의 경우 13.56 MHz 대역을 가지기에 HF밴드(100 ~ 10m 파장범위)로 볼 수 있다.

### 모드

| 모드            | 동작                                                 | 응용분야                                         |
| --------------- | ---------------------------------------------------- | ------------------------------------------------ |
| 카드 모드       | NFC를 탑재한 기기가 기존의 비접촉식 카드와 같이 동작 | 신용카드, 교통카드 등 각종카드                   |
| Read/Write 모드 | NFC를 탑재한 기기가 RFID 태그 리더기로 동작          | 스마트 포스터와 같은 옥외광고, 작품 설명 등      |
| P2P 모드        | NFC 기기 간 데이터 송수신                            | **개인 간 데이터 전송, 명함 교환**, 개인 송금 등 |

### 블루투스와의 비교

범위가 좁다는 NFC의 단점은 privacy와 security 측면에 있어서는 장점이 될 수 있다. 공격자가 멀리 떨어진 곳에서 당신을 해킹할 수 없다. 또한 낮은 비트레이트 덕분에 소비전력 또한 매우 적다.

![image-20230105142041604](/home/myounjunkim/MV1-3/NFC.assets/image-20230105142041604.png)

|              | NFC                 | 블루투스   | 블루투스(저 에너지), BLE |
| ------------ | ------------------- | ---------- | ------------------------ |
| 암호화       | RFID와 동시에 안 됨 | 이용 가능  | 이용 가능                |
| 범위         | < 0.2 m(10cm정도)   | ~10 m      | ~ 1 m                    |
| *비트레이트* | 424 kbit/s          | 2.1 Mbit/s | ~ 1.0 Mbit/s             |
| 설정시간     | < 0.1초             | < 6초      | < 1초                    |
| 소비전력     | < 15mA(읽기)        | 다양       | < 15mA                   |

> :bulb: 비트레이트(bitrate)
>
> 특정 시간 단위마다 처리하는 비트의 수. 즉, 비트레이트가 클수록 단위 시간마다 처리할 수 있는 데이터의 양이 많아진다는 의미이다.

### 활용

NFC의 근접통신기술은 USIM칩, IC칩, RF칩이 활용된다.

## ReactNative에 적용하기

> react-native-nfc-manager 라이브러리를 활용하여 RN에 NFC 기능을 추가해보자.
> Build **React Native** apps to interact with **NFC tags**

### 목차

- NFC 기술에 대한 개요(What is NFC?) - Learn all about NFC

  - Compare to other technologies
  - NFC terminologies(용어)
  - Mobile Platform support
  - What's next?

- Build Three apps - App 1 : Tag Counter Game

  > Learn the basic
  > 사용자가 5개의 NFC 태그를 스캔하는데 필요한 시간을 계산하는 게임

  - How to properly set up an NFC mobile app
  - How to trigger NFC scanning

- Build Three apps - App 2 : Tap and Go

  > Learn NDEF
  > iOS와 Android 두 환경 모두에 지원되고, 거의 모든 NFC 태그에 사용할 수 있는 표준 NFC 데이터 형식인 NDEF에 관한 것
  >
  > NFC 리더, NFC 쓰기 앱 만들기
  > 특정 데이터(혹은 URL과 같은 링크 등)를 NFC 태그에 작성하여 나중에 특정 작업(링크열기, 전화걸기, 메시지 전달 등)을 트리거 할 수 있다.

  - Build and write NDEF into NFC tags
  - Read the parse NDEF from NFC tags
  - Deep linking with NFC tags

- Build Three apps - App 3 : NFC Pokemon

  > Learn low-level NFC programming
  > NFC 태그 내부 메모리를 직접 조작하고 앱이 빌드하려는 독점 NFC 명령을 사용해보자.

  - NFC tag platform commands
  - Sign and verify digital signatures
  - Password protection with proprietray NFC commands

- What will **NOT** cover
  - Advanced NFC knowledge, such as specification or standard details
  - NFC operation mode other than Reader mode
  - NFC Tag Type other than Type 2 Tag
  - Detailed explanation for all APIs in our NFC library

- **Prerequisites**

  - 기본적인 RN에 대한 이해(Basic understanding of React Native)

  - A mobile phone **supports NFC**

    ![image-20230105144233326](/home/myounjunkim/MV1-3/NFC.assets/image-20230105144233326.png)

    - iOS : iPhone 7 이상(iPad doesn't work)
    - Android : check phone settings

  - **iPhone user** also have to enroll in the **Apple Developer Program** to run apps in iPhone

  - NFC tags : NXP **NTAG 213** or **215**

    ![image-20230105141507257](/home/myounjunkim/MV1-3/NFC.assets/image-20230105141507257.png)

    - The most used low-cost NFC tags(가장 많이 사용되는 저비용 NFC 태그)

### NFC Introduction

- What's NFC

  NFC stands for Near-Field Communication

  - **Wireless** communication protocol
  - Rooted in **RFID**(Radio-Frequency IDentification)
  - Founded by Sony, Philips, and Nokia
  - The standard organization is called **NFC Forum**

  Being a wireless technology,

  - Short range, typically within **10 cm**
  - Low speed, under **424 kbps**

- What Makes NFC(RFID) unique?

  The tag doesn't need to carry a battery

  NFC 기술은 아래 다이어그램의 왼쪽에 있는 비대칭 서례로 디자인되었다.

  ![image-20230105142432058](/home/myounjunkim/MV1-3/NFC.assets/image-20230105142432058.png)

  NFC는 리더는 전자기장을 생성하고, 전자기장에서 유도된 전기가 오른쪽의 NFC 태그로 전달되게 된다.

#### NFC Terminologies

- Device Role

  ![image-20230105142824220](/home/myounjunkim/MV1-3/NFC.assets/image-20230105142824220.png)

  NFC 리더는 시작자(Initiator) : starts the entire communication process

  NFC 태그는 타겟(Target)

- Communication mode

  Communication mode는 **Passive Mode**라고도 불린다. target은 오직 initiator의 명령에만 수동적으로 응답할 수 있기 때문이다. 즉, 타겟은 초기 대상 장치(Initiator)에 데이터를 능동적으로(actively 하게) 보낼 수 없다. target devices without batteries usually use passive mode

  물론 **Active Mode**도 존재한다. 이 모드에서 target은 초기 대상 장치에게 능동적으로 데이터를 보내기 위한 배터리(power)를 갖고 있어야 한다.

- NFC Operation Modes

  ![image-20230105144148338](/home/myounjunkim/MV1-3/NFC.assets/image-20230105144148338.png)

  - Reader Mode

    allowing the NFC device to read and/or write passive NFC tags and stickers

  - P2P

    allowing the NFC device to exchange data with other NFC peers; this operation mode is used by **Android Beam**

  - Card Emulation

    allowing the NFC device itself to act as an NFC card. The emulated NFC card can then be accessed by an external NFC reader, such as an NFC point-of-sale(POS) terminal

  - Wireless Charging

#### NFC Specification Landscape

![image-20230105144455779](/home/myounjunkim/MV1-3/NFC.assets/image-20230105144455779.png)

리액트 네이티브 개발자로서 우리가 주목해야할 부분은 NDEF와 Type2 ~ 5 기술 사양이다.

- **NDEF**

  NDEF = **N**FC + **D**ata + **E**xchange + **F**ormat

  - NDEF는 NFC 포럼에서 정의한 NFC 데이터 교환 형식을 나타낸다.
    Defined by NFC Forum, the ORG behind all NFC related specs
  - NFC 지원 장치 간의 데이터 교환을 허용하는 독립적인 기술을 제공하는데 목표를 둔다.
    Aim to provide a technology independent format to allow data exchange between NFC-enabled devices

  - URL 혹은 연락처 정보와 같은 텍스트 기반 데이터를 수행한다.
    Text-based data such as URLs, or contact info
  - Supported by both Android/iOS
  - 대부분의 NFC 태그에 NDEF 데이터가 포함되어 있기 때문에 매우 중요하다.

- Type 2 - 5 Tag Specification
  - 위의 타입 2 ~ 5 사양을 NFC 플랫폼으로 사용할 거다.
  - 근데 몇몇 NFC 도메인 사람들은 Type 2 기술 플랫폼 대신 T2T를 사용하곤 한다.

## App1 : Tag Counter Game App

### Lesson 1 - What we will build

- scan and discover NFC tags

- build a game to count how much time a player needs to scan five NFC tags

- learn some important concepts about NFC
  - How to properly configure your app, especially for iOS
  - How to use react-native-nfc-manager library to discover our NFC tags
  - How to handle the devices without NFC
  - The difference between iOS and Android

### Lesson 2 - NFC APP Setup

- create project skeleton

  ```
  npx react-native init TagCounterGame
  ```

> :bulb: expo cli vs. rn cli
>
> Does your app need custom native codes?
>
> Does your app depends on libraries with native code?
> whether your app depends on third-party libraries with native code in it.
> what does this mean in real native there are two kind of libraries. first one is implemented purely in javascript
>
> JS Only Library vs. JS + Native Library
> for example, react-native-elements. react-native-elements is a well-known ui library which provides lots of useful ui component. since it is a pure ui library it probably requires no special platform features. so it might be implemented in pure js.
>
> Well, most of the time, but that's not always true.
> Most RN UI libraries uses built-in components to compose their own components, but there are some still contain custom native codes, especially for wrapping native UI components
>
> this project 96% javascript and 3% css
> ![image-20230105152037636](/home/myounjunkim/MV1-3/NFC.assets/image-20230105152037636.png)
>
> on the other hand RN-nfc-manager. 
>
> ![image-20230105152134542](/home/myounjunkim/MV1-3/NFC.assets/image-20230105152134542.png)
>
> it made by 34% js, 40% Java, 25% Objective-C for iOS ...
>
> Beside languages, the native module library often includes platform specific directories: ios, android
>
> if your project needs any of this library which contain native codes you have two options.
>
> 1. use react-native cli
> 2. use expo cli, and eject later

- native setup for android

- native setup for iOS

### Lesson 3 - NFC Library Walkthorugh

- install react-native-nfc-manager
- Do a quick walk through for our NFC library

### Lesson 4 - iOS App

```react
```

