#!/usr/bin/env python
"""
Django SECRET_KEY 생성 스크립트
Docker 없이 로컬에서 실행 가능
"""

import random
import string

def generate_secret_key(length=50):
    """Django 스타일의 SECRET_KEY 생성"""
    # Django가 사용하는 문자 집합
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    
    # 랜덤하게 문자 선택
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("\n=== Django SECRET_KEY Generator ===\n")
    
    # 3개의 다른 키 생성 (선택할 수 있도록)
    print("생성된 SECRET_KEY 옵션들:\n")
    for i in range(3):
        key = generate_secret_key()
        print(f"옵션 {i+1}:")
        print(f"{key}\n")
    
    print("위 키 중 하나를 선택하여 .env 파일의 DJANGO_SECRET_KEY에 붙여넣으세요.")
    print("주의: 이 키는 절대 공개 저장소에 커밋하지 마세요!") 