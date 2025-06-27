function closePopup() {
    const popup = document.querySelector('.popup-overlay');
    popup.style.opacity = '0';
    popup.style.transform = 'scale(0.95)';
    setTimeout(() => {
        popup.style.display = 'none';
    }, 300);
}

function donate() {
    alert('CAREBOOL 기부 페이지로 이동합니다.\n소중한 마음 감사드립니다!');
}

// 팝업 열기 애니메이션
window.addEventListener('load', () => {
    const popup = document.querySelector('.popup-overlay');
    popup.style.opacity = '0';
    popup.style.transition = 'all 0.3s ease';
    
    setTimeout(() => {
        popup.style.opacity = '1';
    }, 100);
});

// ESC 키로 팝업 닫기
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closePopup();
    }
});

// 배경 클릭으로 팝업 닫기
document.querySelector('.popup-overlay').addEventListener('click', (e) => {
    if (e.target.classList.contains('popup-overlay')) {
        closePopup();
    }
});

// 진행률 바 애니메이션
setTimeout(() => {
    const progressFill = document.querySelector('.progress-fill');
    progressFill.style.width = '0%';
    progressFill.style.transition = 'width 1.5s ease-out';
    setTimeout(() => {
        progressFill.style.width = '20%';
    }, 500);
}, 800);