# CAREBOOL - 화재 예방 및 보험 정보 플랫폼

<div align="center">
  <h3>🔥 화재로부터 당신의 삶을 지키는 스마트한 선택</h3>
  
  <p>
    <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
    <img src="https://img.shields.io/github/actions/workflow/status/carebool/carebool.github.io/deploy.yml?branch=main&label=build" alt="Build Status">
    <img src="https://img.shields.io/github/actions/workflow/status/carebool/carebool.github.io/api-ci.yml?branch=main&label=tests" alt="Test Status">
  </p>
  
  <p>
    <a href="https://carebool.github.io">🌐 Live Demo</a> •
    <a href="#-주요-기능">주요 기능</a> •
    <a href="#-시작하기">시작하기</a> •
    <a href="./DEPLOYMENT.md">📖 배포 가이드</a> •
    <a href="#-기여하기">기여하기</a>
  </p>
</div>

---

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)
- [시작하기](#-시작하기)
- [배포](#-배포)
- [API 문서](#-api-문서)
- [기여하기](#-기여하기)
- [라이센스](#-라이센스)

## 🎯 프로젝트 소개

CAREBOOL은 AI 기반 화재 예측과 맞춤형 보험 추천을 제공하는 종합 플랫폼입니다. 실시간 화재 위험 정보와 지역별 통계를 기반으로 사용자에게 최적의 화재 예방 솔루션을 제공합니다.

### 핵심 가치
- 🛡️ **예방**: 데이터 기반 화재 위험 예측
- 💰 **보호**: 맞춤형 보험 추천 및 계산
- 🤝 **공동체**: 화재 피해자 지원 기부 플랫폼

## 🚀 주요 기능

### 1. 화재 위험 관리
- 🗺️ **실시간 화재 위험 지도**: 지역별 화재 위험도 시각화
- 📊 **화재 통계 분석**: 원인별, 시간대별, 지역별 상세 통계
- 🔔 **위험 알림**: 고위험 지역 실시간 알림

### 2. 보험 서비스
- 💵 **보험료 계산기**: AI 기반 맞춤형 보험료 산정
- 📋 **보험 상품 비교**: 다양한 화재보험 상품 비교 분석
- 📱 **간편 가입**: 온라인 보험 가입 프로세스

### 3. AI 예측 시스템
- 🤖 **머신러닝 예측 모델**: 화재 발생 가능성 예측
- 📈 **위험도 분석**: 건물별, 지역별 위험도 평가
- 🎯 **맞춤형 추천**: 개인별 예방 조치 추천

### 4. 커뮤니티
- 📰 **실시간 뉴스**: 화재 관련 최신 뉴스 제공
- 💝 **기부 플랫폼**: 화재 피해자 지원 크라우드펀딩
- 📚 **예방 교육**: 화재 예방 가이드 및 교육 자료

## 🛠️ 기술 스택

<table>
<tr>
<td align="center" width="25%">

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
<td align="center" width="25%">

### Backend
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)

</td>
<td align="center" width="25%">

### AI/ML
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

</td>
<td align="center" width="25%">

### DevOps
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)

</td>
</tr>
</table>

## 📂 프로젝트 구조

```
carebool.github.io/
├── 📁 api/                    # Django 백엔드 API
│   ├── config/               # 프로젝트 설정
│   ├── disasters/            # 재난 관리 모듈
│   ├── insurance/            # 보험 서비스 모듈
│   ├── news/                 # 뉴스 크롤링 모듈
│   └── users/                # 사용자 관리 모듈
├── 📁 web/                    # 프론트엔드
│   ├── public/               # HTML 페이지
│   ├── src/                  # CSS, JS, 이미지
│   └── static/               # 정적 리소스
├── 📁 ai-models/              # AI/ML 모델
│   ├── predict_fire_model.pkl
│   └── predictFireModel.py
├── 📁 data-management/        # 데이터 처리
│   └── 화재통계/
├── 📁 deployment/             # 배포 설정
│   ├── docker/               # Docker 구성
│   ├── nginx/                # 웹서버 설정
│   └── github-actions/       # CI/CD 파이프라인
└── 📄 index.html              # 메인 페이지
```

## 🏃 시작하기

### 사전 요구사항
- Python 3.10+
- Docker & Docker Compose
- Git

### 🔧 설치 및 실행

#### 1. 저장소 클론
```bash
git clone https://github.com/carebool/carebool.github.io.git
cd carebool.github.io
```

#### 2. Frontend 실행
```bash
# Python 내장 서버
python -m http.server 8000

# 또는 Node.js
npx http-server
```

#### 3. Backend 실행
```bash
# 환경 변수 설정
cp .env.example .env
# .env 파일 편집

# Docker Compose 실행
cd deployment/docker
docker-compose up -d
```

#### 4. 개발 환경 설정
```bash
# API 개발
cd api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# AI 모델 개발
cd ai-models
pip install -r requirements.txt
python predictFireModel.py
```

## 🚀 배포

CAREBOOL은 프론트엔드와 백엔드를 분리하여 배포합니다.

### GitHub Pages (Frontend)
- 자동 배포: `main` 브랜치 push 시 GitHub Actions로 자동 배포
- URL: https://carebool.github.io

### Backend 배포
- Docker Compose를 통한 컨테이너화 배포
- CI/CD 파이프라인으로 자동화된 테스트 및 배포

📖 **상세한 배포 가이드는 [DEPLOYMENT.md](./DEPLOYMENT.md)를 참조하세요.**

## 📡 API 문서

### 주요 엔드포인트

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/disasters/` | 재난 정보 목록 |
| GET | `/api/insurance/calculate/` | 보험료 계산 |
| GET | `/api/news/` | 최신 뉴스 목록 |
| POST | `/api/users/register/` | 사용자 등록 |
| GET | `/api/ai/predict/` | 화재 위험도 예측 |

자세한 API 문서는 [여기](./api/README.md)를 참조하세요.

## 🧪 테스트

```bash
# Backend 테스트
cd api
python manage.py test

# 코드 품질 검사
flake8 .
black --check .

# 테스트 커버리지
coverage run --source='.' manage.py test
coverage report
```

## 🤝 기여하기

CAREBOOL은 오픈소스 프로젝트입니다. 기여를 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 기여 가이드라인
- 코드 스타일: PEP 8 (Python), ESLint (JavaScript)
- 커밋 메시지: [Conventional Commits](https://www.conventionalcommits.org/)
- PR 전 테스트 필수

## 📝 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👥 팀원

<table>
  <tr>
    <td align="center">
      <b>공모자들</b><br>
        팀장 및 프로젝트 관리 : 강성룡<br>
        프론트엔드 : 김성재, 김태식, 이나리<br>
        백엔드 : 강성룡, 안수현<br>
      <a href="mailto:contact@carebool.com">contact@carebool.com</a>
    </td>
  </tr>
</table>

## 📞 문의

- 📧 Email: contact@carebool.com
- 🐛 Bug Report: [GitHub Issues](https://github.com/carebool/carebool.github.io/issues)
- 💬 Discussion: [GitHub Discussions](https://github.com/carebool/carebool.github.io/discussions)

---

<div align="center">
  <p>
    <b>화재 예방과 안전한 사회를 위해 노력하는 모든 분들께 감사드립니다.</b>
  </p>
  <p>
    Made with ❤️ by <b>공모자들</b><br>
    © 2025 CAREBOOL. All rights reserved.
  </p>
</div>
