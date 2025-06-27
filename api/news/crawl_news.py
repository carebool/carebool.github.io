import requests
from django.core.management.base import BaseCommand
from news.models import News
from datetime import datetime

class Command(BaseCommand):
    help = '네이버 뉴스 API로 산불 기사 크롤링'

    def handle(self, *args, **kwargs):
        url = "https://openapi.naver.com/v1/search/news.json"
        headers = {
            "X-Naver-Client-Id": "GJiPk311q6mpszJaG7OE",
            "X-Naver-Client-Secret": "S4tbhoVRey"
        }
        params = {"query": "산불", "display": 20}
        res = requests.get(url, headers=headers, params=params)
        items = res.json().get("items", [])
        for item in items:
            News.objects.get_or_create(
                title=item["title"],
                link=item["link"],
                description=item["description"],
                pub_date=datetime.strptime(item["pubDate"], "%a, %d %b %Y %H:%M:%S +0900")
            )
        self.stdout.write(self.style.SUCCESS("크롤링 완료"))