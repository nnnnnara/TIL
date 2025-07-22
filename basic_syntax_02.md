# List
여러 개의 값을 순서대로 저장하는, 변경 가능한(mutable) 시퀀스 자료형

리스트 표현
- 대괄호 [] 안에 값들을 쉼표(,)로 구분
- 숫자, 문자열, 심지어 다른 리스트까지 모든 종류의 데이터를 담을 수 있음
- 값을 추가, 수정, 삭제하는 등 자유롭게 변경 가능
```[python]
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```

### 시퀀스로서의 리스트
리스트는 시퀀스이므로, 문자열처럼 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능을 모두 사용 가능
```[python]
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1]) # a

# 슬라이싱
print(my_list[2:4]) # [3, 'b']
print(my_list[:3]) # [1, 'a', 3]
print(my_list[3:]) # ['b', 5]
print(my_list[::2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list)) # 5
```
### 중첩 리스트 (Nested List)
다른 리스트를 값으로 가진 리스트
- 인덱스를 연달아 사용하여 안쪽 리스트의 값에 접근할 수 있음
1. 먼저 바깥 리스트의 인덱스로 안쪽 리스트를 선택
   - my_list[4] = ['hello', 'world', '!!!']
2. 선택된 안쪽 리스트에 다시 한번 인덱스를 사용
    - my_list[4][-1] = '!!!'
```[python]
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(my_list)) # 5
print(my_list[4][-1]) # !!!
print(my_list[-1][1][0]) # w
```
### 리스트의 가변성
여러 개의 값을 순서대로 저장하는, **변경 가능한(mutable)** 시퀀스 자료형

한번 생성된 리스트는 "그 내용을 자유롭게 수정, 추가, 삭제할 수 있다"는 뜻 -> 문자의 불변성(Immutability)과 정반대되는 중요 특징

1. 인덱싱으로 값 수정하기
   ```[python]
   my_list = [1, 2, 3, 4, 5]

   my_list[1] = 'two'

   print(my_list)  # [1, 'two', 3, 4, 5]
   ```
2. 슬라이싱으로 여러 값 한번에 바꾸기
   ```[python]
   my_list = [1, 2, 3, 4, 5]

   my_list[2:4] = ['three', 'four']

   print(my_list)  # [1, 2, 'three', 'four', 5]
   ```
# Tuple
여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

튜플 표현
- 소괄호 () 안에 값들을 쉼표로 구분하여 만듦
- 모든 종류의 데이터를 담을 수 있음
- 리스트와 거의 모든 면에서 비슷하지만, 한번 만들어지면 절대 수정할 수 없다는 결정적 차이
```[python]
my_tuple_1 = ()
my_tuple_2 = (1, )
my_tuple_3 = (1, 'a', 3, 'b', 5)
my_tuple_4 = 1, 'hello', 3.14, True
```
-> 소괄호 없이도 만들 수 있음

-> 단일 요소 튜플을 만들 때는 **반드시 Trailing comma(후행 쉼표)** 를 사용

### 시퀀스로서의 튜플
튜플 역시 시퀀스이므로, 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능을 모두 사용할 수 있음
```[python]
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1]) # a

# 슬라이싱
print(my_tuple[2:4]) # (3, 'b')
print(my_tuple[:3]) # (1, 'a', 3)
print(my_tuple[3:]) # ('b', 5)
print(my_tuple[::2]) # (1, 3, 5)
print(my_tuple[::-1]) # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple)) # 5
```
### 튜플의 불변성
한번 생성된 튜플은 그 내용을 절대 수정, 추가, 삭제할 수 없음
```[python]
my_tuple (1, 'a', 3, 'b', 5)

# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'
```
튜플은 어디에 쓰일까? (튜플이 불변 자료형인 이유)
- 튜플의 불변 특성을 사용하여 내부 동작과 안전한 데이터 전달에 사용됨
- 다중 할당, 값 교환, 함수 다중 반환 값 등
```[python]
# 다중 할당
x, y = 10, 20
print(x) # 10
print(y) # 20

# 실제 내부 동작
(x, y) = (10, 20)
```
```[python]
# 값 교환
x, y = 1, 2
x, y = y, x

# 실제 내부 동작
temp = (y, x) # 튜플 생성
x, y = temp # 튜플 풀어냄
print(x, y) # 2, 1
```
-> 이처럼 튜플은 데이터의 "안정성과 무결성"을 보장

