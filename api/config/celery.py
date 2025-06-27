import os
from celery import Celery
from celery.schedules import crontab

# Django 설정 모듈 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Celery 앱 생성
app = Celery('config')

# Django 설정에서 Celery 설정 읽기
app.config_from_object('django.conf:settings', namespace='CELERY')

# 자동으로 태스크 발견
app.autodiscover_tasks()

# 주기적인 태스크 설정
app.conf.beat_schedule = {
    'crawl-wildfire-news-every-hour': {
        'task': 'news.tasks.crawl_wildfire_news_task',
        'schedule': crontab(minute=0),  # 매시간 정각에 실행
    },
} 