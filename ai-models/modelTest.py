import pandas as pd
import datetime
from ai.predictFireModel import load_model

def modelTest():
    # 원본 데이터
    # 테스트하고 싶은 데이터가 있다면 data_dict을 변경시켜라.
    data_dict = {
        'exmn_hmty': [76.9],        # 평균 습도
        'exmn_tp': [23.6],          # 평균 온도
        'weather': ['rain'],        # 문자열 그대로
        'time': ['2025-06-25'],     # 문자열 → 날짜 처리 필요
        'city_id': [91],            # 도시 id
    }

    # DataFrame 생성
    df = pd.DataFrame(data_dict)

    # 시간: timestamp로 변환 후 파생 피처 생성
    df['time'] = pd.to_datetime(df['time'])
    df['month'] = df['time'].dt.month
    df['dayofyear'] = df['time'].dt.dayofyear

    df['is_weekend'] = df['time'].dt.weekday >= 5  # 토(5), 일(6)
    df['is_weekend'] = df['is_weekend'].astype(int)  # True/False → 1/0

    # weather 인코딩: 학습 때와 같은 매핑 사용해야 함 (예시)
    weather_map = {'snow': 0, 'rain': 1, 'sun': 2}
    df['weather'] = df['weather'].map(weather_map)

    # city_id one-hot 인코딩 (주의: 학습 때 썼던 city_id 목록과 맞춰야 함)
    city_id_encoded = pd.get_dummies(df['city_id'], prefix='city_id')
    
    # 👉 학습에 사용된 전체 city_id 컬럼 목록 (예시: 학습 때 사용된 것과 동일해야 함)
    trained_city_cols = ['city_id_1', 'city_id_2', 'city_id_3', 'city_id_4', 'city_id_5', 'city_id_6', 'city_id_7', 'city_id_8', 'city_id_9', 'city_id_10', 'city_id_11', 'city_id_12', 'city_id_13', 'city_id_14', 'city_id_15', 'city_id_16', 'city_id_17', 'city_id_18', 'city_id_19', 'city_id_20', 'city_id_21', 'city_id_22', 'city_id_23', 'city_id_24', 'city_id_25', 'city_id_26', 'city_id_27', 'city_id_28', 'city_id_29', 'city_id_30', 'city_id_31', 'city_id_32', 'city_id_33', 'city_id_34', 'city_id_35', 'city_id_36', 'city_id_37', 'city_id_38', 'city_id_39', 'city_id_40', 'city_id_41', 'city_id_42', 'city_id_43', 'city_id_44', 'city_id_45', 'city_id_46', 'city_id_47', 'city_id_48', 'city_id_49', 'city_id_50', 'city_id_51', 'city_id_52', 'city_id_53', 'city_id_54', 'city_id_55', 'city_id_56', 'city_id_57', 'city_id_58', 'city_id_59', 'city_id_60', 'city_id_61', 'city_id_62', 'city_id_63', 'city_id_64', 'city_id_65', 'city_id_66', 'city_id_67', 'city_id_68', 'city_id_69', 'city_id_70', 'city_id_71', 'city_id_72', 'city_id_73', 'city_id_74', 'city_id_75', 'city_id_76', 'city_id_77', 'city_id_78', 'city_id_79', 'city_id_80', 'city_id_81', 'city_id_82', 'city_id_83', 'city_id_84', 'city_id_85', 'city_id_86', 'city_id_87', 'city_id_88', 'city_id_89', 'city_id_90', 'city_id_91', 'city_id_92', 'city_id_93', 'city_id_94', 'city_id_95', 'city_id_96', 'city_id_97', 'city_id_98', 'city_id_99', 'city_id_100', 'city_id_101', 'city_id_102', 'city_id_103', 'city_id_104', 'city_id_105', 'city_id_106', 'city_id_107', 'city_id_108', 'city_id_109', 'city_id_110', 'city_id_111', 'city_id_112', 'city_id_113', 'city_id_114', 'city_id_115', 'city_id_116', 'city_id_117', 'city_id_118', 'city_id_119', 'city_id_120', 'city_id_121', 'city_id_122', 'city_id_123', 'city_id_124', 'city_id_125', 'city_id_126', 'city_id_127', 'city_id_128', 'city_id_129', 'city_id_130', 'city_id_131', 'city_id_132', 'city_id_133', 'city_id_134', 'city_id_135', 'city_id_136', 'city_id_137', 'city_id_138', 'city_id_139', 'city_id_140', 'city_id_141', 'city_id_142', 'city_id_143', 'city_id_144', 'city_id_145', 'city_id_146', 'city_id_147', 'city_id_148', 'city_id_149', 'city_id_150', 'city_id_151', 'city_id_152', 'city_id_153', 'city_id_154', 'city_id_155', 'city_id_156', 'city_id_157', 'city_id_158', 'city_id_159', 'city_id_160', 'city_id_161']

    # 누락된 city_id 컬럼 보완
    for col in trained_city_cols:
        if col not in city_id_encoded.columns:
            city_id_encoded[col] = 0
    city_id_encoded = city_id_encoded[trained_city_cols]  # 컬럼 순서도 맞춤

    # 최종 입력 데이터 구성
    X_new = pd.concat([
        df[['exmn_hmty', 'exmn_tp', 'weather', 'month', 'dayofyear', 'is_weekend']],
        city_id_encoded
    ], axis=1)

    # 모델 로드 후 예측
    model = load_model()
    prediction = model.predict(X_new)
    print("🔥 산불 예측 결과:", prediction[0])