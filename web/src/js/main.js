// 통계 카드 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    const statCards = document.querySelectorAll('.stat-card');
    
    statCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 200);
    });
});

// 뉴스 아이템 클릭 효과
document.querySelectorAll('.news-item').forEach(item => {
    item.addEventListener('click', function() {
        this.style.transform = 'scale(0.98)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
});

// 호버 효과 개선
document.querySelectorAll('.stat-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-4px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// 알림 버튼 클릭 이벤트
document.querySelectorAll('.alert-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        const btnText = this.textContent;
        
        // 클릭 피드백
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
        
        // 데모 알림
        setTimeout(() => {
            alert(`${btnText} 페이지로 이동합니다!`);
        }, 200);
    });
});