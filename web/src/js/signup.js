// 전체 동의 체크박스 기능
document.getElementById('agreeAll').addEventListener('change', function() {
    const checkboxes = document.querySelectorAll('.checkbox-group .checkbox:not(#agreeAll)');
    checkboxes.forEach(checkbox => {
        checkbox.checked = this.checked;
    });
});

// 개별 체크박스 변경 시 전체 동의 상태 업데이트
document.querySelectorAll('.checkbox-group .checkbox:not(#agreeAll)').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const allCheckboxes = document.querySelectorAll('.checkbox-group .checkbox:not(#agreeAll)');
        const checkedCount = document.querySelectorAll('.checkbox-group .checkbox:not(#agreeAll):checked').length;
        document.getElementById('agreeAll').checked = checkedCount === allCheckboxes.length;
    });
});

// 비밀번호 확인 유효성 검사
document.getElementById('passwordConfirm').addEventListener('blur', function() {
    const password = document.getElementById('password').value;
    const passwordConfirm = this.value;
    
    if (password !== passwordConfirm && passwordConfirm !== '') {
        this.style.borderColor = '#e53e3e';
        this.style.boxShadow = '0 0 0 3px rgba(229, 62, 62, 0.1)';
    } else if (password === passwordConfirm && passwordConfirm !== '') {
        this.style.borderColor = '#48bb78';
        this.style.boxShadow = '0 0 0 3px rgba(72, 187, 120, 0.1)';
    } else {
        this.style.borderColor = '#e2e8f0';
        this.style.boxShadow = 'none';
    }
});

// 아이디 중복 확인
function checkUsername() {
    const username = document.getElementById('username').value;
    if (username.length < 4) {
        alert('아이디는 4자 이상 입력해주세요.');
        return;
    }
    
    // 실제로는 서버에서 중복 확인을 해야 함
    setTimeout(() => {
        alert('사용 가능한 아이디입니다.');
    }, 500);
}

// 취소 버튼
document.querySelector('.cancel-button').addEventListener('click', function() {
    if (confirm('회원가입을 취소하시겠습니까?')) {
        window.history.back();
    }
});

// 폼 제출 처리
document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // 필수 약관 동의 확인
    const requiredTerms = document.querySelectorAll('.checkbox-group .checkbox[required]');
    let allAgreed = true;
    
    requiredTerms.forEach(checkbox => {
        if (!checkbox.checked) {
            allAgreed = false;
        }
    });
    
    if (!allAgreed) {
        alert('필수 약관에 동의해주세요.');
        return;
    }
    
    // 비밀번호 확인
    const password = document.getElementById('password').value;
    const passwordConfirm = document.getElementById('passwordConfirm').value;
    
    if (password !== passwordConfirm) {
        alert('비밀번호가 일치하지 않습니다.');
        return;
    }
    
    const signupBtn = document.querySelector('.signup-button');
    signupBtn.textContent = '가입 처리중...';
    signupBtn.disabled = true;
    
    setTimeout(() => {
        signupBtn.textContent = '가입완료';
        signupBtn.disabled = false;
        alert('회원가입이 완료되었습니다!');
    }, 2000);
});