# Range
연속된 정수 시퀀스를 생성하는, 변경 불가능한(immutable) 자료형
- 주로 반복문과 함께 사용되어 특정 횟수만큼 코드를 반복 실행할 때 매우 유용
- 실제로 모든 숫자를 메모리에 저장하는 대신, 시작 값, 끝 값, 간격이라는 '규칙'만 기억하여 메모리를 매우 효율적으로 사용
### range 기분 구문
range()는 1개, 2개, 또는 3개의 매개변수(인자)를 가질 수 있음
```[python]
range(start, stop, step)
```
range 매개변수별 특징
- range(stop)
  - 매개변수가 하나면 stop으로 인식
  - start는 0이, step은 1이 기본값으로 자동 설정
  - range(5) -> 0, 1, 2, 3, 4
- range(start, stop)
  - 매개변수가 두 개면 start와 stop으로 인식
  - step은 1이 기본값으로 자동 설정
  - range(2, 5) -> 2, 3, 4
- range(start, stop, step)
  - 모든 매개변수를 직접 지정
  - range(2, 10, 2) -> 2, 4, 6, 8
```[python]
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)
print(my_range_3) # range(5, 0, -1)

print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3)) # [5, 4, 3, 2, 1]
```
### range의 규칙
1. 값의 범위 규칙
   - stop 값은 생성되는 시퀀스에 절대 포함되지 않음
   - range(1, 5)는 1부터 5 '전'까지의 숫자를 의미하므로, 1, 2, 3, 4가 생성
```[python]
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)


print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)
print(my_range_3) # range(5, 0, -1)
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3)) # [5, 4, 3, 2, 1]
```
-> stop 값 바로 앞에서 시퀀스가 끝난다고 기억

2. 증가/감소 값(step) 규칙
    - step 값은 숫자 시퀀스의 간격과 방향을 결정
    1. step이 양수일 때 (기본값 : 1)
        - 숫자가 start부터 stop을 향해 증가
        - range(1, 10, 2) -> 1, 3, 5, 7, 9
    ```[python]
    # 시작 값이 끝 값보다 작은 경우 (정상)
    print(list(range(1, 5))) # [1, 2, 3, 4]
    # 시작 값이 끝 값보다 큰 경우
    print(list(range(5, 1))) # []
    ```
    2. step이 음수일 때
        - 숫자가 start부터 stop을 향해 감수
        - 이 경우, start 값은 stop 값보다 반드시 커야 함
        - range(10, 1, -2) -> 10, 8, 6, 4, 2
    ```[python]
    # 시작 값이 끝 값보다 큰 경우 (정상)
    print(list(range(5, 1, -1))) # [5, 4, 3, 2]
    # 시작 값이 끝 값보다 작은 경우
    print(list(range(1, 5, -1))) # []
    ```

# Dict
key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

딕셔너리 표현
- 중괄호 { } 안에 값들이 쉼표로 구분되어 있음
- 값 1개는 키와 값이 쌍으로 이루어져 있음
- Key(키)
  - 값을 식별하기 위한 고유한 '이름표' **(중복 불가)**
- Value(값)
  - 키에 해당하는 실제 데이터
- 각 값에는 순서가 없음
```[python]
my_dict_1 = { }
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1) # { }
print(my_dict_2) # {'key': 'value'}
print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}
```
### 딕셔너리 규칙
Key의 규칙
- 고유해야 함
  - Key는 중복될 수 없음
- 변경 불가능한(Immutable) 자료형만 사용 가능
  - O : str, int, float, tuple
  - X : list, dict

