# week09/tools.py 설명 노트 (2)

## 한 줄 요약
날짜를 넣으면 영화진흥위원회(KOBIS) 오픈 API에 물어봐서 **그날 박스오피스 1위 영화 제목**을 알려주는 파일입니다.

## 전체 코드
```python
import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(date):
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    date = response.json()
    movies = date['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']
```

## 줄별 설명

| 코드 | 설명 |
|---|---|
| `import requests` | 인터넷으로 HTTP 요청을 보내는 라이브러리를 불러옵니다. |
| `from secret import API_KEY` | `secret.py`에 따로 저장한 API 키를 불러옵니다. 키를 코드에 직접 쓰지 않아 GitHub에 올라가지 않게 합니다. |
| `BASE_URL = (...)` | 일별 박스오피스 목록을 JSON으로 주는 API 주소입니다. |
| `params = {...}` | 요청에 붙일 값입니다. `key`는 API 키, `targetDt`는 조회할 날짜입니다. |
| `requests.get(..., timeout=10)` | API를 호출합니다. 10초 안에 응답이 없으면 포기합니다. |
| `response.json()` | 응답 내용(JSON 글자)을 파이썬 딕셔너리로 바꿉니다. |
| `date['boxOfficeResult']['dailyBoxOfficeList']` | 응답 안에서 영화 순위 목록(리스트)을 꺼냅니다. |
| `movies[0]['movieNm']` | 목록의 첫 번째(1위) 영화의 제목을 돌려줍니다. |

## API 응답 구조 (간단히)
```json
{
  "boxOfficeResult": {
    "dailyBoxOfficeList": [
      { "rank": "1", "movieNm": "오디세이", ... },
      { "rank": "2", "movieNm": "...", ... }
    ]
  }
}
```
→ `dailyBoxOfficeList[0]`이 1위, 그 안의 `movieNm`이 영화 제목입니다.

## 사용 예시
```python
from tools import get_boxoffice_rank_1

print(get_boxoffice_rank_1("20261013"))  # 오디세이
```
- 실행하려면 같은 폴더에 `API_KEY = "발급받은키"`가 들어 있는 `secret.py`가 있어야 합니다.

## 주의할 점
- 함수 안에서 매개변수 `date`에 JSON 응답을 다시 넣고 있어 헷갈립니다. `data`처럼 다른 이름을 쓰면 더 읽기 쉽습니다.
- 날짜 형식이 틀리거나, API 키가 잘못됐거나, 결과가 비어 있으면 `KeyError` / `IndexError`가 납니다. 오류 처리가 없습니다.
- 오늘 날짜는 아직 집계 전이라 결과가 없을 수 있으니 어제 이전 날짜를 넣어야 합니다.
