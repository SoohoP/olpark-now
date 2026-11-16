# 올팍 지금 갈까? (olpark-now)

올림픽공원 주차장 실시간 주차대수와 **평소 대비 혼잡도**를 한 화면에 보여주는 모바일 웹입니다.
2026년도 한국체육산업개발(주) 공공데이터 활용 경진대회 출품용으로 만들고 있습니다.

## 구성

| 경로 | 내용 |
|---|---|
| `collector/collect.py` | 실시간 주차현황 API를 1회 호출해 `data/parking_log.csv`에 한 줄 추가 |
| `.github/workflows/collect.yml` | GitHub Actions로 10분마다 수집기 실행 후 커밋 |
| `data/parking_log.csv` | 수집 기록 (`timestamp_kst, parking_sum, status`) |
| `index.html` | GitHub Pages 웹페이지 |

## 데이터

- 한국체육산업개발주식회사_실시간 주차현황 — 공공데이터포털 [15168686](https://www.data.go.kr/data/15168686/openapi.do)
  - 요청 주소·키는 기관 공공데이터 개방목록에 공개된 값을 사용합니다.
  - 주차대수는 동2문·남2문·북2문 주차구역 합계이며, 장기 주차 차량은 출차가 기록되지 않아 실제보다 많을 수 있습니다(기관 설명).
- 예정: 올림픽공원 2025 차량입출차·공연·날씨 연계 데이터(15164822 / 문화공공데이터광장 API_CPM_009)로 시간대별 기준 패턴 보강

`status`가 `manual`인 행은 수집기 설치 전에 같은 API를 직접 호출해 확인한 값입니다.

## 운영비

GitHub Actions(공개 저장소 무료)와 GitHub Pages만 사용합니다. 별도 서버·유료 서비스가 없습니다.