Value의 규칙
- 어떤 자료형이든 자유롭게 사용할 수 있음
### 딕셔너리 값 접근
- Key를 사용하여 해당 Value를 꺼내 올 수 있음
- Key에 접근 시 대괄호 [ ] 사용
  ```[python]
  my_dict = {'name': '홍길동', 'age': 25}

  print(my_dict['name']) # '홍길동'
  print(my_dict['test']) # KeyError: 'test'
  ```
-> 존재하지 않는 Key로 접근하면 KeyError가 발생하며 프로그램 멈춤

-> 사전에서 단어(Key)를 찾아 뜻(Value)을 확인하는 것처럼, 딕셔너리는 Key를 통해 Value에 빠르게 접근

>**딕셔너리 값 추가 및 변경**
```[python]
my_dict = {'apple': 12, 'list': [1, 2, 3]}

# 추가
my_dict['banana'] = 50
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
```
TIP : 언제 딕셔너리를 사용?

-> 데이터에 순서X, 각 데이터에 의미 있는 이름을 붙여 관리하고 싶을 때

# Set
순서와 중복이 없는 변경 가능한 자료형

세트 표현
- 중괄호 { } 안에 값들을 쉼표로 구분하여 만듦
- 수학에서의 집합과 동일한 연산 처리 가능
```[python]
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) # set()
print(my_set_2) # {1, 2, 3}
print(my_set_3) # {1}
```
-> 비어있는 딕셔너리와의 혼동을 피하기 위해, 비어있는 세트는 반드시 set() 함수로 만들어야 함

>**세트의 두 가지 핵심 특징**
1. 중복을 허용하지 않음
   - 똑같은 값은 단 하나만 존재할 수 있음
2. 순서가 없음
   - 인덱싱(set[0])이나 슬라이싱(set[0:2])을 사용할 수 없음
### 세트의 집합 연산
- 세트는 수학의 '집합'개념을 그대로 가져와, 두 데이터 그룹 간의 관계를 파악하는 데 매우 효과적
```[python]
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_2) # {3}
```
# Other
### None
파이썬에서 '값이 없음'을 표현하는 특별한 데이터 타입
- 마치 내용물이 없는 '빈 상자'
- 숫자 0이나 빈 문자열(' ')과는 다른, **'값이 존재하지 않음'** 또는 **'아직 정해지지 않음'** 이라는 상태를 나타내기 위해 사용
```[python]
# my_variable에는 아직 아무 값도 할당하고 싶지 않을 때

my_variable = None

print(my_variable) # None
```
### Boolean
'참(True)'과 '거짓(False)' 단 두 가지 값만 가지는 데이터 타입
- 마치 'ON / OFF' 스위치처럼, 프로그램의 흐름을 제어하는 조건문에서 "맞다" 또는 "틀리다"를 판단하는 역할

**Boolean 표현**
- 비교 / 논리 연산의 평가 결과로 사용됨
```[python]
is_active = True
is_logged_in = False

print(is_active) # True
print(is_logged_in) # False
print(10 > 5) # True
print(10 == 5) # False
```
-> 주로 조건 / 반복문과 함께 사용할 예정
# Collection
**여러 개의 값을 하나로 묶어 관리**하는 자료형들을 통칭하는 말
- 여러 물건을 담는 '보관함'과 같으며, 파이썬은 목적에 따라 다양한 종류의 컬렉션을 제공
- str, list, tuple, range, set, dict 데이터 타입이 모두 Collection에 분류

컬렉션명 | 변경 가능 여부 | 순서 존재 여부
|:---:|:---:|:---:|
| str |  X  |  O  |
|list |  O  |  O  |
|tuple|  X  |  O  | 
|dict |  O  |  X  |
| set |  O  |  X  |

