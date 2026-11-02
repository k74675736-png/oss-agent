# week09 - 박스오피스 1위 영화 조회

영화진흥위원회(KOBIS) 오픈 API를 호출해서 특정 날짜의 일별 박스오피스 1위 영화 제목을 가져오는 프로그램입니다.

## 파일 구성

| 파일 | 하는 일 |
| ---- | ------- |
| `main.py` | 실행 시작점. `tools` 모듈의 함수를 호출해 2026년 10월 13일의 1위 영화 제목을 출력합니다. |
| `tools.py` | KOBIS API에 요청을 보내고 응답에서 1위 영화 제목을 뽑아내는 함수가 들어 있습니다. |
| `requirements.txt` | 실행에 필요한 파이썬 패키지와 버전 목록입니다. |
| `secret.py` (따로 만들어야 함) | API 키(`API_KEY`)를 보관합니다. 이 폴더에는 없으므로 직접 만들어야 합니다. |

## main.py

```python
import tools
print(tools.get_boxoffice_rank_1("20261013"))
```

- `tools` 모듈을 불러옵니다.
- `get_boxoffice_rank_1("20261013")`을 호출해서 2026-10-13의 박스오피스 1위 영화 제목을 받아 화면에 출력합니다.

## tools.py

### 변수

| 변수명 | 의미 |
| -------- | ------ |
| `API_KEY` | `secret.py`에서 가져오는 KOBIS 오픈 API 인증 키입니다. |
| `BASE_URL` | KOBIS 일별 박스오피스 조회 API의 주소이며, JSON 형식으로 응답을 받습니다. |
| `data` (매개변수) | 조회할 날짜를 8자리 문자열(`YYYYMMDD`)로 받습니다. 예: `"20261013"` |
| `params` | API 요청에 붙는 쿼리 파라미터입니다. `key`에는 API 키, `targetDt`에는 조회 날짜가 들어갑니다. |
| `response` | `requests.get`으로 받은 HTTP 응답 객체입니다. |
| `data` (함수 내부에서 다시 대입) | 응답 JSON을 파이썬 딕셔너리로 바꾼 값입니다. 처음에 날짜를 담던 매개변수 `data`를 이 값이 덮어씁니다. |
| `movies` | 응답 안의 `boxOfficeResult` → `dailyBoxOfficeList`에 있는 영화 목록(리스트)이며, 순위 순서대로 정렬되어 있습니다. |

응답 JSON 안에서 쓰는 키:

- `boxOfficeResult`: 박스오피스 결과 전체
- `dailyBoxOfficeList`: 일별 순위 영화 목록
- `movieNm`: 영화 이름

### 함수

#### `get_boxoffice_rank_1(data)`

입력한 날짜의 박스오피스 1위 영화 제목을 돌려줍니다.

- **입력**: `data`, 8자리 날짜 문자열 (예: `"20261013"`)
- **출력**: 1위 영화 제목 문자열 (예: `"오디세이"`)
- **처리 순서**:
  1. API 키와 날짜로 `params`를 만듭니다.
  2. `BASE_URL`에 GET 요청을 보냅니다. 타임아웃은 10초입니다.
  3. 응답을 JSON으로 바꿉니다.
  4. `dailyBoxOfficeList`에서 첫 번째 항목(`movies[0]`), 즉 1위 영화의 `movieNm` 값을 돌려줍니다.

## requirements.txt

| 패키지 | 역할 |
| -------- | ------ |
| `requests==2.34.2` | HTTP 요청을 보내는 라이브러리이며, 코드에서 직접 사용합니다. |
| `certifi==2026.7.22` | HTTPS 인증서 검증에 쓰는 루트 인증서 모음입니다. (requests가 의존) |
| `charset-normalizer==3.5.2` | 응답의 문자 인코딩을 감지합니다. (requests가 의존) |
| `idna==3.20` | 국제화 도메인 이름을 처리합니다. (requests가 의존) |
| `urllib3==2.8.0` | requests 내부에서 쓰는 저수준 HTTP 클라이언트입니다. (requests가 의존) |

## 실행 방법

1. 패키지를 설치합니다.

   ```
   pip install -r requirements.txt
   ```

2. 같은 폴더에 `secret.py`를 만들고, [KOBIS 오픈 API](https://www.kobis.or.kr/kobisopenapi/)에서 발급받은 키를 넣습니다.

   ```python
   API_KEY = "발급받은_키"
   ```

   이 파일은 git에 커밋하지 않도록 주의하세요.
3. 프로그램을 실행합니다.

   ```
   python main.py
   ```
