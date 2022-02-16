# Canvas

ReactNative에서는 자체 컴포넌트를 사용해야하기에 react-natve-canvas 라이브러리를 설치하여 `Canvas` 컴포넌트를 사용한다.

```react
import Canvas from 'react-native-canvas'

const QRcode = () => {
    const handleCanvas = (canvas) => {
    	...    
    }
    
    return (
    	<Canvas ref={handleCanvas}/>
    )
}
```

- wallet을 생성할 때 account 별로 고유한 프로필 이미지를 부여하기 위해서 canvas를 활용하기로 했다.
- html, script를 활용하는 것과는 약간의 방식에 차이가 있다.

```react
const handleCanvas = (canvas) => {
    // 인자로 들어오는 canvas 유무확인
    if (canvas) {
    	var ctx = canvas.getContext("2d");
        
        ctx.fillStyle = "rgb(200,0,0)";
        ctx.fillRect (10, 10, 50, 50);
		
        // RN에서는 ctx내의 메서드를 통해 Promise객체를 받게된다.
        ctx.createRadialGradient(45, 45, 10, 52, 50, 60)
        	.then((radgrad) => {
            	radgrad.addColorStop(0, '#00ABEB')
            	radgrad.addColorStop(0.8, '#26C000')
            	radgrad.addColorStop(1, 'rgba(1, 159, 98, 0)')
        })
    }

}
```

- ![image](Canvas.assets/image.png)

- 