### 불변과 가변
컬렉션 타입은 생성 후 내용을 변경할 수 있는지 없는지에 따라 '불변'과 '가변' 두 그룹으로 나뉨
구분|불변 (Immutable)|가변 (Mutable)
:---:|:---:|:---:
특징|변경 불가, 안전성, 예측 가능|변경 가능, 유연성, 효울성
종류|str, tuple, range|list, dict, set
# 형변환 Type Conversion
한 데이터 타입을 **다른 데이터 타입으로 변환**하는 과정
### 암시적 형변환 Implict Conversion
파이썬이 연산 중에 **자동으로 데이터 타입을 변환**하는 것
- 암시적 형변환은 파이썬이 데이터 손실을 막기 위해 더 정밀한 타입으로 자동 변환해주는 규칙
- 마치 작은 '정수 상자'와 큰 '실수 상자'의 내용물을 합칠 때, 더 안전하게 담을 수 있는 큰 '실수 상자'로 알아서 옮겨 담는 것과 같음
- 개발자가 신경 쓰지 않아도 "더 안전한 쪽으로" 파이썬이 처리해주는 것

**암시적 형변환 예시**
- 정수와 실수의 연산에서 정수가 실수로 변환됨
- Boolean과 Numeric Type에서만 가능
```[python]
# 정수(int)와 실수(float)의 덧셈
print(3 + 5.0) # 8.0

# 불리언(bool)과 정수(int)의 덧셈
print(True + 3) # 4

# 불리언간의 덧셈
print(True + False) # 1
```
### 명시적 형변환 Explicit Conversion
개발자가 변환하고 싶은 타입을 **직접 함수로 지정**하여 변환하는 것
- 명시적 형변환은 서로 다른 타입의 데이터를 '호환'되도록 맞추는 과정
- 마치 해외에서 다른 모양의 전기 콘센트에 맞는 '어댑터'를 끼우는 것과 같음
- 파이썬은 타입에 엄격해서, 정수와 문자열을 바로 더할 수 없는 것처럼 모양이 다른 플러그는 바로 연결할 수 없음
  
함수 | 설명 | 예시 | 결과
:---:|:---:|:---:|:---:|
int( )|정수로 변환|int("123")|123
float( )|실수로 변환|float("3.14")|3.14
str( )|문자열로 변환|str(100)|"100"
list( )|리스트로 변환|list("abc")|['a', 'b', 'c']
tuple( )|튜플로 변환|tuple([1,2])|(1, 2)
set( )|세트로 변환|set([1, 2, 2])|{1, 2}

>**str -> int**
- 형식에 맞는 숫자만 가능
```[python]
print(int('1')) # 1

# ValueError: invalid literal for int() with base 10: '3.5'
print(int(3.5))

print(int(3.5)) # 3
print(float(3.5)) # 3.5
```
>**int -> str**
- 모두 가능
```[python]
print(str(1) + '등') # 1등
```
||str|list|tuple|range|set|dict
:---:|:---:|:---:|:---:|:---:|:---:|:---:
str||O|O|X|O|X
list|O||O|X|O|X
tuple|O|O||X|O|X
range|O|O|O||O|X
set|O|O|O|X||X
dict|O|O (key만)|O (key만)|X|O (key만)||

# 연산자
### 산술 연산자
수학적 계산을 위해 사용되는 연산자
기호|연산자
:---:|:---:
-|음수 부호
+|덧셈
-|뺄셈
*|곱셈
/|나눗셈
//|정수 나눗셈(몫)
%|나머지
**|지수 (거듭제곱)
### 복합 연산자
연산과 할당이 함께 이뤄짐
기호|예시|의미
:---:|:---:|:---:|
+=|a += b|a = a + b
-=|a -= b|a = a - b
*=|a *= b|a = a * b
/=|a /= b|a = a / b
//=|a //= b|a = a // b
%=|a %= b|a = a % b
**=|a **= b|a = a ** b
>**복합 연산자 예시**
```[python]
y = 10
y -= 4
print(y) # 6

z = 7
z *= 2
print(z) # 14

w = 15
w /= 4
print(w) # 3.75

q = 20
q // 3
print(q) # 6
```
### 비교 연산자
두 값을 비교하여 그 관계가 맞는지 틀리는지를 True 또는 False로 반환
기호|내용
:---:|:---:
<|미만
<=|이하
\>|초과
\>=|이상
==|같음
!=|같지 않음
is|같음
is not|같지 않음
>**== 연산자**
- 값(데이터)이 같은지를 비교
- 동등성(equality)
- ex) 1 == True의 경우 파이썬이 내부적으로 True를 1로 간주할 수 있으므로 True 결과가 나옴
  ```[python]
  print(2 == 2.0) # True
  print(2 != 2) # False
  print('HI' == 'hi') # False
  print(1 == True) # True
  ```
