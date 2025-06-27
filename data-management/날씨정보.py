# Python3 샘플 코드 #

import requests
import urllib3
import pandas as pd
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.safetydata.go.kr/V2/api/DSSP-IF-00183"	
serviceKey = "서비스키"
all_items = []
page = 1
while True:
    params = {
        "serviceKey": serviceKey,
        "returnType": "json",
        "pageNo": str(page),
        "numOfRows": "1000"
    }
    response = requests.get(url, params=params, verify=False)
    data = response.json()

    # 에러 응답 처리
    if data.get("header", {}).get("resultCode") != "00":
        print("API 오류 발생:", data["header"].get("resultMsg"))
        break

    items = data.get("body", [])
    if not items:
        break  # 더 이상 데이터 없음

    all_items.extend(items)
    print(f"{page}페이지 수집 완료, 총 {len(all_items)}건")
    page += 1

# CSV 저장
if all_items:
    df = pd.DataFrame(all_items)
    df.to_csv("날씨정보.csv", index=False, encoding='utf-8-sig')
    print("CSV 저장 완료!")
else:
    print("수집된 데이터가 없습니다.")