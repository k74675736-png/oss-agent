작성: Claude code / 확인: (이름)

## 규칙 체크리스트

- [V] 한국어 개조식(~함, ~임)으로 씀
- [V] 파일을 만들거나 고치기 전에 할 일을 먼저 한 줄로 말함
- [V] tools.py, secret.py는 고치지 않음
- [V] 문서 맨 위에 "작성: Claude code / 확인: (이름)" 줄 넣음
- [V] 문서 상단(작성 줄 밑)에 규칙 체크리스트 넣고 V로 표시함

# week09/tools.py 함수 설명

## 개요
- 영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스 정보를 가져오는 도구 파일임
- 사용 라이브러리: `requests`
- API 키는 `secret.py`의 `API_KEY`에서 불러옴
- 요청 주소(`BASE_URL`): `searchDailyBoxOfficeList.json` (일별 박스오피스 목록)
- 들어 있는 함수: `get_boxoffice_rank_1` 1개

## 함수 목록

### `get_boxoffice_rank_1(date)`
- 지정한 날짜의 박스오피스 1위 영화 제목을 돌려줌

| 항목 | 내용 |
|---|---|
| 입력 | `date` (문자열): 8자리 날짜. 예: `"20261013"` |
| 출력 | (문자열): 1위 영화 제목. 예: `"오디세이"` |

**동작 순서**
1. `key`(API 키)와 `targetDt`(날짜)로 요청 파라미터를 만듦
2. `requests.get`으로 API 호출함 (제한 시간 10초)
3. JSON 응답에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼냄
4. 목록 첫 번째 항목(1위)의 `movieNm`(영화 제목)을 돌려줌

**사용 예시**
```python
from tools import get_boxoffice_rank_1

print(get_boxoffice_rank_1("20261013"))  # 오디세이
```

## 참고 / 개선할 점
- JSON 응답을 매개변수와 같은 이름인 `date`에 다시 저장해 읽기 헷갈림. `data` 같은 다른 이름이 나음
- 오류 처리 없음. 날짜 형식 오류, 잘못된 API 키, 빈 결과 목록이면 `KeyError` 또는 `IndexError` 발생함
- 1위 영화만 조회 가능함. 순위를 인자로 받거나 전체 목록을 돌려주도록 확장할 수 있음
- 오늘 날짜는 집계 전이라 결과가 없을 수 있음. 어제 이전 날짜를 넣어야 함
