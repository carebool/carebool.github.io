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

    // 테이블 행 애니메이션
    const tableRows = document.querySelectorAll('.disaster-table tbody tr');
    tableRows.forEach((row, index) => {
        row.style.opacity = '0';
        row.style.transform = 'translateX(-20px)';
        
        setTimeout(() => {
            row.style.transition = 'all 0.4s ease';
            row.style.opacity = '1';
            row.style.transform = 'translateX(0)';
        }, 1200 + (index * 100));
    });

    // 알림 박스 애니메이션
    const alertBox = document.querySelector('.alert-box');
    alertBox.style.opacity = '0';
    alertBox.style.transform = 'translateY(-10px)';
    
    setTimeout(() => {
        alertBox.style.transition = 'all 0.5s ease';
        alertBox.style.opacity = '1';
        alertBox.style.transform = 'translateY(0)';
    }, 600);
});

// 버튼 핸들러 함수들
function handleRefresh() {
    alert('재난 정보를 새로고침합니다.');
    const loading = document.getElementById('loading');
    loading.classList.remove('hidden');
    
    setTimeout(() => {
        loading.classList.add('hidden');
        alert('최신 재난 정보로 업데이트되었습니다.');
    }, 1500);
}

function handleGoBack() {
    alert('이전 페이지로 돌아갑니다.');
}

// 네비게이션 이벤트
document.addEventListener('DOMContentLoaded', function() {
    // 로그인/로그아웃 버튼
    const loginBtns = document.querySelectorAll('.logout-btn');
    loginBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const isLogin = this.textContent === '로그인';
            if (isLogin) {
                alert('로그인 페이지로 이동합니다.');
            } else {
                if (confirm('로그아웃 하시겠습니까?')) {
                    alert('로그아웃 되었습니다.');
                }
            }
        });
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

// 테이블 행 클릭 이벤트
document.addEventListener('DOMContentLoaded', function() {
    const tableRows = document.querySelectorAll('.disaster-table tbody tr');
    
    tableRows.forEach(row => {
        row.addEventListener('click', function() {
            const disasterType = this.querySelector('.disaster-type').textContent;
            const magnitude = this.cells[1].textContent;
            const status = this.cells[2].textContent;
            
            alert(`${disasterType} 상세 정보\n규모: ${magnitude}\n상태: ${status}`);
        });
        
        // 클릭 가능한 행임을 표시
        row.style.cursor = 'pointer';
    });
});

// 실시간 업데이트 시뮬레이션
setInterval(() => {
    const ongoingStatus = document.querySelector('.status-ongoing');
    if (ongoingStatus) {
        // 진행중 상태 깜빡임 효과는 이미 CSS에서 처리
    }
}, 3000);