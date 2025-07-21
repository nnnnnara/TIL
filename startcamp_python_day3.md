### Git / Git Hub 복습
1. 조장은 홈 디렉토리에 word-ralay 폴더 생성
2. 조장은 github에 word-relay 원격 저장소 생성 및 로컬 저장소와 연결
3. 조장은 로컬 저장소에 README.md 파일과 .gitignore파일을 생성하고 push
4. 조장은 원격 저장소의 collaborator로 조원을 초대하기
    (조장: github 해당 repository -> setting -> collaborators -> add people -> 각 조원들 email or username 입력 후 초대)
    (조원: 각자 이메일에 들어가 조장의 초대를 승낙하기)
5. 조원들은 해당 레포 clone 하기
---
5번까지 각 팀원들도 모두 진행

---

1. 조장과 조원은 add, commit, push, pull을 이용해서 끝말잇기를 진행
2. 규칙)
   1. 순서는 팀 내에서 알아서 정하기
   2. 자신이 끝말잇기 작성 후 push, push 완료 후 완료한 사실을 팀원에게 공유 (README.md에 작성한다.)
   3. 전체 6바퀴 돌면 상황 종료
   4. 전체 6바퀴가 돈 이후에도 연습을 한다면, 순서를 뺏거나 데이터를 섞어서 conflict를 유발하면서 여러가지 실험을 하는 것도 추천!

처음 생성
```[python]
cd ~
mkdir word-relay
cd word-relay
git init
touch README.md
touch .gitignore
git add README.md
git commit -m "first"
git remote add origin #주소
git push origin master
```
조원이 처음 받을 때 (clone)
```[python]
git clone #주소
git add origin
git commit -m "second"
git push origin master
```
주고 받을 때 (push & pull)
```[python]
git pull origin master
git add README.md
git commit -m "third"
git push origin master
```

# 1.  ChatGPT
### Generative AI
오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 콘텐츠르 생성하는 인공지능 모델

-> 최근 언어 및 이미지 분석에서 큰 파급력을 보임
###  Generative / Pre-trained / Transformer
: 생성모델 / 사전 훈련 / 트랜스포머 AI 모델

  -> GPT 모델을 기반으로 한 대화형 AI

  ## ChatGPT 주요 개념
  - Generative AI
    - 기존 패턴을 기반으로 오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 콘텐츠를 생성하는 인공지능 모델
  - Pre-trained
    - 거대 언어 모델 + 추가 학습 데이터 + 추가 강화 학습
  - Transformer
    - 문장 속의 단어 간 관게를 추적해 맥락과 의미를 학습
    - 인간처럼 일관되고 연관성이높은 언어를 구사하여 대화형 작업에 강점

## Transformer : Neural Network Architecture
문장의 맥락을 효과적으로 이해하고 처리 -> Attention 매커니즘
- Self-Attention
  - 입력 데이터 간의 관계와 중요도를 계산
- 병렬 처리 가능
  - RNN과 달리 순차 처리가 필요 없어 속도가 빠름
- 스케일링 가능
  - 대규모 데이터 및 파라미터로 확장 가능

-> GPT 모델은 특히 Transformer의 **디코더** 부분만을 사용

# 2. API
## Interface
- 서로 다른 두 개의 시스템(기기, 소프트웨어 등)이 정보를 교환할 때, 그 사이에 존재하는 접점

    -> 사용자가 기기를 쉽게 동작 시키거나, 기계와 기계가 통신할 때 필요한 '약속된 방식'

- 인터페이스 예시
  - 키보드, 마우스, 모니터: 컴퓨터와 사람 사이의 물리적 인터페이스
  - TV 리모컨: TV와 사람 사이의 인터페이스
  - 자동차 운전대, 페달: 자동차의 내부 장치와 운전자 사이를 연결
  - 스마트폰 터치 스크린: 디지털 인터페이스
- UI (User Interface): 사람(사용자)이 소프트웨어에 접근하는 그래픽적/화면적 요소
  - User Interface 예시: ATM의 언어 선택 화면, 브라우저의 뒤로가기 버튼, 스마트폰 앱의 아이콘 등
  - 눈에 보이지 않는 영역의 통신
    - 실제로는 기계와 기계, 시스템과 시스템 사이에서도 수많은 '인터페이스'를 통해 정보를 주고받고 있음
    - 여기서는 화면(UI)이 없을 뿐, 약속된 방식으로 데이터를 주고받음

**눈에 보이지 않는 영역에서도 수 많은 통신이 이루어지고 있다.**
기계와 기계, 시스템과 시스템 사이에서의 소통

## 클라이언트와 서버
- 웹의 동작 방식
  - 우리가 컴퓨터 혹은 모바일 기기로 웹 페이지, 데이터를 보게 될 때까지 무슨일이 일어날까?
- 클라이언트 (Client): 서비스를 요청하는 쪽
  - 예) 사용자의 웹 브라우저, 모바일 앱
- 서버 (Server): 요청을 받아서 처리하고, 결과를 응답해주는 쪽
  - 예) 웹 서버, 데이터베이스 서버
- 클라이언트와 서버 예시
  - 사용자가 브라우저로 특정 주소(URL)을 요청
  - 서버가 해당 페이지, 데이터 등을 보내줌
## API
- API (Application Programming Interface): 두 소프트웨어(또는 시스템)가 서로 통신할 수 있게 하는 매커니즘
  - '약속된 방식의 인터페이스'로, 특정 규칙에 따라 데이터를 요청하고 응답하는 규칙을 제공
- Application: 특정 기능을 수행하는 모든 소프트웨어
  - 웹/모바일/데스크톱/앱 등, 우리가 만든 서비스나 프로그램도 모두 앱의 일종

**API 활용**
- 소셜 로그인
  - 최근에는 특정 사이트에 직접 회원가입을 하지 않고 다른 소셜 미디어 계정으로 회원가입 및 로그인 하는 경우가 많음
  - 어떻게 가능할까?
  - ChatGPT에서 Google로 회원가입 및 로그인을 진행하는 과정 알아보기
  - 사용자는 ChatGPT 로그인 화면에서 "Google로 계속하기"를 클릭
  - ChatGPT가 제공한 Google 로그인 화면에서 Google 계정으로 로그인 진행
  - Google 로그인 계정으로 로그인을 성공했을 경우 Google API는 ChatGPT에게 로그인에 성공한 인증된 사용자 정보를 넘겨줌
  - 사용자 정보를 넘겨받은 ChatGPT는 해당 정보를 활용해 회원가입 및 로그인을 진행
- 날씨앱
  - 기상 데이터가 들어있는 기상청의 서버
  - 스마트폰의 날씨 앱, 웹사이트의 날씨 정보 등 다양한 서비스들이 이 기상청 서버로부터 데이터를 요청해서 응답을 받음
  - 날씨 데이터를 얻으려면?
    - 기상청 서버에는 날씨 정보를 얻고 싶으면 이런 식으로 요청해야 한다는 지정된 형식들이 작성되어 있음
    - 지역, 날짜, 조회할 내용들(온도, 바람 등)을 제공하는 매뉴얼
  - "이렇게 요청을 보내면, 이렇게 정보를 제공해줄 것이다"라는 매뉴얼
    - 소프트웨어와 소프트웨어 간 지정된 정의(형식)으로 소통하는 수단 -> API
  
      -> 스마트폰의 날씨 앱은 기상청에서 제공하는 API를 통해 기상청 시스템과 대화하여 매일 최신 날씨 정보를 표시할 수 있음
## API Key
## API 정리

# 3. Prompt Engineering

# 4. Vibe Coding