# 배포 가이드

## 🚀 GitHub Pages 배포 (Frontend)

### 자동 배포 설정
1. GitHub 저장소의 Settings > Pages로 이동
2. Source를 "GitHub Actions"로 설정
3. main 브랜치에 push하면 자동으로 배포됨

### 수동 배포
```bash
# 1. 링크 업데이트 스크립트 실행
python update_links.py

# 2. 정적 파일 복사 (이미 완료됨)
cp -r frontend/src .
cp -r frontend/static .
cp -r frontend/media .

# 3. Git 커밋 및 푸시
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main
```

### 배포 확인
- URL: https://carebool.github.io
- GitHub Actions 탭에서 배포 상태 확인 가능

## 🖥️ Backend 배포

### 1. 서버 요구사항
- Docker & Docker Compose
- 80, 443, 8000 포트 사용 가능
- 최소 2GB RAM

### 2. 환경 설정
```bash
# .env 파일 생성
cp .env.example .env
# .env 파일을 편집하여 실제 값 입력
```

### 3. Docker Compose 실행
```bash
# 백그라운드에서 실행
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 서비스 중지
docker-compose down
```

### 4. SSL 인증서 설정 (선택사항)
Let's Encrypt를 사용한 SSL 설정:
```bash
# Certbot 설치 및 실행
docker run -it --rm --name certbot \
  -v /etc/letsencrypt:/etc/letsencrypt \
  -v /var/lib/letsencrypt:/var/lib/letsencrypt \
  certbot/certbot certonly --webroot \
  -w /var/www/html -d your-domain.com
```

## 🔄 CI/CD (지속적 통합/배포)

### Django API CI/CD
`.github/workflows/api-ci.yml` 파일이 다음을 자동화합니다:

#### 1. 자동 테스트 (모든 PR 및 push)
- Python 의존성 설치
- MySQL 데이터베이스 설정
- Django 마이그레이션 실행
- 단위 테스트 및 통합 테스트
- 코드 커버리지 측정

#### 2. 코드 품질 검사
- Flake8 린팅
- Black 코드 포맷 검사
- isort import 정렬 검사
- 보안 취약점 스캔 (safety)

#### 3. Docker 이미지 빌드
- main 브랜치 push 시 자동 빌드
- 이미지 태깅 및 아티팩트 저장

#### 4. 배포 단계
- **Staging**: dev 브랜치 → 스테이징 서버
- **Production**: main 브랜치 → 프로덕션 서버

### 로컬에서 테스트 실행
```bash
cd api

# 린팅
flake8 .
black --check .
isort --check-only .

# 테스트
python manage.py test
pytest  # 또는 pytest 사용

# 커버리지
coverage run --source='.' manage.py test
coverage report
```

### GitHub Actions 시크릿 설정
Repository Settings > Secrets에서 설정:
- `DEPLOY_HOST`: 배포 서버 주소
- `DEPLOY_USER`: SSH 사용자명
- `DEPLOY_KEY`: SSH 개인키
- `DOCKER_REGISTRY_TOKEN`: Docker 레지스트리 토큰

## 📱 Frontend-Backend 연결

### API 엔드포인트 설정
Frontend JavaScript 파일에서 API URL 업데이트:
```javascript
// 개발 환경
const API_URL = 'http://localhost:8000/api';

// 프로덕션 환경
const API_URL = 'https://your-backend-domain.com/api';
```

### CORS 설정
Backend의 settings.py에서 CORS 허용:
```python
CORS_ALLOWED_ORIGINS = [
    "https://carebool.github.io",
    "http://localhost:8000",
]
```

## 🔧 트러블슈팅

### GitHub Pages 배포 실패
1. Actions 탭에서 에러 로그 확인
2. 저장소 Settings > Pages에서 설정 확인
3. .github/workflows/deploy.yml 파일 검증

### Backend 연결 실패
1. CORS 설정 확인
2. API 엔드포인트 URL 확인
3. 네트워크 방화벽 설정 확인

### CI/CD 파이프라인 실패
1. GitHub Actions 로그 확인
2. 환경 변수 및 시크릿 설정 확인
3. 의존성 버전 충돌 확인

### 정적 파일 로딩 실패
1. 파일 경로 확인 (상대 경로 사용)
2. 대소문자 구분 확인 (Linux 서버)
3. 파일 권한 확인

## 📞 지원
문제가 발생하면 Issues 탭에 문의해주세요. 