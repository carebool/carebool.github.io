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
    const tableRows = document.querySelectorAll('.insurance-table tbody tr');
    tableRows.forEach((row, index) => {
        row.style.opacity = '0';
        row.style.transform = 'translateX(-20px)';
        
        setTimeout(() => {
            row.style.transition = 'all 0.4s ease';
            row.style.opacity = '1';
            row.style.transform = 'translateX(0)';
        }, 1200 + (index * 100));
    });
});

// 버튼 핸들러 함수들
function handleInsuranceApplication() {
    alert('추가 보험 신청 페이지로 이동합니다.');
}

function handleDownloadReport() {
    alert('보험 내역 PDF 다운로드를 시작합니다.');
}

function handleGoBack() {
    alert('마이페이지로 돌아갑니다.');
    // window.history.back(); // 실제로는 이렇게 구현
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

// 테이블 행 클릭 이벤트
document.addEventListener('DOMContentLoaded', function() {
    const tableRows = document.querySelectorAll('.insurance-table tbody tr');
    
    tableRows.forEach(row => {
        row.addEventListener('click', function() {
            const insuranceName = this.querySelector('.insurance-name').textContent;
            alert(`${insuranceName} 상세 정보를 확인합니다.`);
        });
        
        // 클릭 가능한 행임을 표시
        row.style.cursor = 'pointer';
    });
});