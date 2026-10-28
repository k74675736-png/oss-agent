import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(data):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다.
    
    받는 것: data(문자열) - 8자리 날짜. 예: "20261013"
    돌려주는 것: (문자열) 1위 영화 제목. 예: "오디세이"
    """
    params = {"key": API_KEY, "targetDt": data}
    response=requests.get(BASE_URL, params=params, timeout=10)
    data=response.json()
    movies=data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']