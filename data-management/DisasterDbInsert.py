import sys, os, csv, django, requests
import pandas as pd
import numpy as np
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datetime import datetime

# 프로젝트 최상위 폴더(여기서는 manage.py가 있는 폴더)를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1. Django 설정 불러오기
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# 2. models import (Django setup 후!)
from disasters.models import CityCategory, AiDataset, DisasterCategory, DisasterDetail

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

"""
# 도시
csv_path = os.path.join(BASE_DIR, 'CityCategory_Data.csv')
with open(csv_path, newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    print("CSV fieldnames:", reader.fieldnames)  # 헤더 필드명 출력
    for row in reader:
        # row가 비었는지 확인 (빈 줄이면 continue)
        if not any(row.values()):
            continue

        city_name1 = row['city_name1'].strip()
        city_name2 = row.get('city_name2', '').strip() or None

        # 중복 확인 (정확히 동일한 데이터가 존재하는지)
        exists = CityCategory.objects.filter(
            city_name1=city_name1,
            city_name2=city_name2
        ).exists()

        if exists:
            continue

        CityCategory.objects.get_or_create(
            city_name1=city_name1,
            city_name2=city_name2
        )



# 일일날씨 
csv_path = os.path.join(BASE_DIR, '2023_2025_DayWeather.csv')
with open(csv_path, newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    print("CSV fieldnames:", reader.fieldnames)  # 헤더 필드명 출력
    for row in reader:
        # row가 비었는지 확인 (빈 줄이면 continue)
        if not any(row.values()):
            continue

         # 도시 찾기 (지점명 기준)
        city_name = row['지점명'].strip()
        city = CityCategory.objects.filter(city_name2__icontains=city_name).first()

        if city_name == "광주":     # 여기서 광주는 광주광역시다. 경기도 광주시랑 다르다.
            city = CityCategory.objects.filter(city_name1__icontains=city_name).first()
        
        if not city:
            city = CityCategory.objects.filter(city_name1__icontains=city_name).first()
        if not city:
            print(f"[!] 도시 '{city_name}'을(를) 찾을 수 없습니다.")
            continue
        
        
         # 날짜 변환
        try:
            date = datetime.strptime(row['일시'].strip(), "%Y-%m-%d").date()
        except ValueError:
            print(f"[!] 날짜 오류: {row['일시']}")
            continue

        # 값 변환
        exmn_tp = float(row['평균기온(°C)']) if row['평균기온(°C)'].strip() else None
        exmn_hmty = float(row['평균 상대습도(%)']) if row['평균 상대습도(%)'].strip() else None

        # 날씨 판단
        rain_val = row['강수 계속시간(hr)'].strip()
        snow_val = row['일 최심적설(cm)'].strip()

        if rain_val and float(rain_val) > 0:
            weather = "rain"
        elif snow_val and float(snow_val) > 0:
            weather = "snow"
        else:
            weather = "sun"

        # 화재 여부는 기본 False
        fire_check = False

        #print(f"데이터 삽입 {city_name} {city} {date}")
        # 중복 확인 (정확히 동일한 데이터가 존재하는지)
        exists = AiDataset.objects.filter(
            time=date,
            city=city
        ).exists()

        if exists:
            continue

        # 저장
        AiDataset.objects.create(
            time=date,
            city=city,
            exmn_tp=exmn_tp,
            exmn_hmty=exmn_hmty,
            weather=weather,
            fire_check=fire_check
        )



# 결측 날짜를 전날 후날의 평균으로 보완
# 1. 데이터프레임으로 가져오기
qs = AiDataset.objects.all().values()
df = pd.DataFrame.from_records(qs)
df['time'] = pd.to_datetime(df['time'])

# 2. 그룹핑 및 보간 함수 정의
def interpolate_group(group):
    group = group.set_index('time')
    
    # 중복된 인덱스가 있으면 첫 번째 값만 사용
    if group.index.duplicated().any():
        group = group[~group.index.duplicated(keep='first')]
    
    # 날짜 전체 채우기 (누락된 날 포함)
    full_index = pd.date_range(start=group.index.min(), end=group.index.max(), freq='D')
    group = group.reindex(full_index)
    
    # 정수형 컬럼 처리 주의
    numeric_cols = ['exmn_hmty', 'exmn_tp']
    group[numeric_cols] = group[numeric_cols].interpolate(method='linear')
    
    # 범주형(weather) 보간 (앞 값으로 채움)
    group['weather'] = group['weather'].ffill().bfill()
    group['city_id'] = group['city_id'].ffill().bfill()  # city_id는 동일해야 하므로

    # 인덱스를 다시 컬럼으로 복원
    group.reset_index(inplace=True)  # ← index → time 컬럼으로 복원
    group.rename(columns={'index': 'time'}, inplace=True)  # 인덱스 이름 지정
    return group

# 3. city_id 별로 보간 적용
df_grouped = df.groupby('city_id', group_keys=False).apply(interpolate_group, include_groups=False).reset_index(level=0, drop=True).reset_index()

# 4. 기존에 없던 행만 추출
existing_dates = set(zip(df['time'], df['city_id']))
interpolated_dates = set(zip(df_grouped['time'], df_grouped['city_id']))

# 새로 생긴 보간 행만 필터링
df_grouped['row_key'] = list(zip(df_grouped['time'], df_grouped['city_id']))
new_rows = df_grouped[df_grouped['row_key'].isin(interpolated_dates - existing_dates)].drop(columns='row_key')

# 5. 새 객체 생성
new_objs = []
for _, row in new_rows.iterrows():
    new_objs.append(AiDataset(
        time=row['time'].date(),
        exmn_hmty=row['exmn_hmty'],
        exmn_tp=row['exmn_tp'],
        weather=row['weather'],
        fire_check=False,
        city_id=int(row['city_id']),
    ))

AiDataset.objects.bulk_create(new_objs)



# 없는 시군의 데이터를 근처 위치의 데이터를 복사해 추가하기
# 도시 ID 가져오기 (또는 city_name으로 검색)
city_pairs = {
    "동해시": "삼척시",
    "원주시": "횡성군",
    "인제군": "양구군",
    "속초시": ["고성군", "양양군"],     # 강원특별자치도 고성군
    "수원시": ["성남시", "안양시", "안산시", "과천시", "군포시", "의왕시", "용인시", "화성시"],
    "동두천시": ["의정부시", "양주시", "포천시"],
    "인천광역시": ["부천시", "시흥시", "김포시"],
    "서울특별시": ["광명시", "고양시", "구리시", "남양주시", "오산시"],
    "천안시": ["평택시", "안성시", "아산시", "진천군"],
    "양평군": ["하남시", "광주시"],
    "이천시": "여주시",
    "철원군": "연천군",
    "춘천시": "가평군",
    "남해군": "사천시",
    "의령군": "함안군",
    "밀양시": ["창녕군", "청도군"],
    "통영시": "고성군",     # 경상남도 고성군
    "광양시": "하동군",
    "영동군": "김천시",
    "안동시": ["의성군", "예천군"],
    "청송군": "영양군",
    "합천군": "고령군",
    "구미시": ["성주군", "칠곡군"],
    "대구광역시": "경산시",
    "광주광역시": ["나주시", "화순군"],
    "순창군": ["담양군", "곡성군"],
    "순천시": "구례군",
    "강진군": "영암군",
    "목포시": ["신안군", "무안군"],
    "영광군": "함평군",
    "전주시": ["익산시", "완주군"],
    "부안군": "김제시",
    "금산군": "무주군",
    "장수군": "진안군",
    "세종특별자치시": "공주시",
    "부여군": ["논산시", "청양군"],
    "대전광역시": ["계룡시", "옥천군"],
    "서산시": ["당진시", "태안군"],
    "군산시": "서천군",
    "홍성군": "예산군",
    "충주시": ["괴산군", "음성군"],
    "영주시": "단양군",
    "청주시": "증평군",
}

@transaction.atomic
def copy_many_weather_pairs(city_pairs):
    for from_name, to_names in city_pairs.items():
        # 문자열이면 리스트로 바꿔줌
        if isinstance(to_names, str):
            to_names = [to_names]

        # from_city 찾기
        from_city = None
        try:
            from_city = CityCategory.objects.get(city_name2=from_name)
        except ObjectDoesNotExist:
            try:
                from_city = CityCategory.objects.get(city_name1=from_name)
            except ObjectDoesNotExist:
                print(f"[!] 도시 '{from_name}'을(를) 찾을 수 없습니다. (1)")
                continue

        for to_name in to_names:
            to_city = None
            try:
                to_city = CityCategory.objects.get(city_name2=to_name)
            except ObjectDoesNotExist:
                try:
                    to_city = CityCategory.objects.get(city_name1=to_name)
                except ObjectDoesNotExist:
                    print(f"[!] 도시 '{to_name}'을(를) 찾을 수 없습니다. (2)")
                    continue
            except MultipleObjectsReturned:
                if from_name == "속초시":   # 강원특별자치도 고성군
                    to_city = CityCategory.objects.get(city_name1="강원특별자치도", city_name2=to_name)
                elif from_name == "통영시": # 경상남도 고성군
                    to_city = CityCategory.objects.get(city_name1="경상남도", city_name2=to_name)
                else:
                    print(f"[!] 도시 '{to_name}'을(를) 찾을 수 없습니다!. (3)")
                    continue



            print(f"📦 복사: {from_name} → {to_name}")

            # to_city에 이미 있는 날짜는 제외
            to_dates = set(
                AiDataset.objects.filter(city=to_city).values_list("time", flat=True)
            )

            # from_city의 데이터 중에서 to_city에 없는 날짜만 복사
            from_entries = AiDataset.objects.filter(city=from_city).exclude(time__in=to_dates)

            new_data = [
                AiDataset(
                    time=entry.time,
                    city=to_city,
                    exmn_hmty=entry.exmn_hmty,
                    exmn_tp=entry.exmn_tp,
                    weather=entry.weather,
                    fire_check=entry.fire_check
                )
                for entry in from_entries
            ]

            AiDataset.objects.bulk_create(new_data, batch_size=500)

copy_many_weather_pairs(city_pairs)


# 산불 정보를 읽어서 fire_check를 True 시킨다.
@transaction.atomic
def mark_fire_check_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            address = row['FRSTFR_DCLR_ADDR']   # 산불신고주소
            date_str = row['FRSTFR_GNT_DT']     # 산불발화일시
            date = datetime.strptime(date_str, "%Y-%m-%d").date()

            # 주소에서 시/군 추출 (예: "강원특별자치도 양양군..." → "강원특별자치도" "양양군")
            parts = address.split()
            city_keyword1 = None
            city_keyword2 = None

            no_keyword2 = [
                "광주광역시",
                "대구광역시",
                "대전광역시",
                "부산광역시",
                "서울특별시",
                "세종특별자치시",
                "울산광역시",
                "인천광역시",
            ]
            # 시, 군 부분 빼기. 서울시와 서울특별시 둘다 들어있기 때문에 '서울'로 like 찾기 위해
            for index, p in enumerate(parts):
                if index == 0:
                    stop = False
                    city_keyword1 = p[:-1]
                    for strNo in no_keyword2:
                        if city_keyword1 in strNo:
                            stop = True
                            break
                    if stop == True:
                        break
                elif index == 1:
                    if len(p) > 3:
                        city_keyword2 = p[:3]
                    else:
                        city_keyword2 = p[:-1]
                    break

            if not city_keyword1:
                print(f"[!] 주소에서 도시 정보 추출 실패: {address}")
                continue

            # 도시 검색
            city = None

            try:
                if city_keyword2:
                    city = CityCategory.objects.get(city_name2__icontains=city_keyword2)
                else:
                    city = CityCategory.objects.get(city_name1__icontains=city_keyword1)
            except ObjectDoesNotExist:
                try:
                    data = get_location_from_address(address.strip())
                    if data == None:
                        print(f"[!] 도시 미발견1-1: {address.strip()}")
                        continue
                    print(f"도시 미발견이라 카카오맵으로 찾아봄. {data['region_1depth_name']} {data['region_2depth_name']} {data['region_3depth_name']}")
                    print(f"region_2depth_name: {repr(data['region_2depth_name'])}")
                    city_keyword2 = str(data["region_2depth_name"]).strip()[:3]
                    city = CityCategory.objects.get(city_name2__icontains=city_keyword2)
                except ObjectDoesNotExist:
                    city_keyword1 = str(data["region_1depth_name"]).strip()[:2]
                    city = CityCategory.objects.get(city_name1__icontains=city_keyword1)
                except MultipleObjectsReturned:
                    print(f"[!] 도시 미발견1-2: {city_keyword1} {city_keyword2}")
                    continue
            except MultipleObjectsReturned:
                if "강원" in city_keyword1:   # 강원특별자치도 고성군
                    city = CityCategory.objects.get(city_name1="강원특별자치도", city_name2__icontains=city_keyword2)
                elif "경상남" in city_keyword1: # 경상남도 고성군
                    city = CityCategory.objects.get(city_name1="경상남도", city_name2__icontains=city_keyword2)
                elif "양주" == city_keyword2: # 경기도 양주시. 경기도에는 남양주시와 양주시가 있다. 남양주시는 잘 들어갈 테니 양주시를 넣는다.
                    city = CityCategory.objects.get(city_name1="경기도", city_name2="양주시")
                else:
                    print(f"[!] 도시 미발견2: {city_keyword1} {city_keyword2}")
                    continue

            if not city:
                print(f"[!] 도시 미발견3: {city_keyword1} {city_keyword2}")
                continue

            # AiDataset 업데이트
            updated = AiDataset.objects.filter(city=city, time=date).update(fire_check=True)
            if updated:
                print(f"✅ {city_keyword1} {city_keyword2} / {date} → fire_check = True")
            else:
                print(f"⚠️  해당 날짜 데이터 없음: {city_keyword1} {city_keyword2} / {date}")

# 사용 예시
csv_path = os.path.join(BASE_DIR, 'FireMountain_Data.csv')
mark_fire_check_from_csv(csv_path)



# 화재유형
csv_path = os.path.join(BASE_DIR, '화재통계/화재유형.csv')
with open(csv_path, newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    print("CSV fieldnames:", reader.fieldnames)  # 헤더 필드명 출력
    for row in reader:
        # row가 비었는지 확인 (빈 줄이면 continue)
        if not any(row.values()):
            continue

        # 화재유형 가져오기
        name = row['화재유형'].strip()

        # 중복 확인 (정확히 동일한 데이터가 존재하는지)
        exists = DisasterCategory.objects.filter(
            name=name
        ).exists()

        if exists:
            continue

        # 저장.
        # 아직 픽토그램 이미지가 없어서 임시로 넣음.
        DisasterCategory.objects.create(
            name=name,
            pictogram_image="pictogram_image"
        )


# 화재통계
@transaction.atomic
def insert_firedetail_from_csv(file_path):
    with open(csv_path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("CSV fieldnames:", reader.fieldnames)  # 헤더 필드명 출력
        for row in reader:
            # row가 비었는지 확인 (빈 줄이면 continue)
            if not any(row.values()):
                continue

            # 화재유형
            category_name = row['화재유형'].strip()
            category = DisasterCategory.objects.filter(name=category_name).first()

            if not category:
                print(f"[!] 도시 '{category_name}'을(를) 찾을 수 없습니다.")
                continue

            # 도시 찾기 (지점명 기준)
            city_keyword1 = row['시도'].strip()[:-1]
            city_keyword2 = row['시_군_구'].strip()[:3]

            # 도시 검색
            city = None

            try:
                city = CityCategory.objects.get(city_name2__icontains=city_keyword2)
            except ObjectDoesNotExist:
                try:
                    city = CityCategory.objects.get(city_name1__icontains=city_keyword1)
                except ObjectDoesNotExist:
                    data = get_location_from_address(city_keyword1 + ' ' + city_keyword2)
                    if data == None:
                        print(f"[!] 도시 미발견1-1: {city_keyword1 + ' ' + city_keyword2}")
                        continue
                    print(f"도시 미발견이라 카카오맵으로 찾아봄. {data['region_1depth_name']} {data['region_2depth_name']} {data['region_3depth_name']}")
                    print(f"region_2depth_name: {repr(data['region_2depth_name'])}")
                    city_keyword2 = str(data["region_2depth_name"]).strip()[:3]
                    # city_keyword1 = str(data["region_1depth_name"]).strip()[:2]
                    city = CityCategory.objects.get(city_name2__icontains=city_keyword2)
                except MultipleObjectsReturned:
                    if city_keyword2 == "군위군":      # 군위군은 2023년 7월 1일부터 대구광역시로 편입되었다.
                        city = CityCategory.objects.get(city_name1="대구광역시")
                    else:
                        print(f"[!] 도시 미발견1-2: {city_keyword1} {city_keyword2}")
                        continue
            except MultipleObjectsReturned:
                if "강원" in city_keyword1:   # 강원특별자치도 고성군
                    city = CityCategory.objects.get(city_name1="강원특별자치도", city_name2__icontains=city_keyword2)
                elif "경상남" in city_keyword1: # 경상남도 고성군
                    city = CityCategory.objects.get(city_name1="경상남도", city_name2__icontains=city_keyword2)
                elif "양주시" == city_keyword2: # 경기도 양주시. 경기도에는 남양주시와 양주시가 있다. 남양주시는 잘 들어갈 테니 양주시를 넣는다.
                    city = CityCategory.objects.get(city_name1="경기도", city_name2="양주시")
                else:
                    print(f"[!] 도시 미발견2: {city_keyword1} {city_keyword2}")
                    continue

            if not city:
                print(f"[!] 도시 미발견3: {city_keyword1} {city_keyword2}")
                continue
            
            
            # 날짜 변환
            try:
                date = datetime.strptime(row['일시'].strip(), "%Y-%m-%d").date()
            except ValueError:
                print(f"[!] 날짜 오류: {row['일시']}")
                continue

            # 발화요인
            caused = row['발화요인대분류'].strip()

            # 값 변환
            casualty = int(row['인명피해(명)소계']) if row['인명피해(명)소계'].strip() else None
            scale = int(row['재산피해소계']) if row['재산피해소계'].strip() else None

            #print(f"데이터 삽입 {city_name} {city} {date}")
            # 중복 확인 (정확히 동일한 데이터가 존재하는지)
            exists = DisasterDetail.objects.filter(
                occurrence_time=date,
                city=city
            ).exists()

            if exists:
                continue

            # 저장
            DisasterDetail.objects.create(
                category = category,
                city = city,
                occurrence_time = date,
                scale = scale,
                casualty = casualty, 
                caused = caused,
                status = "진화완료",
            )

csv_names = [
    "2018년 화재.csv",
    "2019년 화재.csv",
    "2020년 연간화재통계.csv",
    "2021년 연간화재통계.csv",
    "소방청_연간화재통계_20221231.csv",
    "소방청_연간화재통계_20231231.csv"
]
for cn in csv_names:
    csv_path = os.path.join(BASE_DIR, '화재통계/' + cn)
    insert_firedetail_from_csv(csv_path)

"""
