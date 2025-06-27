import requests
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from news.models import News
from datetime import datetime
import time

class Command(BaseCommand):
    help = '네이버 뉴스 API를 사용하여 산불 관련 기사 크롤링'

    def handle(self, *args, **kwargs):
        if not settings.NAVER_CLIENT_ID or not settings.NAVER_CLIENT_SECRET:
            self.stdout.write(self.style.ERROR(
                "네이버 API 키가 설정되지 않았습니다. "
                "NAVER_CLIENT_ID와 NAVER_CLIENT_SECRET을 .env 파일에 추가하세요."
            ))
            return
        
        keywords = ['산불', '산불 피해', '산불 예방', '대형 산불', '산불 진화']
        
        for keyword in keywords:
            self.stdout.write(f"\n'{keyword}' 검색 중...")
            self.search_naver_news(keyword)
            time.sleep(0.5)  # API 호출 제한 준수
        
        self.stdout.write(self.style.SUCCESS("\n모든 크롤링 완료!"))
    
    def search_naver_news(self, keyword):
        """네이버 뉴스 API를 사용하여 뉴스 검색"""
        url = "https://openapi.naver.com/v1/search/news.json"
        
        headers = {
            "X-Naver-Client-Id": settings.NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": settings.NAVER_CLIENT_SECRET
        }
        
        params = {
            "query": keyword,
            "display": 30,  # 최대 30개
            "start": 1,
            "sort": "date"  # 최신순
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            items = data.get('items', [])
            
            self.stdout.write(f"  검색 결과: {len(items)}개")
            
            for item in items:
                self.save_news_item(item, keyword)
                
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"  API 호출 오류: {str(e)}"))
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f"  JSON 파싱 오류: {str(e)}"))
    
    def save_news_item(self, item, keyword):
        """뉴스 아이템 저장"""
        try:
            # HTML 태그 제거
            import re
            clean_title = re.sub('<[^<]+?>', '', item.get('title', ''))
            clean_description = re.sub('<[^<]+?>', '', item.get('description', ''))
            
            # 날짜 파싱
            pub_date = item.get('pubDate', '')
            if pub_date:
                # 'Wed, 19 Jun 2024 10:30:00 +0900' 형식 파싱
                from datetime import datetime
                import locale
                try:
                    # 영어 로케일 설정 (Windows에서는 다를 수 있음)
                    pub_date_obj = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
                    crawl_date = pub_date_obj.date()
                except:
                    crawl_date = datetime.now().date()
            else:
                crawl_date = datetime.now().date()
            
            # 중복 확인 및 저장
            news, created = News.objects.get_or_create(
                url=item.get('link', ''),
                defaults={
                    'title': clean_title[:500],  # 제목 길이 제한
                    'source_name': '네이버뉴스',
                    'source_url': item.get('originallink', item.get('link', '')),
                    'category': keyword,
                    'crawl_time': crawl_date,
                    'crawl_status': 'success',
                    'error_message': ''
                }
            )
            
            if created:
                self.stdout.write(f"    ✓ 저장: {clean_title[:50]}...")
            else:
                # 기존 뉴스 업데이트 (선택사항)
                news.title = clean_title[:500]
                news.crawl_time = crawl_date
                news.save()
                self.stdout.write(f"    ↻ 업데이트: {clean_title[:50]}...")
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"    ✗ 저장 오류: {str(e)}"))
    
    def add_arguments(self, parser):
        """명령어 인자 추가"""
        parser.add_argument(
            '--keyword',
            type=str,
            help='특정 키워드만 검색',
        )
        parser.add_argument(
            '--display',
            type=int,
            default=30,
            help='검색 결과 개수 (최대 100)',
        ) 