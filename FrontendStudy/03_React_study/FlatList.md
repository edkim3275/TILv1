# FlatList

> :bulb: ReactNative에서 배열을 화면으로 구현할 때 자주 사용되는 컴포넌트인 FlatList 컴포넌트에 대해서 정리해보자.

- 예시

  ```react
  <FlatList
      ref={flatListRef}
      *data={data}
      horizontal
      scrollEnabled
      snapToAlignment='center'
      decelerationRate={'fast'}
      showHorizontalScrollIndicator={false}
      scrollEventThrottle={16}
      *renderItem={(item) => {
          <View>
          	<Card item={item} />
          </View>
      }}
      onViewableItemChanged={onViewRef.current}
      viewabilityConfig={viewConfigRef.current}
      onScroll={
          Animated.event(
          	[{ nativeEvent: { contentOffset: { x: scrollX } } }]
              { useNativeDrier: false}
          )
      }
      ListFooterComponent={
          <LinearGradient
          	colors={['#4646cd', '#8282ff', '#5abef5']}
              start={{ x: 0, y: 0.25 }}
              end={{ x: 0.5, y: 1.25 }}
              style={styles.card}
          >
          </LinearGradient>
      }
  />
  ```

## Props

- `renderItem`(**필수**) : data에서 각 요소(item)을 가져와서 리스트에 렌더링.

  ```react
  renderItem({ item, index, seperators })
  ```

- `data`(**필수**) : 렌더링하고자 하는 데이터. 일반 배열을 넣어준다.

- `ref`: 해당 FlatList를 불러와서 사용하고자 할때 사용되는 값

  ```react
  flatListRef.current.scrollToIndex({ animated: true, index: 1 })
  ```

- `horizontal` : 데이터 나열 방향을 수평으로 전환(default는 수직 나열)

- `scrollEnabled` : scrollable 하도록 해주는 설정
- `snapToAlignment='center'` : Carousel 카드의 왼쪽, 오른쪽 카드가 보이도록 하는 설정(iOS에서만 가능)
- `showHorizontalScrollIndicator` : scroll 시각화 유무 설정
- `onScroll` : scrolll event handler

- `ListFooterComponent` : 모든 항목의 맨 마지막에 렌더링

## 활용 예시

![flatList활용](/home/myounjunkim/비디오/flatList활용.gif)