# Practice

## 2021.01.14

### 01_ data types

```python
number = 3
print(number, type(number))
# 출력값은 3 <class 'int'>
# 여기서 int는 integer(정수)

string = '문자열'
print(string, type(string))
# 출력값은 문자열 <class 'str'>
# 여기서 str은 string(문자)

boolean = true
print(boolean, type(boolean))
# 출력값은 true <class 'bool'>
# 여기서 bool은 boolean(참,거짓)
```

### 02_f-string

```python
name = '유태영'
greeting = '반갑습니다.'
# 이를 string interpolation이라고 부른다.
print(f'{name}님, {greeting}')
# 결과값은 유태영님, 반갑습니다.
```

### 03_list

```python
# 음식 목록을 담은 리스트 한개를 생성해주세요
foods = ['치킨', '피자', '햄버거']
print(lists[0])
foods[0] = '초밥'
print(lists)
# 결과값은 치킨
# ['초밥', '피자', '햄버거']
```

- 변수이름 list는 절대로 쓰면 안된다!
  - 이미 list라는 이름이 쓰이고있다.
  - 너무 모호하다
- list는 무조건 복수형 변수로 이름을 짓는다.
- python에서 흰색문자는 변수로 이해하자

### 04_dict

```python
# my_home = {'서울': 59, '부산': 30, '대구': 30} 이것은 잘 못된 표기
weather_infos = [
	{
    	'location': '서울',
    	'mise': 10,
    	'temp': 5
	},
	{
    	'location': '부산',
    	'mise': 30,
    	'temp': 6
	},
	{
    	'location': '대구',
    	'mise': 30,
    	'temp': 10
	}
]
print(weather_infos[0])
# 결과값은 {'location': '서울', 'mise': 10, 'temp': 5}
```

- 쉼표 뒤에 띄어쓰기 필수
- dictionary가 왜 존재하는가? => 표(table)를 옮기기 위함, 그냥 표가 아니라 '표의 행(row)'을 옮기기 위함
- table 또한 복수형(이러한 약속, 규범들을 Convention이라 한다.)
- list는 정의할 때 {}, 불러올 때 []

```python
#예제
coin = {
    "BTC": {
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364.5",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

# 2-1. 코인의 정보에서 BTC의 / 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])
# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
print(int(coin['BTC']['opening_price']) + float(coin['XRP']['opening_price']))
```

### 05_practice

```python
import requests

key = '내키'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=부산&ver=1.0&returnType=json'

'''
http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty 까지는 약속
serviceKey={key}
&
numOfRows=5
&
pageNo=1
&
sidoName=부산
&
ver=1.0
&
returnType=json
'''
# 주석 사용은 #을 사용하거나 '''사용하거나 ctrl + / 하면 주석 사용된다.
response = requests.get(url).json()

print(response['response']['body']['items'][2]['stationName'])
# print(url)
# print(response)
# print(type(response))
```

```python
import requests

url = 'https://api.agify.io/?name=edgar'

response = requests.get(url).json()

# print(response)  # 출력결과: 내 이름은 neo, 나이는 37

print(f"내 이름은 {response['name']}, 나이는 {response['age']}")
```

```python
movie = {  # movie는 딕셔너리
    'movieInfo': {  # movie라는 딕셔너리 안의 movieInfo라는 딕셔너리
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
                'nationNm': '한국'
            }
        ],
        'genres': [
            {
                'genreNm': '사극'
            },
            {
                'genreNm': '드라마'
            }
        ],
        'directors': [
            {
                'peopleNm': '추창민',
                'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [
            {
                'peopleNm': '이병헌',
                'peopleNmEn': 'LEE Byung-hun',
                'cast': '광해/하선'
            },
            {
                'peopleNm': '류승룡',
                'peopleNmEn': 'RYU Seung-ryong',
                'cast': '허균'
            },
            {
                'peopleNm': '한효주',
                'peopleNmEn': 'HAN Hyo-joo',
                'cast': '중전'
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오.(하)
print(movie['movieInfo']['movieNm'])

# 2. 영화 감독의 영어 이름을 출력하시오.(중)
print(movie['movieInfo']['directors'][0]['peopleNmEn'])

# 3. 영화 배우의 인원을 출력하시오. (상)
print(len(movie['movieInfo']['actors'])
      
# len("python") => 6
# len([1, 2, 3]) => 3
# len((1, 'a')) => 2      

# Sol)
# movie_data = movie('movieInfo') 라는 반복되는 부분을 변수로 지정해서 중복을 줄인다.
```



