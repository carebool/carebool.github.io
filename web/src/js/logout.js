function handleConfirm() {
    // 확인 버튼 클릭 시 처리할 로직
    alert('확인 버튼이 클릭되었습니다.');
    
    // 실제 구현에서는 로그인 페이지로 리다이렉트하거나
    // 모달을 닫는 등의 처리를 할 수 있습니다
    // 예: window.location.href = '/login';
    // 예: document.querySelector('.modal-overlay').style.display = 'none';
}

// ESC 키로 모달 닫기 (선택사항)
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        handleConfirm();
    }
});

// 모달 외부 클릭 시 닫기 (선택사항)
document.querySelector('.modal-overlay').addEventListener('click', function(event) {
    if (event.target === this) {
        handleConfirm();
    }
});