>**is 연산자**
- 객체 자체가 같은지를 비교
- 식별성(identity)
- 두 변수가 완전히 동일한 객체를 가리키는지, 즉 메모리 주소가 같은지를 확인할 때 사용
  ``` [python]
  # SyntaxWarning: "is" with a literal.
  Did you mean "=="?

  print(1 is True) # False
  print(2 is 2.0) # False
  ```
  -> is는 메모리 주소를 비교하는데, 값 자체를 비교하는 ==를 써야할 곳에 실수로 사용한 것 같다고 파이썬이 알려주는 경고

>**is 대신 ==를 사용해야 하는 이유**
  - 결론 : is는 '정체성'을, ==는 '가치'를 비교하기 대문
  - 두 연산자는 "같다"를 확인하는 목적이 근본적으로 다름
  - is (Identity Operator):
    - 두 변수가 **완전히 동일한 메모리 주소의 객체**를 가리키는지, 즉 '정체성(identity)'이 같은지를 확인
  - == (Equality Operator):
    - 두 변수가 가리키는객체의 내용, 즉 '값(Value)'이 같은지를 확인

>**is를 값 비교에 사용하면 안 되는 이유 - "의도와 다른 결과를 낳음"**
- 아래 코드에서 is는 "두 객체가 메모리상에서 같은 존재인가?"를 묻기 때문에 False가 출력됨
- 하지만 우리가 정말 궁금한 것은 **"두 객체의 값이 논리적으로 같은가?"**이므로 ==를 사용해야 의도에 맞는 True를 얻을 수 있음
```[python]
# 1(정수)과 True(불리언)는 다른 객체이다.
print(1 is True) # False

# 1과 True의 '값'은 논리적으로 같다.
print(1 == True) # True
```
```[python]
# 2(정수)와 2.0(실수)은 다른 객체이다.
print(2 is 2.0) # False

# 2와 2.0의 '값'은 논리적으로 같다.
print(2 == 2.0) # True
```
>**is 연산자는 언제 사용하는가?**
- 주로 싱글턴 객체를 비교 할 때 사용
>**싱글턴(Singleton)객체란?**
- 특정 값에 대해 파이썬 전체에서 **단 하나의 객체만 생성되어 재사용**되는 특별한 객체
- 여러 변수가 이 값을 가지더라도, 모두 **미리 만들어진 하나의 객체**를 함께 가리키게 되므로 항상 같은 메모리 주소를 가짐
- 파이썬의 대표적인 싱글턴 객체: None, True, False

>**싱글턴 객체를 비교할 때**
- is 연산자는 두 변수가 완전히 동일한 객체를 가리키는지, 즉 메모리 주소가 같은지를 확인할 때 사용
- 파이썬 전체에서 **단 하나의 객체만 생성되어 재사용**되는 싱글턴 객체 비교에 적합
```[python]
x = None

# 권장
if x is None:
    print('x는 None입니다.')

# 비권장
if x == None:
    print('x는 None입니다.')
```
```[python]
x = True
y = True

print(x is y) # True
print(True is True) # True
print(False is False) # True
print(None is None) # True
```
>**추가 예시: 리스트나 객체 비교 시 주의사항**
- 리스트 또는 다른 가변 객체(mutable)를 비교할 때, 값 자체가 같은 지 확인하려면 ==를 사용
- 두 변수가 완전히 동일한 객체를 가리키는지를 확인해야 한다면 is를 사용
```[python]
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True (두 리스트 값은 동일)
print(a is b) # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b) # True (같은 객체를 가리키므로 True)
```
>**==와 is 정리**
- 값 비교에는 ==을 사용하고, 객체(레퍼런스) 비교에는 is를 사용하는 것이 원칙
- 숫자나 문자열, 불리언 값 등 동등성(값)을 판단해야 할 때 is를 쓰면 의도치 않은 결과(False)가 나올 수 있으며, 이는 파이썬 내부적인 최적화 타입 차이로 인해 일관성이 깨질 수 있기 때문
- is는 주로 싱글턴 객체에 대한 비교 시 사용
### 논리 연산자
여러 개의 조건을 조합하거나, True/False 값을 반대로 뒤집을 때 사용 (and, or, not이 대표적)
기호|연산자|내용
:---:|:---:|:---:
and|논리곱|두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가
or|논리합|두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가
not|논리부정|단일 피연산자를 부정

