"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("news/", include("news.urls")),
    
    # 메인 페이지
    path("", views.main_page, name="main"),
    
    # 사용자 관련 페이지
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    path("mypage/", views.mypage, name="mypage"),
    path("logout/", views.logout_page, name="logout"),
    path("needlogin/", views.needlogin_page, name="needlogin"),
    path("editinformation/", views.edit_information_page, name="editinformation"),
    
    # 보험 관련 페이지
    path("calculator/", views.calculator_page, name="calculator"),
    path("public_insurance/", views.public_insurance_page, name="public_insurance"),
    path("check_insurance/", views.check_insurance_page, name="check_insurance"),
    
    # 화재 정보 페이지
    path("fireinformation/", views.fire_information_page, name="fireinformation"),
    path("firestatistics_year/", views.fire_statistics_year_page, name="firestatistics_year"),
    path("firestatistics_region/", views.fire_statistics_region_page, name="firestatistics_region"),
    path("firestatistics_cause/", views.fire_statistics_cause_page, name="firestatistics_cause"),
    
    # 기타 페이지
    path("instructions/", views.instructions_page, name="instructions"),
    path("donationpage/", views.donation_page, name="donationpage"),
    
    # 팝업 페이지들
    path("popup_disaster/", views.popup_disaster_page, name="popup_disaster"),
    path("popup_news/", views.popup_news_page, name="popup_news"),
    path("popup_private/", views.popup_private_page, name="popup_private"),
    path("popup_protocol/", views.popup_protocol_page, name="popup_protocol"),
    path("popup_public/", views.popup_public_page, name="popup_public"),
]

# 개발 환경에서만 정적 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
