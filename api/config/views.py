from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def serve_html(request, filename):
    """frontend/public 폴더의 HTML 파일을 서비스하는 뷰"""
    try:
        # Docker 컨테이너 내 /frontend/public 경로
        frontend_path = '/frontend/public/' + filename
        with open(frontend_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 상대경로를 nginx 서빙 경로로 변환
        content = content.replace('href="../src/', 'href="/src/')
        content = content.replace('src="../src/', 'src="/src/')
        
        return HttpResponse(content, content_type='text/html; charset=utf-8')
    except FileNotFoundError:
        return HttpResponse(f"페이지를 찾을 수 없습니다: {filename}", status=404)

def main_page(request):
    """메인 페이지 (main.html)를 서비스"""
    return serve_html(request, 'main.html')

def login_page(request):
    """로그인 페이지"""
    return serve_html(request, 'login.html')

def signup_page(request):
    """회원가입 페이지"""
    return serve_html(request, 'signup.html')

def mypage(request):
    """마이페이지"""
    return serve_html(request, 'mypage.html')

def calculator_page(request):
    """보험료 계산기 페이지"""
    return serve_html(request, 'calculator.html')

def public_insurance_page(request):
    """공적보험 페이지"""
    return serve_html(request, 'public_insurance.html')

def check_insurance_page(request):
    """보험 확인 페이지"""
    return serve_html(request, 'check_insurance.html')

def fire_information_page(request):
    """화재 정보 페이지"""
    return serve_html(request, 'fireinformation.html')

def fire_statistics_year_page(request):
    """화재 통계 (연도별) 페이지"""
    return serve_html(request, 'firestatistics_year.html')

def fire_statistics_region_page(request):
    """화재 통계 (지역별) 페이지"""
    return serve_html(request, 'firestatistics_region.html')

def fire_statistics_cause_page(request):
    """화재 통계 (원인별) 페이지"""
    return serve_html(request, 'firestatistics_cause.html')

def instructions_page(request):
    """이용 안내 페이지"""
    return serve_html(request, 'instructions.html')

def donation_page(request):
    """기부 페이지"""
    return serve_html(request, 'donationpage.html')

def edit_information_page(request):
    """정보 수정 페이지"""
    return serve_html(request, 'editinformation.html')

def logout_page(request):
    """로그아웃 페이지"""
    return serve_html(request, 'logout.html')

def needlogin_page(request):
    """로그인 필요 페이지"""
    return serve_html(request, 'needlogin.html')

# 팝업 페이지들
def popup_disaster_page(request):
    return serve_html(request, 'popup_disaster.html')

def popup_news_page(request):
    return serve_html(request, 'popup_news.html')

def popup_private_page(request):
    return serve_html(request, 'popup_private.html')

def popup_protocol_page(request):
    return serve_html(request, 'popup_protocol.html')

def popup_public_page(request):
    return serve_html(request, 'popup_public.html') 