>**논리 연산자 활용**
```[python]
print(True and False) # False
print(True or False) # True
print(not True) # False
print(not 0) # True
```
>**비교 연산자와 함께 사용 가능**
```[python]
num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False

name = 'Alice'
age = 25
result = (name == 'Alice) or (Age == 30)
print(result) # True
```
### 단축 연산자
**단축 평가**: 논리 연산에서 **두 번째 피연산자를 평가하지 않고 결과를 결정**하는 동작
>**파이썬의 '참(True)'와 '거짓(False)'에 대한 새로운 시각**
- 단축 평가를 이해하려면, 파이썬이 어떤 값을 '참'으로보고 어떤 값을 '거짓'으로 보는지 알아야 함
- 거짓으로 취급되는 값들
  - False, 숫자 0, 빈 문자열" ", 빈 리스트 [ ], None 등 '비어있거나 없다'는 느낌의 값들
- 참으로 취급되는 값들
  - True 그리고 '거짓'이 아닌 모든 값
  - 1, -10, "hello", [1, 2] 등 내용이 있는 값
>**단축 평가 동작 정리**
- and 연산자
  - 하나라도 '거짓'이면 바로 '거짓'
  - and는 연산을 왼쪽에서 오른쪽으로 진행하다가, 처음 만나는 '거짓'값을 바로 반환
  - 만약 끝까지 갔는데 모든 값이 '참'이면 맨 마지막 '참' 값을 반환
- or 연산자
  - 하나라도 '참'이면 바로 '참'
  - or는 연산을 왼쪽에서 오른쪽으로 진행하다가, 처음 만나는 '참' 값을 바로 반환
  - 만약 끝까지 갔는데 모든 값이 '거짓'이면, 맨 마지막 '거짓' 값을 반환
>**단출평가 and 연산자 예시**
```[python]
item1 = '지도'
item2 = '나침반'

# and는 item1('지도')를 보고 통과
# -> item2('나침반')을 보고 통과
# -> 맨 마지막 값인 '나침반'을 최종 결과로 선택
result = item1 and item2

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건: 나침반
```
```[python]
item1 = '지도'
item2 = ''

# and는 item1('지도')를 보고 통과 -> item2('')를 봄
# -> item2가 '내용 없는 값'이므로, 여기서 멈추고 ''를
# 최종 결과로 선택!
result = item1 and item2

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건: ''
```
```[python]
item1 = ''
item2 = '나침반'

# and는 item1('')을 보자마자 '탈락!'을 외치며 평가를 멈춤
# -> 그 자리에서 바로 ''를 최종 결과로 선택!
# (item2는 쳐다보지도 않음)

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건: ''
```
>**단축 평가를 하는 이유**
- 코드 실행을 최적화 하고, 불필요한 연산을 피할 수 있도록 함
- 단순히 True/False 논리 연산을 넘어, 이처럼 코드의 흐름을 제어하고, 오류를 방지하며, 간결한 코드를 작성하는 데 매우 유용하게 사용되는 파이썬의 중요한 기능
### 멤버십 연산자
특정 값이 시퀀스나 다른 컬렉션 안에 포함되어 있는지 확인하는 연산자
기호|내용
:---:|:---:
in|왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인
not in|왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인
```[python]
word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word) # True
print('z' in word) # False
print(4 not in numbers) # False
print(6 not in numbers) # True
```
### 시퀀스형 연산자
- 시퀀스 자료형(문자열, 리스트, 튜플)에 특별한 의미로 사용되는 연산자
- '+'는 시퀀스를 연결하는 기능을, '*'는 시퀀스를 반복하는 기능을 함

