># 목표

>### 실습 목표
- **인터넷에 있는 날씨 정보**를 가져와 내가 원하는 정보만 출력
- 전문용어 이해하기
  - 서버: 부탁을 받으면 처리해주거나, 부탁대로 원하는 값을 돌려주는 역할
  - 클라이언트: 부탁하는 역할
- 클라이언트가 서버에 요청하는 두 가지 방법
  - 웹 브라우저를 켜서 주소창에 주소(URL)을 입력
  - 서버에 정보를 요청하는 파이썬 코드 작성


**1. 웹 브라우저를 켜서 URL에 접속**
- 크롬을 켜서 주소창에 아래 URL 입력
  - https://fakestoreapi.com/carts

**2. 서버에 정보를 달라는 파이썬 코드 작성**
- vscode켜고 터미널 창 열기
- 아래 명령어를 실행하여 필요한 도구 설치
    
    `$ pip install requests`
- `test.py` 파일을 만들고, 아래처럼 파이썬 코드를 작성하고 실행
  ```[python]
  import requests

  url = 'https://fakestoreapi.com/carts'
  data = requests.get(url).json()
  print(data)
  ```
>### 파이썬  코드 이해하기
- url
  - 요청을 보내는 서버의 주소
- requests.get(url)
  - 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수
- .json()
  - 내부의 데이터를 JSON(파이썬의 딕셔너리와 비슷함) 형태로 변환해주는 함수
  - JSON에 대한 자세한 설명은 뒷부분에서 다룰 예정
  - 
>### 서버는 어떻게 요청을 해석할까
- 웹  브라우저와 파이썬을 통해 서버에 데이터를 요청하는 방법을 알게 됨
- 그렇다면, 서버는 어떻게 요청을 이해하고 데이터를 반환할까 ?

- 서버에 요청을 보내는 클라이언트는 매우 다양
  - 클라이언트들은 각자 다른 방식으로 요청을 보냄
- 서버가 어떻게 모두 해석 ?
># API 이해하기

>### API
- 클라이언트가 원하는 기능을 수행하기 위해 서버 측에 만들어 놓은 프로그램
  - 기능 예시: 데이터 저장, 조회, 수정, 삭제 등
- 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어둠
  - 클라이언트는 서버가 미리 만들어 놓은 주소로 요청을 보냄

>### 오픈 API
- 외부에서 사용할 수 있도록 무료로 개방(OPEN)된 API
- 사용법은 공식 문서(Docs)에 명시
- 프로젝트에서 사용되는 API
  - OpenWeatherMap API: 기상 데이터 및 날씨 정보를 제공하는 오픈 API
  - 금융상품통합비교공시 API: 금융감독원에서 제공하는 금융 상품 정보를 제공하는 오픈 API

>### 오픈 API 특징 및 주의사항
- 악성 사용자가 100만 개의 계정을 생성해 API에 요청을 보내는 상황
  - 너무 많은 계정에서 동시에 요청을 보내면 서버가 견디지 못함
- 이러한 문제점을 해결하기 위해 오픈 API는 **API KEY** 를 활용하여 사용자를 확인
  - 사용자 인증 혹은 회원가입을 하면 서버에서 API KEY를 발급
  - 서버에 요청할 때 마다 해당 API KEY를 함께 보내 정상적인 사용자인 것을 확인
- API KEY를 가지고 있는 악성 사용자가 1초에 100만 개의 요청을 보내는 상황
  - 서버가 견디지 못하여 정상적인 서비스 불가능
- 일부 오픈 API는 **사용량이 제한**
  - 공식 문서의 일일 및 월간 사용량 제한을 반드시 확인
  - **[주의] 사용량이 초과될 경우 요금이 청구될 수 있음**

># 날씨 데이터 수집
>### JSON
- API가 반환하는 데이터는 어떻게 생겼을까 ?

>### API가 사용하는 데이터 형식 - JSON
- JavaScript Object Notation의 약자. 직역하면 '자바스크립트 객체 표기법'
- 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 텍스트 기반의 데이터 방식**
- 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법 중 하나
- 특징
  - 데이터는 중괄호({ })로 둘러싸인 키-값 쌍의 집합으로 표현
  - 키 = 문자열 / 값 = 다양한 데이터 유형
  - 값은 쉼표로 구분
>### JSON - python 예제
- 파이썬은 JSON을 할용하는 기능을 갖고있음
- 참고
  - 파싱(Parsing)
    - 데이터를 의미 있는 구조로 분석하고 해석하는 과정
  - json.loads()
    - JSON 형식의 문자열을 피싱하여 Python Dictionary 로 변환
>### 날씨 데이터 수집

>OpenWeatherMap API
- 기상 데이터 및 날씨 정보를 제공하는 오픈 API
- 전세계 날씨 데이터를 가져와 날씨, 일일 및 시간 별 예보 등 다양한 정보
- API 사용량 제한
  - 60 calls/minute
  - 1,000,000 calls/month
- 생성형 AI를 활용하여 OpenWeatherMap API 에 대해 검색
>OpenWeatherMap API - KEY 발급
- 사이트 접속 및 회원가입 진행
  - 가입 후 반드시 이메일 인증 완료
- API Keys 탭으로 이동
- API Key 복사
  - API Key를 복사하여 코드에서 활용
>OpenWeatherMap API - 사용법 확인
- 상단 API 탭을 클릭
  - 현재 날씨에 대한 데이터를 사용하기 위해 Current Weather Data의 API doc 클릭
>OpenWeatherMap API - 실습
- 특정 지역의 현재 날씨에 대한 모든 정보 출력하기
  - 공식 문서 참고
  - [참고] 서울의 위도: 37.56 / 경도: 126.97
  - 출력 결과
    - 날짜에 따라 출력 결과는 다를 수 있음
- 서울의 현재 날씨 중 온도만 출력
  - 기본적으로 캘빈(K) 온도를 반환
  - 섭씨 온도 = (캘빈 온도 - 273.15)
  - 출력 결과
      ```[python]
      캘빈 온도: 300.71K
      섭씨 온도: 27.56 C
      ```
- 서울의 현재 날씨에 대한 설명(description) 데이터만 출력
  - 출력 결과
    ```[python]
    '날씨 설명: clear sky'
    ```
  - Json 형태의 데이터를 분석하여 원하는 부분만 가져오도록 구성
    ```[python]
    json_response = requests.get(url).json()
    description = json_response['weather'][0]['description']
    return f'날씨 설명: {description}'
    ```

### 실습 결과
    ```
    import requests
    from pprint import pprint as print

    # url = 'https://fakestoreapi.com/carts'
    # data = requests.get(url).json()
    # print(data)

    api_key = "d7face1d6b293b0647abed6a5d1dcfd6"

    # lat = 37.65
    # lon = 126.97

    # url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    city = "Seoul,KR"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    data = requests.get(url).json()

    kelvin = float(data['main']['temp'])
    celsius = kelvin - 273.15


    print(f'캘빈 온도: {kelvin}K')
    print(f'섭씨 온도: {celsius:.2f}°C')



    def weather_description(url):
        data = requests.get(url).json()
        description = data['weather'][0]['description']
        return f'날씨 설명: {description}'

    print(weather_description(url))
    ```


    