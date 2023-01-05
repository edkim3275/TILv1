# React Native Animation

Animated를 사용하여 컴포넌트에 움직임을 넣거나, 색상, 투명도 등이 변경되도록 애니메이션을 만들 수 있다.

state나 변수 등을 직접 제어하지 않고, **Animated 객체로 생성된 value를 제어함으로써 애니메이션을 만든다.**

Animated value는 한 가지 값을 갖는 Value()와 x축, y축 값을 갖는 ValueXY가 있다.

- React Native는 애니메이션에 사용할 수 있는 4가지 컴포넌트를 제공한다.
  Animated.Image
  Animated.ScrollView
  Animated.Text
  Animated.View

- 또한, 세 가지 애니메이션 타입이 있다.
  Timing - 시간이 지남에 따라 값을 애니메이션(animates)
  Spring - 간단한 스프링 물리 모델을 제공
  Decay - 초기 속도로 시작하여 점차 정지

## 기본구성

- 애니메이션 사용을 시작하려면 먼저 초기 값을 정의해야 한다.

  먼저 `new Animated.Value(n)` (또는 2D 애니메이션 구동을 위한 `new Animated.ValueXY({x : n, y: m})`)을 사용하여 초기 값을 정의한다. 다양한 곳에서 초기화가 가능한데 그 중 하나는 컴포넌트의 상태(state)에 유지하는 것.

  ```react
  animation : new Animated.Value(0)
  ```

- 그 다음 `Animated` 모듈을 가져온다.

  ```react
  import { Animated } from 'react-native'
  ```

- 그 다음으로 `Animated.View` 컴포넌트 렌더링

  ```react
  return (
  	<Animated.View
      	style={[objectStyles, animationStyles]}    
      ></Animated.View>
  )
  ```

  여기에서 스타일이 두 부분으로 나눌 수 있다

  `objectStyles` : 모양과 모양을 설명하는 `Animated` 컴포넌트의 정적 스타일

  `animationStyles` : 시간이 지남에 따라 변경할 스타일

- `timing()` 함수를 호출하여 애니메이션을 시작한다. 이 함수는 animated value를 첫 번째 인수로, 구성 개체(configuration object)를 두 번째로 받는다. 그 다음 애니메이션 오브젝트에서 `start()` 함수를 호출하여 애니메이션을 시작한다.

  ```react
  Animated.timing(
  	this.state.animation,
      {
          toValue: 250, // 변경할 value값
          duration: 2000 // 지속시간
      }
  ).start();
  ```

## Movement

- 상자를 화면 아래로 이동시키는 예제.

- 좌표계 원점 (0, 0)은 화면 왼쪽 상단. x좌표(x-coordinates)는 오른쪽으로 증가, y좌표(y-coordinates)는 위에서 아래로 증가.

- 위와 동일하게 코드를 작성하고 적당한 애니메이션 스타일로 오브젝트를 렌더링한다.

  ```react
  const animationStyles = {
      transform: [
          { translateY: this.state.animation }
      ]
  }
  return (
  	<Animated.View style={[objectStyle, animationStyles ]}></Animated.View>
  )
  ```

  상자를 이동하기 위해 변환(transform) 스타일을 이용하여 traslateY를 현재 애니메이션 값으로 변경한다. 

## Fading in and out

- 오브젝트에 페이딩 효과(fading effect)를 적용하기 위해 시간 경과에 따라 해당 오브젝트의 불투명도(opacity) 속성을 변경할 수 있다.

- 1의 값은 100% 가시(visible) 오브젝트이고 0은 완전히 투명한 오브젝트

- 페이드 아웃 효과(fade out effect)를 만들기위해서는 불투명도를 1에서 0으로 변경해야한다. 따라서, 애니메이션 값을 1로 초기화한다.

  ```react
  state = {
  	animation : new Animated.value(1)
  }
  Animated.timing(
  	this.state.animation,
  	{
  		toValue: 0,
  		duration: 2000
  	}
  )
  const animationStyles = {
  	opacity: this.state.animation
  }
  ```

