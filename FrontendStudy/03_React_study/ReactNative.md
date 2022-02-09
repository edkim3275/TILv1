# ReactNative

- 리액트 네이티브 프로젝트를 생성하는 방법
  - Expo를 이용하는 방법
  - 리액트 네이티브 CLI를 이용하는 방법

- react-native 버전확인 `react-native -v`

  react-native-cli: 2.0.1
  react-native: 0.66.3

## reactnative

- 웹 브라우저가 아닌, iOS와 안드로이드에서 동작하는 네이티브 모바일(Native Mobile) 애플리케이션을 만드는 자바스크립트 프레임워크
- 실사용예 : 페이스북, 인스타그램, 핀터레스트, 월마트 ...
- 장점
  - 대부분의 코드가 플랫폼 간 공유가 가능해서 iOS, 안드로이드에서 동시 개발이 가능
  - 저장하기만 해도 자동으로 변경된 내용이 적용된 화면을 확인할 수 있는 패스트 리프레쉬(Fast Refresh)기능

- 단점

  - 네이티브의 새로운 기능을 사용하는 데 오래 걸림
  - 유지보수의 어려움

- 동작방식

  - **브릿지** : 자바스크립트 코드 -> 네이티브 코드. 자바스크립트 코드를 이용해 네이티브 계층과 통신할 수 있도록 연결하는 역할

  - **가상DOM** : 화면에 보이지는 않지만 데이터가 변할 경우 실제 DOM과 비교하면서 차이점을 확인하여 차이점이 있는 부분만 실제 DOM에 적용하여 그리는 역할

  - **JSX(JavaScript XML)** : 자바스크립트 확장 문법. 자바스크립트 코드 안에서 UI 작업을 할 때 도움을 준다. 리액트에서 많이 사용. 나중에 바벨(Babel)을 사용하여 자바스크립트로 변환된다.

    ```jsx
    const element = <h1>Hello, world</h1>;
    ```

## 개발환경

- 맥에서는 iOS, 안드로이드 모두 개발 가능하지만, 윈도우와 리눅스 환경에서는 안드로이드 개발만 가능.
- 공통적으로 Node.js, JDK, 안드로이드 스튜디오 설치가 필요. 그 외 맥에서는 왓치맨과 XCode의 추가 설치가 필요. 윈도우에서는 파이썬 설치가 필요.
  - 왓치맨 : 파일 시스템 변경 감지 도구. 파일 변화를 감지하고 파일의 변화가 조건을 만족 시키면 특정 동작을 실행. RN에서는 소스코드의 변화를 감지하고 자동으로 빌드하여 화면에 업로드하는 역할
  - 파이썬 : 윈도우에서 RN은 빌드할 때 파이썬이 필요.
  - XCode : iOS를 개발하는 데 반드시 필요한 개발 도구
  - JDK(Java Development Kit) : 안드로이드 개발을 위한 안드로이드 개발 언어인 자바 개발 도구
  - 안드로이드 스튜디오 : 안드로이드 개발을 위한 공식 IDE(Integrated Development Environment)

- RN 프로젝트 생성방법

  - Expo를 이용하는 방법

    - Expo : RN을 편하게 사용할 수 있도록 미리 여러 가지 설정이 되어 있는 툴
    - https://expo.io

  - 리액트 네이티브 CLI를 이용하는 방법

    - 프로젝트 생성 : `npx react-native init PJTname (--version X.XX.X)`

    - 프로젝트 실행

      ```
      cd PJTname
      npm run ios
      npm run android
      
      or
      
      npm react-native run-ios
      npm react-native run-android
      ```

      RN이 실행되면 터미널 혹은 명령 프롬프트 창 하나가 추가로 열리고 Metro가 실행 됨.

      Metro : RN을 위한 자바스크립트 번들러(Bundler)로서 RN가 실행될 때마다 자바스크립트 파일들을 단일 파일로 컴파일하는 역할.

## 스타일링

- 리액트 네이티브에서의 스타일링은 웹 프로그래밍에서 사용하는 CSS와는 약간 차이가 있다.

  ```
  background-color (x)
  backgroundColor (o)
  ```

- 인라인 스타일링과 클래스 스타일링

  - 컴포넌트 style 속성에 **인라인 스타일**을 적용하는 방법

    ```react
    const App = () => {
        return (
        	<View
            	style={{
                    flex: 1,
                    backgroundColor: '#fff',
                    alignItems: 'center',
                    justifyContent: 'center',
                }}    
            >
            </View>
        )
    }
    ```

  - 스타일시트(StyleSheet)에 정의된 스타일을 사용하는 **클래스 스타일링** 방법

    - 컴포넌트 태그에 직접 입력하는 방식이 아니라 스타일시트에 정의된 스타일을 사용하는 방법.
    - 스타일시트에 스타일을 정의하고 컴포넌트에서는 정의된 스타일의 이름으로 적용

    ```react
    import React from 'react';
    import { StyleSheet, View } from 'react-native';
    
    const App = () => {
        return (
        	<View style={styles.container}></View>
        )
    }
    
    const styles = StyleSheet.create({
        container: {
            flex: 1,
            backgroundColor: '#fff',
            alignItems: 'center',
            justifyContent: 'center',
        }
    })
    ```

