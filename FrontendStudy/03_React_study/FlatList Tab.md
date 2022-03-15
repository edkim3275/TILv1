- basic code

```react
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const images = {
  man:
    'https://images.pexels.com/photos/3147528/pexels-photo-3147528.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
  women:
    'https://images.pexels.com/photos/2552130/pexels-photo-2552130.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
  kids:
    'https://images.pexels.com/photos/5080167/pexels-photo-5080167.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
  skullcandy:
    'https://images.pexels.com/photos/5602879/pexels-photo-5602879.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
  help:
    'https://images.pexels.com/photos/2552130/pexels-photo-2552130.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
};
const data = Object.keys(images).map((i) => ({
  key: i,
  title: i,
  image: images[i],
}));

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar hidden />
      <Text style={{ fontSize: 42 }}>❤️</Text>
      <Text
        style={{
          fontFamily: 'Menlo',
          marginTop: 10,
          fontWeight: '800',
          fontSize: 16,
        }}
      >
        Expo
      </Text>
      <Text style={{ fontFamily: 'Menlo', fontStyle: 'italic', fontSize: 12 }}>
        (expo.io)
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

- practice

```react
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Dimensions, FlatList, Animated, Image, findNodeHandler } from 'react-native';
const { width, height } = Dimensions.get('screen')

const images = {
	...
};
const data = Object.keys(images).map((i) => ({
  key: i,
  title: i,
  image: images[i],
  ref: React.createRef()
}));
// we have access to the each paricular tab ref and we can measure the layout
const Tab = React.forwardRef(({item}, ref) => {
    return <View ref={ref}>
    	<Text style={{ color: 'white', fontSize: 84/data.length, fontWeight: 'bold', fontTransfrom: 'uppercase'}}>{item.title}</Text>
    </View>
}

const Indicator = ({measures, scrollX}) => {
    const inputRange = data.map((_. i) => i*width);
    const indicatorWidth = scrollX.interpolate({
        inputRange,
        outputRange: measures.map(measure => measure.width)
    })
    const translateX = scrollX.interpolate({
        inputRange,
        outputRange: measures.map(measure => measure.x)
    })
    return <Animated.View 
    	style={{
            position: 'absolute',
            height: 4,
            width: indicatorWidth,
            backgroundColor: 'white',
            bottom: -10,
            left: 0,
            transfrom: [{
                translateX
            }]
        }}           
    />
})

const Tabs = ({data, scrollX}) => {
    const [measures, setMeasures] = React.useState([]);
    const containerRef = React.useRef();
    React.useEffect(() => {
        const m = []
        data.forEach(item => {
            // you need to specify the relative node where to measure
            item.ref.current.measureLayout(containerRef.current, 
            (x, y, width, height) => {
                m.push({
                    x, y, width, height,
                });
                if (m.length === data.length) {
                    setMeasures(m)
                }
            })
        })
    }, []);
    
    return (
      <View style={{ position: 'absolute', top: 100}}>
      	<View 
          ref={containerRef}
          style={{ 
            justifyContent: 'space-evenly', 
            flex: 1, 
            flexDirection: 'row'
          }}>
          {data.map((item) => {
            return <Tab key={item.key} item={item} ref={item.ref} />;
          })}
        </View>
        {measures.length > 0 && <Indicator measures={measures} scrollX={scrollX} />}
      </View>
    )
}
export default function App() {
  // Animated value is not going to change when react is going to be re-renderd or is going to receive new props
  const scrollX = React.useRef(new Animated.Value(0)).current;
  return (
    <View style={styles.container}>
      <StatusBar hidden />
      <Animated.FlatList 
      	data={data}
        keyExtractor={item => item.key}
        horizontal
        showsHorizontalScrollIndicator={false}
        pagingEnabled
        onScroll={Animated.event(
          [{nativeEvent: {contentOffset: {x: scrollX}}}],
          // indicator로만 width를 변경하고 useNativeDriver는 transform나 opacity변경에서만 작동하도록 하기 위해
          { useNativeDriver: false}
        )}
        bounces={false}
        renderItem={({item}) => {
          <View style={{ width, height }}>
            <Image 
              source={{ uri: item.image }}
              style={{ flex: 1, resizeMode: 'cover' }}
            />
            <View style={{ StyleSheet.absoluteFillObject, {backgroundColor: 'rgba(0,0,0,0.3)'}}}/>
          </View>
       	}}
      />
      <Tabs scrollX={scrollX} data={data} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

- change indicator
  - get the measurements for each particular tab
  - in order to do this, we need to measure layout plus find node handler from react native