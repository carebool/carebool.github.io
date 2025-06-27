import os
import pandas as pd
import numpy as np
from disasters.models import AiDataset
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, precision_recall_curve
from imblearn.over_sampling import SMOTE
import pickle

def load_data():
    qs = AiDataset.objects.all().values('time', 'exmn_hmty', 'exmn_tp', 'weather', 'fire_check', 'city_id')
    df = pd.DataFrame.from_records(qs)

    # 결측치 제거 또는 채우기
    df = df.dropna()

    # weather는 문자열 → 숫자 인코딩
    # 문자열을 학습용 숫자로 변형함.
    df['weather'] = df['weather'].astype('category').cat.codes

    # 시간: timestamp로 변환 후 파생 피처 생성
    df['time'] = pd.to_datetime(df['time'])
    df['month'] = df['time'].dt.month
    df['dayofyear'] = df['time'].dt.dayofyear

    df['is_weekend'] = df['time'].dt.weekday >= 5  # 토(5), 일(6)
    df['is_weekend'] = df['is_weekend'].astype(int)  # True/False → 1/0

    return df

def train_ensemble_model():
    df = load_data()
    X = df[['exmn_hmty', 'exmn_tp', 'weather', 'month', 'dayofyear', 'is_weekend', 'city_id']]   # 'is_weekend',
    X = pd.get_dummies(X, columns=['city_id'])  # city_id는 one-hot encoding
    X = X.fillna(0)  # 결측치 처리
    y = df['fire_check']

    # 훈련/테스트 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

    # 불균형 데이터 처리 (SMOTE)
    smote = SMOTE(random_state=42, k_neighbors=5)
    # print(f"Before SMOTE: {Counter(y_train)}")
    X_train, y_train = smote.fit_resample(X_train, y_train)
    # print(f"After SMOTE: {Counter(y_train)}")

    # 모델 정의
    # XGBoost가 메인 성능 담당. 불균형 대응 및 과적합 제어에 탁월하다.
    xgb = XGBClassifier(
        scale_pos_weight=5,  # 13:1이라 비율 조정 (데이터 비율에 따라 수정)
        max_depth=7,
        n_estimators=300,
        learning_rate=0.05,
        use_label_encoder=False,
        eval_metric='logloss',
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    # 단순하고 안정적인 성능, 보조 예측.
    rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        class_weight='balanced',
        min_samples_leaf=3,
        random_state=42
    )

    # 앙상블 모델 (soft voting)
    # 두 모델을 확률 기반으로 조합한다.
    ensemble = VotingClassifier(
        estimators=[('xgb', xgb), ('rf', rf)],
        voting='soft',
        weights=[2, 1]  # XGBoost에 가중치 더 주기
    )

    # 학습
    ensemble.fit(X_train, y_train)

    # 예측 확률 추출
    # y_pred = ensemble.predict(X_test)
    y_proba = ensemble.predict_proba(X_test)[:, 1]

    # 최적 threshold(임계값) 탐색
    prec, rec, thresholds = precision_recall_curve(y_test, y_proba)
    f1 = 2 * (prec * rec) / (prec + rec + 1e-6)
    best_idx = np.argmax(f1)
    best_thresh = thresholds[best_idx]

    print(f"📌 최적 Threshold(임계값) (F1 기준): {best_thresh:.2f}")

    # 성능 출력 (기본 임계값: 0.5)
    y_pred = (y_proba >= 0.5).astype(int)
    print("\n📊 기본 Threshold (0.5) 평가:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"ROC AUC: {roc_auc_score(y_test, y_proba):.4f}")
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # 최적 임계값 적용
    y_pred_opt = (y_proba >= best_thresh).astype(int)
    print("\n✅ 최적 Threshold 적용 결과:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_opt):.4f}")
    print(f"ROC AUC: {roc_auc_score(y_test, y_proba):.4f}")
    print(classification_report(y_test, y_pred_opt))
    print(confusion_matrix(y_test, y_pred_opt))

    # 모델 저장
    fileName = 'ai/predict_fire_model.pkl'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)  # 폴더 없으면 생성
    with open(fileName, 'wb') as f:
        pickle.dump(ensemble, f)

    print(f"✅ 모델이 {fileName}에 저장되었습니다.")


def load_model(fileName='ai/predict_fire_model.pkl'):
    with open(fileName, 'rb') as f:
        model = pickle.load(f)
    print(f"✅ 모델이 {fileName}에서 로드되었습니다.")
    return model

"""
# 모델 불러오기
model = load_model()

# 모델로 예측할 때
y_pred = model.predict(X_new)
y_proba = model.predict_proba(X_new)[:, 1]
"""