- 여러 개의 스타일 적용

  - 두 컴포넌트가 중복된 스타일을 가지고있는 경우처럼 스타일을 덮어쓰거나 하나의 컴포넌트에 여러 개의 스타일을 적용해야 할 때 **배열을 이용하여 style 속성에 여러 개의 스타일을 적용**
  - :exclamation: 스타일의 순서에 주의하자. 뒤에 오는 스타일이 앞에 있는 스타일을 덮는다.

  ```react
  const App = () => {
  	return (
      	<View style={styles.container}>
          	<Text style={styles.text}>a</Text>
              <Text style={[styles.text, styles.error]}>b</Text>
          </View>
      )
  }
  
  const styles = StyleSheet.create({
      container: {...},
      text: {...},
      error: {
          fontWeight: '400',
          color: 'red',
      }
  })
  ```

  - 인라인 스타일과 클래스 스타일 방식을 혼용해서 사용하는 것도 가능

  ```react
  const App = () => {
  	return (
      	<View style={styles.container}>
          	<Text style={styles.text}>a</Text>
              <Text style={[styles.text, { color: 'red' }]}>b</Text>
          </View>
      )
  }
  ```

- 외부 스타일 이용

  - 우리가 만든 스타일을 다양한 곳에서 사용하고 싶은 경우.
  - 외부 파일에 스타일을 정의하고 여러 개의 파일에서 스타일을 공통으로 사용

  ```react
  // src/styles.js
  import { StyleSheet } from 'react-native';
  
  export const viewStyles = StyleSheet.create({
      container: {...}
  });
      
  export const textStyles = StyleSheet.create({
      text: {...},
      error: {...},
  });
  
  // src/App.js
  import React from 'react';
  import { View, Text } from 'react-native';
  import { viewStyles, textStyles } from './styles';
  
  const App = () => {
  	return (
      	<View style={viewStyles.container}>
          	<Text style={textStyles.text}>a</Text>
              <Text style={[textStyles.text, textStyles.error]}>b</Text>
          </View>
      )
  }
  ```

### 스타일드 컴포넌트

- 자바스크립트 파일 안에 스타일을 작성하는 CSS-in-JS 라이브러리(스타일이 적용된 컴포넌트라고 이해하자.)
- RN에서 스타일 주는 것이 기존의 웹 프로그래밍 방식과 조금씩 차이가 있기에(타입, 카멜케이스 등) 이를 해소하고자 사용하는 기능
- 설치 : `npm install styled-components`

- 태그드 템플릿 리터럴(Tagged Template Literals)

  - 스타일드 컴포넌트를 사용할 때 `styled.[컴포넌트 이름]``(백틱)` 이와 같이 작성하고 백틱 내에 스타일을 지정하면 된다.

  :exclamation: styled뒤에 오는 컴포넌트 이름은 반드시 존재하는 컴포넌트를 지정해야한다. 

- 재사용 가능한 코드를 분리해낼 수 있다.

  ```react
  import styled, { css } from 'styled-components/native';
  
  const whiteText = css`
  	color: #fff;
  	font-size: 14px;
  `;
  const MyBoldTextComponent = styled.Text`
  	${whiteText}
  	font-weight: 600;
  `;
  const MyLightTextComponent = styled.Text`
  	${whiteText}
  	font-weight: 200;
  `;
  ```

- 완성된 컴포넌트를 상속받아 이용할 수 있다.

  ```react
  import styled from 'styled-components/native';
  
  const StyledText = styled.Text`
  	color: #000;
  	font-size: 20px;
  	margin: 10px;
  	padding: 10px;
  `;
  
  const ErrorText = styled(StyledText)`
  	font-weight: 600;
  	color: red;
  `;
  ```

- ThemeProvider

  - Context API를 활용해 애플리케이션 전체에서 스타일드 컴포넌트를 이용할 때 미리 정의한 값들을 사용할 수 있도록 props로 전달.

  ```react
  // 1. 컴포넌트에 사용할 색 지정
  // src/theme.js
  export const theme = {
      purple: '#9b59b6';
      blue: '#3498db';
  }
  
  // 2. 모든 컴포넌트를 감싸는 최상위 컴포넌트로 ThemeProvide 컴포넌트를 사용하고, 해당 컴포넌트의 theme 속성에 설정 => 자식 컴포넌트에서는 스타일드 컴포넌트를 이용할 때 props로 theme을 전달 받아 사용이 가능
  // src/App.js
  import React from 'react';
  import styled, { ThemeProvider } from 'styled-components/native';
  import theme from './theme';
  
  const App = () => {
      return (
      	<ThemeProvider style={theme}>
              ...
          </ThemeProvider>
      )
  }
  
  // 3. 컴포넌트에서 스타일을 정의할 때 props로 전달받은 theme을 이용
  // src/components/Button.js
  const ButtonContainer = styled.TouchableOpacity`
  	background-color: ${props => 
  		props.title === 'Hanbit' ? props.theme.purple : props.theme.blue
  	};
  `;
  ```

  
