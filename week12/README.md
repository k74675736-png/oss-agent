# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
날짜를 받아 해당 날짜의 KOBIS 영화 1위를 출력함

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
secret.py(API KEY), tools.py

## 설치
.claude\skiils\안에 넣고, 
boxoffice.py rank 날짜 / boxoffice.py audience 날짜 영화제목
으로 사용함

## 바깥으로 요청하는 곳
("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
            "boxoffice/searchDailyBoxOfficeList.json")

## 키
secret.py에 API_KEY='키' 형식으로 저장

## 권한
접근 권한을 물음

## 라이선스
MIT LICENSE, week12 파일 내에 바로 있음
