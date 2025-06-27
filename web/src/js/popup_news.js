// 뉴스 아이템 클릭 효과
document.querySelectorAll('.news-popup-item').forEach(item => {
    item.addEventListener('click', function() {
        this.style.transform = 'scale(0.98)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
});

// 네비게이션 링크 호버 효과
document.querySelectorAll('.nav-links a, .user-menu a').forEach(link => {
    link.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-1px)';
    });
    
    link.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});