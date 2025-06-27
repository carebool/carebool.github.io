FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# 🔽 mysqlclient 설치에 필요한 패키지 추가 (중요)
RUN apt-get update \
  && apt-get install -y gcc default-libmysqlclient-dev pkg-config dos2unix \
  && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# entrypoint.sh 실행 권한 부여 및 줄 끝 문자 변환
RUN dos2unix entrypoint.sh && chmod +x entrypoint.sh

ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
