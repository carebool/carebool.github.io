import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from news.models import News
from datetime import datetime
import time
import re

class Command(BaseCommand):
    help = '네이버 뉴스에서 산불 관련 기사 크롤링'

    def handle(self, *args, **kwargs):
        keywords = ['산불', '산불 피해', '산불 예방', '대형 산불']
        
        for keyword in keywords:
            self.stdout.write(f"'{keyword}' 검색 중...")
            self.crawl_naver_news(keyword)
            time.sleep(1)  # 서버 부하 방지
        
        self.stdout.write(self.style.SUCCESS("모든 크롤링 완료!"))
    
    def crawl_naver_news(self, keyword):
        try:
            # 네이버 뉴스 검색 URL
            base_url = "https://search.naver.com/search.naver"
            params = {
                'where': 'news',
                'query': keyword,
                'sort': '0',  # 최신순
                'photo': '0',
                'field': '0',
                'pd': '0',
                'ds': '',
                'de': '',
                'docid': '',
                'related': '0',
                'mynews': '0',
                'office_type': '0',
                'office_section_code': '0',
                'news_office_checked': '',
                'nso': 'so%3Ar%2Cp%3Aall',
                'is_sug_officeid': '0'
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 뉴스 기사 선택
            news_items = soup.select('div.news_wrap.api_ani_send')
            
            for item in news_items[:10]:  # 최대 10개 기사
                try:
                    # 제목과 링크
                    title_elem = item.select_one('a.news_tit')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get('title', '').strip()
                    url = title_elem.get('href', '').strip()
                    
                    # 언론사 정보
                    press_elem = item.select_one('a.info.press')
                    press_name = press_elem.text.strip() if press_elem else '알 수 없음'
                    
                    # 날짜 정보 추출
                    date_elem = item.select_one('span.info')
                    crawl_date = datetime.now().date()
                    
                    # 중복 확인 및 저장
                    news, created = News.objects.get_or_create(
                        url=url,
                        defaults={
                            'title': title,
                            'source_name': press_name,
                            'source_url': url,
                            'category': keyword,
                            'crawl_time': crawl_date,
                            'crawl_status': 'success',
                            'error_message': ''
                        }
                    )
                    
                    if created:
                        self.stdout.write(f"  ✓ 저장: {title[:50]}...")
                    else:
                        self.stdout.write(f"  - 중복: {title[:50]}...")
                        
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  ✗ 기사 파싱 오류: {str(e)}"))
                    continue
                    
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"크롤링 오류 ({keyword}): {str(e)}"))
            # 오류 로그 저장
            News.objects.create(
                title=f"크롤링 오류 - {keyword}",
                url='',
                source_name='시스템',
                source_url='',
                category=keyword,
                crawl_time=datetime.now().date(),
                crawl_status='error',
                error_message=str(e)
            ) 