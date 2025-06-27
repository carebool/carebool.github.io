// 페이지 로드 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    const loading = document.getElementById('loading');
    
    setTimeout(() => {
        loading.classList.add('hidden');
    }, 800);

    // 섹션 애니메이션
    const sections = document.querySelectorAll('.section');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            section.style.transition = 'all 0.6s ease';
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 1000 + (index * 200));
    });
});

// 버튼 핸들러 함수들
function handleEditProfile() {
    alert('개인정보 수정 페이지로 이동합니다.');
}

function handleGoToMain() {
    alert('메인 페이지로 이동합니다.');
}

function handleDetailView(type) {
    alert(`${type} 자세히 보기`);
}

// 네비게이션 이벤트
document.addEventListener('DOMContentLoaded', function() {
    // 로그아웃 버튼
    document.querySelector('.logout-btn').addEventListener('click', function(e) {
        e.preventDefault();
        if (confirm('로그아웃 하시겠습니까?')) {
            alert('로그아웃 되었습니다.');
        }
    });

    // 확대/축소 기능
    let zoomLevel = 1;
    
    document.querySelector('.zoom-in').addEventListener('click', function(e) {
        e.preventDefault();
        zoomLevel = Math.min(zoomLevel + 0.1, 1.5);
        document.body.style.zoom = zoomLevel;
    });

    document.querySelector('.zoom-out').addEventListener('click', function(e) {
        e.preventDefault();
        zoomLevel = Math.max(zoomLevel - 0.1, 0.8);
        document.body.style.zoom = zoomLevel;
    });
});