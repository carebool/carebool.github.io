import sys
import os
import django
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import requests
import csv
from datetime import datetime
import pandas as pd
import numpy as np


# 프로젝트 최상위 폴더(여기서는 manage.py가 있는 폴더)를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1. Django 설정 불러오기
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# 2. models import (Django setup 후!)
from disasters.models import CityCategory
from insurance.models import PulicInsurance

# 현재 스크립트 위치 기준 CSV 파일 절대 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 주소를 읽어와 카카오맵에서 데이터를 가져온다.
def get_location_from_address(address):
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {
        "Authorization": "KakaoAK 서비스키", # 여기에 본인의 카카오 API 키를 입력하세요.
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "KA": "sdk/1.0.0 os/python lang/en"
        }
    params = {"query": address}

    response = requests.get(url, headers=headers, params=params)
    result = response.json()

    if result.get("documents"):
        data = result["documents"][0]
        addr = data["address"]
        return {
            "latitude": addr["y"],
            "longitude": addr["x"],
            "region_1depth_name": addr["region_1depth_name"],
            "region_2depth_name": addr["region_2depth_name"],
            "region_3depth_name": addr["region_3depth_name"],
        }
    return None


# 공공기관 보험
@transaction.atomic
def insert_pulic_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("CSV fieldnames:", reader.fieldnames)  # 헤더 필드명 출력
        # 지역,보험명,담당부서명,담당자전화번호,계약자명,피보험자명,청구방법,홈페이지,보험료합계,보장시작,보장종료,보장항목,보장설명,보장금액(원),최종수정일
        for row in reader:
            # row가 비었는지 확인 (빈 줄이면 continue)
            if not any(row.values()):
                continue

            # 지역
            city_name = row['지역'].strip()

            # 보험명, 담당부서명, 담당자전화번호
            insurance_name = row['보험명'].strip()
            manage_department = row['담당부서명'].strip()
            manage_phone = row['담당자전화번호'].strip()

            # 청구방법 + 보장설명
            description_text = ""
            if row['보장설명']:
                description_text += row['보장설명'].strip()

            if row['청구방법']:
                if description_text:
                    description_text += " / "
                description_text += f"청구방법: {row['청구방법'].strip()}"

            # 홈페이지, 보장항목
            gov_site = row['홈페이지'].strip()
            coverage_type = row['보장항목'].strip()

            # 보장금액(원)
            coverage_amount = float(row['보장금액(원)']) if row['보장금액(원)'] else 0

            
            # 날짜 변환
            start_date, end_date = None, None
            try:
                start_date = datetime.strptime(row['보장시작'], '%Y%m%d').date()
            except ValueError:
                print(f"[!] 날짜 오류: {row['보장시작']}")
                continue

            try:
                end_date = datetime.strptime(row['보장종료'], '%Y%m%d').date()
            except ValueError:
                print(f"[!] 날짜 오류: {row['보장종료']}")
                continue


            # 중복 확인 (정확히 동일한 데이터가 존재하는지)
            exists = PulicInsurance.objects.filter(
                insurance_name=insurance_name,
                city_name=city_name,
                coverage_type = coverage_type,
                start_date = start_date,
                end_date = end_date,
                manage_department = manage_department
            ).exists()

            if exists:
                print(f"[!] 중복 발생: {insurance_name} {city_name} {coverage_type} {start_date} {end_date} {manage_department}")
                continue

            # 저장
            PulicInsurance.objects.create(
                insurance_name = insurance_name,
                coverage_type = coverage_type,
                coverage_amount = coverage_amount,
                city_name = city_name,
                description = description_text,
                gov_site = gov_site,
                start_date = start_date,
                end_date = end_date,
                manage_department = manage_department,
                manage_phone = manage_phone
            )


csv_path = os.path.join(BASE_DIR, '시민안전보험_데이터_수정.csv')
insert_pulic_from_csv(csv_path)



