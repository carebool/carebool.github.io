#!/bin/sh

# 데이터베이스가 준비될 때까지 대기
echo "Waiting for database..."
python wait-for-db.py

# 마이그레이션 실행
echo "Running migrations..."
python manage.py migrate --noinput

# 정적 파일 수집
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Django 서버 실행
echo "Starting Django server..."
exec "$@" 