연산자 | 내용
:---:|:---:
+|결합 연산자
*|반복 연산자
```[python]
# Gildong Hong
print('Gildong' + 'Hong')
# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a' + 'b'])
# [1, 2, 1, 2]
print([1, 2] * 2)
```
### 연산자 우선순위
우선순위|연산자|내용
:---:|:---:|:---:
높음|( )|소괄호 grouping
||[ ]|인덱싱, 슬라이싱
||**|거듭제곱
||+, -|단항 연산자 양수/음수
||*, /, //, %|산술 연산자
||+, -|산술 연산자
||<, <=, >, >=, ==, !=|비교 연산자
||is, is not|객체 비교
||in, not in|멤버십 연산자
||not|논리 부정
||and|논리 AND
낮음|or|논리 OR

# 참고
### Trailing Comma
컬렉션의 마지막 요소 뒤에 붙는 쉼표
- Trailing Comma 작성은 '선택사항'
- 단, 하나의 요소로 구성된 튜플을 만들 때는 필수
```[python]
x = 1 # 정수
x = (1) # 정수

x = 1, # 튜플
x = (1,) # 튜플
```
>**Trailing Comma 기본 규칙**
- 각 요소를 별도의 줄에 작성
- 마지막 요소 뒤에 Trailing Comma 추가
- 닫는 괄호는 새로운 줄에 배치
```[python]
items = [
    'item1',
    'item2',
    'item3',
]

config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True,
}
```
>**Trailing Comma 좋은 예시**
```[python]
# Good

items = [
    'item1',
    'item2',
]
my_func(
    'value1',
    'value2',
)
```
>**Trailing Comma 나쁜 예시**
```[python]
# Bad

items = ['item1', 'item2',]
my_func('value1', 'value2',)
```
```[python]
# 한 줄 작성 시에는 불필요

items = ['item1', 'item2']
my_func('value1', 'value2')
```
>**Trailing Comma 장점**
1. 가독성 향상
   - 각 줄이 동일한 패턴을 가짐
   - 코드 리뷰가 용이함
2. 유지보수 용이성
   - 항목 추가/제거가 간단
   - 실수로 인한 구문 오류 방지
# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
### mutable과 immutable
- mutable: list, set, dict
- immutable: str, boolean, int, float, tuple
- 재할당은 변수를 다시 할당하는 것이므로 mutable과 immutable과는 관계 X (재할당 시 메모리 주소 변경)

### 변수간 대입
- mutable한 객체의 변수 간 대입
  - 같은 메모리 주소 가짐
- immutable한 객채의 변수 간 대입
  - b에 자료형 str a 변수 대입 시 같은 메모리 주소
  
### 얕은 복사 (shallow copy)
- list의 슬라이싱을 통한 값 할당
  - 다른 메모리 주소
  - 그래도 얕은 복사에 해당
- mutable 객체 안에 mutable 객체인 경우 문제
- **a와 b의 메모리 주소 값은 다르지만 a[0]과 b[0]은 같은 메모리 주소**
- a[1]의 값 변경 시 b[1]의 값도 변경됨
- copy 모듈의 copy 메소드 또한 얕은 복사
```[python]
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
a[1].append(5)

print(a) # [[1, 2], [3, 4, 5]]
print(b) # [[1, 2], [3, 4, 5]]
```

### 깊은 복사 (deep copy)
- 내부의 객체들까지 모두 새롭게 copy
- copy.deepcopy메소드가 해결
```[python]
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[1].append(5)

print(a) # [[1, 2], [3, 4, 5]]
print(b) # [[1, 2], [3, 4]]
```