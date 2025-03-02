import requests
from time import sleep
from datetime import datetime, timedelta

url = "https://www.futsalbase.com/api/price/getPriceStadiumTotalList"
reservation_url = "https://www.futsalbase.com/api/reservation/create"

cookie = "s%3ATEix_dAX2wxc1M2XH-N3qicNCGxlzSUg.VAxBic66t8KcZkY%2BvqfbOFRgBJjveVX9nf0Me4ppX2M"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "cookie": "thebase=" + cookie,
    "origin": "https://www.futsalbase.com",
    "referer": "https://www.futsalbase.com/home",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

available_stadium = {f"ST_{i}": [] for i in range(1, 8)}

start_date = datetime(2025, 2, 10)
end_date = datetime(2025, 3, 31) - timedelta(days=1)

# 주중 날짜 리스트 생성
date_list = [
    (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    for i in range((end_date - start_date).days + 1)
    if (start_date + timedelta(days=i)).weekday() < 5
]

print("예약할 날짜 목록:", date_list)

want_time = ["19:00"]
max_retries = 5  # 최대 재시도 횟수
retry_delay = 5  # 실패 시 대기 시간 (초)

while True:
    try:
        for date in date_list:
            print("\n✅ 날짜:", date)
            for stadium in available_stadium.keys():
                data = {"date": date, "stadium_code": stadium}

                # 요청 및 예외 처리
                for attempt in range(max_retries):
                    try:
                        response = requests.post(url, headers=headers, json=data, timeout=10)

                        if response.status_code == 200 and response.json().get("success"):
                            result = response.json().get("result")
                            available_stadium_list = []
                            
                            for sta in result:
                                if sta.get("is_reserved") == 0 and sta.get("is_open") and sta.get("time").split(" ~ ")[0] in want_time:
                                    if date == "2025-03-03":
                                        continue
                                    
                                    res_data = {
                                        "stadium_code": sta.get("stadium_code"),
                                        "time_code": sta.get("time_code"),
                                        "use_date": sta.get("date"),
                                    }

                                    res_response = requests.post(reservation_url, headers=headers, json=res_data)
                                    
                                    available_stadium_list.append({"date": date, "time": sta.get("time")})

                            if available_stadium_list:
                                available_stadium[stadium].append(available_stadium_list)

                        else:
                            print(f"⚠️ 요청 실패 ({response.status_code}): {response.text}")

                        break  # 요청 성공하면 재시도 루프 탈출

                    except requests.exceptions.RequestException as e:
                        print(f"🚨 요청 실패 ({attempt+1}/{max_retries}): {e}")
                        if attempt + 1 < max_retries:
                            sleep(retry_delay)
                        else:
                            print("❌ 최대 재시도 횟수 초과. 다음 요청 진행.")
                
                sleep(0.1)
            
            print("📌 현재 예약 가능 목록:", available_stadium)

    except KeyboardInterrupt:
        print("\n프로그램 종료됨")
        break

    sleep(60)  # 1분 후 다시 실행
