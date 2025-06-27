# CAREBOOL - 화재 예방 및 보험 정보 플랫폼

<div align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status">
</div>

## 🔥 프로젝트 소개

CAREBOOL은 화재 예방과 보험 정보를 제공하는 종합 플랫폼입니다. 실시간 화재 위험 정보, 맞춤형 보험 추천, 그리고 재난 대응 프로토콜을 제공합니다.

### 🌐 웹사이트
[https://carebool.github.io](https://carebool.github.io)

## 🚀 주요 기능

- **화재 위험 지도**: 실시간 화재 위험 지역 표시
- **보험료 계산기**: 개인 맞춤형 화재보험료 계산
- **화재 통계**: 지역별, 원인별 화재 통계 제공
- **뉴스 및 정보**: 최신 화재 관련 뉴스 및 예방 정보
- **기부 플랫폼**: 화재 피해자 지원 기부 시스템
- **AI 화재 예측**: 머신러닝 기반 화재 위험도 예측

## 🛠️ 기술 스택

### Frontend
- HTML5, CSS3, JavaScript
- Responsive Web Design
- GitHub Pages 호스팅

### Backend
- Django 4.x
- MySQL 8.0
- Django REST Framework
- Celery (비동기 작업)

### AI/ML
- Python
- Scikit-learn
- 화재 예측 모델

### DevOps
- Docker & Docker Compose
- Nginx
- GitHub Actions (CI/CD)

## 📂 프로젝트 구조

```
carebool.github.io/
├── api/                    # Django 백엔드 API
│   ├── config/            # Django 설정
│   ├── disasters/         # 재난 관련 앱
│   ├── insurance/         # 보험 관련 앱
│   ├── news/              # 뉴스 크롤링 앱
│   ├── users/             # 사용자 관리 앱
│   └── manage.py
├── web/                    # 프론트엔드 웹
│   ├── public/            # HTML 파일
│   ├── src/               # CSS, JS, 이미지
│   ├── static/            # 정적 파일
│   └── media/             # 미디어 파일
├── ai-models/             # AI/ML 모델
│   ├── predict_fire_model.pkl
│   └── predictFireModel.py
├── data-management/       # 데이터 관리
│   ├── 화재통계/
│   └── 각종 데이터 처리 스크립트
├── deployment/            # 배포 관련 설정
│   ├── docker/            # Docker 설정
│   ├── nginx/             # Nginx 설정
│   └── github-actions/    # CI/CD 워크플로우
├── index.html             # GitHub Pages 메인 페이지
├── .github/workflows/     # GitHub Actions
└── README.md
```

## 🚀 배포

### GitHub Pages (Frontend)
- 자동 배포: `main` 브랜치 푸시 시 GitHub Actions를 통해 자동 배포
- URL: https://carebool.github.io

### Backend 배포
백엔드는 별도의 서버에 배포되어야 합니다:
```bash
cd deployment/docker
docker-compose up -d
```

## 💻 로컬 개발 환경 설정

### Frontend
```bash
# 저장소 클론
git clone https://github.com/carebool/carebool.github.io.git
cd carebool.github.io

# 로컬 서버 실행 (Python 3.x)
python -m http.server 8000

# 또는 Node.js 사용
npx http-server
```

### Backend
```bash
# 환경 변수 설정
cp .env.example .env

# Docker Compose로 실행
cd deployment/docker
docker-compose up -d
```

### AI 모델 개발
```bash
cd ai-models
python predictFireModel.py
```

## 🗂️ 기능별 모듈 설명

### API 모듈 (`/api`)
- Django 기반 RESTful API 서버
- 사용자 인증, 데이터 관리, 비즈니스 로직 처리

### 웹 모듈 (`/web`)
- 사용자 인터페이스
- 반응형 웹 디자인
- API와 통신하여 데이터 표시

### AI 모델 (`/ai-models`)
- 화재 예측 머신러닝 모델
- 데이터 분석 및 예측 알고리즘

### 데이터 관리 (`/data-management`)
- CSV 데이터 처리
- 데이터베이스 초기화 스크립트
- 통계 데이터 가공

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👥 팀원

- **개발팀**: 공모자들
- **문의**: contact@carebool.com

## 🙏 감사의 말

화재 예방과 안전한 사회를 위해 노력하는 모든 분들께 감사드립니다.

---

<div align="center">
  <p>Made with ❤️ by 공모자들</p>
  <p>© 2024 CAREBOOL. All rights reserved.</p>
</div>