## Scale

- 개체의 크기 조정을 위해 transform.scale 스타일을 변경할 수 있다.

  ```rea
  const animationStyles = {
  	transform: [
  		{ scale: this.state.animation }
  	]
  }
  ```

  예를들어 애니메이션 값이 1 (오브젝트 크기의 100%)에서 2(2배만큼)로 변경할 수 있다. 상자 안의 텍스트도 크기가 조정된다.

- 또한 오브젝트를 음수 값으로 조정할 수 있다. 

## Resizing

- 오브젝트 크기를 조정(resize) 하려면 width와 height 속성을 업데이트해야한다.

  ```react
  const animationStyles = {
  	width: this.state.animation,
  	height: this.state.animation    
  }
  ```

  오브젝트의 크기를 조절하기 위해 크기를 늘릴 때 상자안의 텍스트가 어떻게 동작하는지 주의해야한다.

## Interpolation

- 다음 단계로 넘어가기 위해서 보간(Interpolation)이란 무엇이고 어떻게 사용하는지 알아야한다.

- 경우에 따라 값을 n에서 m으로 변경 한 결과로는 충분하지 않다. 일부 오브젝트 스타일은 정수가 아닌 다른 형식을 받아들이기 때문에 커스텀 값을 가져와야 할 수도 있다. 예를들면 colors와 rotation degrees가 있다.

  이 경우 `interpolate()` 함수를 호출하여 사용자 정의 값 범위를 작성할 수 있다.

- 예를들어 화면의 퍼센트 사이즈를 사용하여 상자의 크기를 조정하려는 경우에 보간(Interpolation)을 실행 할 수 있다.

  ```react
  value.interpolate({
      inputRange: [0, 1],
      outputRange: ['0%', '100%'],
  })
  ```

  이 함수는 두 개의 키가있는 오브젝트를 받는다.

  `inputRange` : 애니메이션 값의 범위

  `outputRange` : 보간 된 값이 inputRange에 맵핑 된 결과

  이 예제에서 애니메이션 값이 0에서 1로 변경되면 퍼센트가 0%에서 100%로 점차 변경된다.

## Rotation

- 이 예제에서 보간이 작동하는 것을 확인할 수 있다.

- 회전 효과를 얻기 위해 애니메이션 값을 0에서 1로 변경하고 transform.rotate 스타일을 업데이트한다.

  해당 스타일은 숫자 값을 지원하지 않으므로 보간(interpolation)을 적용한다.

  ```react
  const animationStyles = {
      transform: [
          {
              rotate: this.state.animation.interpolate({
                  inputRange: [0, 1],
                  outputRange: ['0deg', '360deg']
              })
          }
      ]
  }
  ```

  여기서 0도에서 360까지의 값을 변경하는 보간 규칙을 정의한다.

- 옵션으로 `transform.rotateX` 또는 `transform.rotateY` 스타일을 업데이트하면  뒤집는 효과를 볼 수 있다.

## Color change

- 시간이 지남에 따라 오브젝트의 색상을 변경할 수도 있다.

- 상자의 backgroundColor를 변경해보면

  ```react
  const animationStyles = {
      backgroundColor: this.state.animation.interpolate({
          inputRange: [0, 0.5, 1],
          outputRange: ['orange', 'rgb(0, 200, 0)', 'purple']
      })
  }
  ```

  위 처럼 보간(interpolation)에는 둘 이상의 입력과 출력 값이 포함될 수 있다. 이 예제에서는 애니메이션이 오렌지색에서 시작하여 중간에 배경색을 녹색으로 변경하도록 한다. 그리고 animation이 상자를 보라색으로 칠한다. 

## 참고

https://www.devh.kr/2020/Introduction-to-animation-in-React-Native/