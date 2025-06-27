from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from .models import News
from .serializers import NewsSerializer
import requests

class NewsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.filter(crawl_status='success')
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'source_name']
    search_fields = ['title', 'source_name']
    ordering_fields = ['crawl_time', 'article_id']
    ordering = ['-crawl_time']

class NaverNewsSearchAPIView(APIView):
    """네이버 API를 통한 실시간 뉴스 검색"""
    
    def get(self, request):
        query = request.GET.get('q', '산불')
        display = int(request.GET.get('display', 10))
        start = int(request.GET.get('start', 1))
        sort = request.GET.get('sort', 'date')  # date(최신순) or sim(정확도순)
        
        if not settings.NAVER_CLIENT_ID or not settings.NAVER_CLIENT_SECRET:
            return Response(
                {'error': '네이버 API 키가 설정되지 않았습니다.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        url = "https://openapi.naver.com/v1/search/news.json"
        headers = {
            "X-Naver-Client-Id": settings.NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": settings.NAVER_CLIENT_SECRET
        }
        params = {
            "query": query,
            "display": min(display, 100),  # 최대 100개
            "start": start,
            "sort": sort
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # HTML 태그 제거
            import re
            for item in data.get('items', []):
                item['title'] = re.sub('<[^<]+?>', '', item.get('title', ''))
                item['description'] = re.sub('<[^<]+?>', '', item.get('description', ''))
            
            return Response(data)
            
        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'네이버 API 호출 오류: {str(e)}'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            ) 