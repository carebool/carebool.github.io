// 폼 제출 처리
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const loginBtn = document.getElementById('loginBtn');
    loginBtn.classList.add('loading');
    loginBtn.textContent = '로그인 중';
    
    // 2초 후 원복 (실제로는 서버 응답 처리)
    setTimeout(() => {
        loginBtn.classList.remove('loading');
        loginBtn.textContent = '로그인';
        
        // 데모 알림
        alert('로그인이 완료되었습니다!');
    }, 2000);
});

// 입력 필드 포커스 효과
document.querySelectorAll('.form-input').forEach(input => {
    input.addEventListener('focus', function() {
        this.style.transform = 'translateY(-1px)';
    });
    
    input.addEventListener('blur', function() {
        this.style.transform = 'translateY(0)';
    });
});