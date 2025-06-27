let passwordChangeMode = false;
let isSubmitting = false;

function togglePasswordChange() {
    passwordChangeMode = !passwordChangeMode;
    const passwordFields = document.getElementById('password-fields');
    const button = document.querySelector('.btn-secondary');
    
    if (passwordChangeMode) {
        passwordFields.classList.add('active');
        button.textContent = '취소';
    } else {
        passwordFields.classList.remove('active');
        button.textContent = '비밀번호 변경';
        // 입력 필드 초기화
        document.getElementById('current-password').value = '';
        document.getElementById('new-password').value = '';
        document.getElementById('confirm-password').value = '';
    }
}

function changePassword() {
    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (!currentPassword) {
        alert('현재 비밀번호를 입력해주세요.');
        return;
    }
    
    if (!newPassword || !confirmPassword) {
        alert('새 비밀번호를 입력해주세요.');
        return;
    }

    if (newPassword !== confirmPassword) {
        alert('새 비밀번호가 일치하지 않습니다.');
        return;
    }

    alert('비밀번호가 변경되었습니다.');
    togglePasswordChange();
}

function handleSubmit() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    if (!name || !email || !phone) {
        alert('필수 항목을 모두 입력해주세요.');
        return;
    }

    if (isSubmitting) return;

    isSubmitting = true;
    const submitBtn = document.getElementById('submit-btn');
    const loadingSpinner = document.getElementById('loading-spinner');
    const submitText = document.getElementById('submit-text');

    submitBtn.disabled = true;
    loadingSpinner.style.display = 'block';
    submitText.textContent = '수정중...';

    setTimeout(() => {
        isSubmitting = false;
        submitBtn.disabled = false;
        loadingSpinner.style.display = 'none';
        submitText.textContent = '수정완료';
        alert('개인정보가 수정되었습니다!');
    }, 2000);
}

function handleCancel() {
    if (confirm('수정한 내용이 저장되지 않습니다. 취소하시겠습니까?')) {
        alert('이전 페이지로 이동합니다.');
    }
}

// 페이지 로드 시 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section');
    
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            section.style.transition = 'all 0.6s ease';
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, index * 200);
    });
});