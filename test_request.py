import requests

# 서버 주소 오타 시 에러
# 서버 뒤 요청 데이터 종류 오타 404
url = 'https://fakestoreapi.com/carts'
data = requests.get(url)
print(data) # 200: 정상, 404: 해당 데이터 서버에 없음

data_json = requests.get(url).json()
print(data_json)