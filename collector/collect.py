"""올림픽공원 실시간 주차대수 1회 수집 → data/parking_log.csv 에 한 줄 추가.

데이터: 한국체육산업개발주식회사_실시간 주차현황 (공공데이터포털 15168686)
API 주소와 키(PARKING21803504)는 기관 공공데이터 개방목록에 공개된 값이다.
"""
import csv
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://www.ksponco.or.kr/online/main/parkingorsApi.do?apiKey=PARKING21803504"
KST = timezone(timedelta(hours=9))
LOG = Path(__file__).resolve().parent.parent / "data" / "parking_log.csv"
HEADER = ["timestamp_kst", "parking_sum", "status"]


def fetch():
    req = urllib.request.Request(API, headers={"User-Agent": "olpark-now/1.0 (+github.com/SoohoP/olpark-now)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read().decode("utf-8", errors="replace")
    data = json.loads(body)
    return int(data[0]["parking_sum"])


def main():
    now = datetime.now(KST).replace(second=0, microsecond=0)
    try:
        value, status = fetch(), "ok"
    except Exception as e:  # 기록은 남기고 실패 사유는 로그로
        value, status = "", f"error:{type(e).__name__}"
        print(f"fetch failed: {e!r}", file=sys.stderr)
    new_file = not LOG.exists()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(HEADER)
        w.writerow([now.strftime("%Y-%m-%d %H:%M"), value, status])
    print(now.isoformat(), value, status)


if __name__ == "__main__":
    main()
