from django.urls import path
# from . import views  # 템플릿 뷰 제거
from .api_views import NewsListAPIView, NaverNewsSearchAPIView

urlpatterns = [
    # API 엔드포인트
    path("api/", NewsListAPIView.as_view(), name="news_api_list"),
    path("api/search/", NaverNewsSearchAPIView.as_view(), name="news_api_search"),
    
    # 관리자용 템플릿 뷰 제거 - 프론트엔드로 분리됨
    # path("admin-preview/", views.news_list, name="news_admin_preview"),
]