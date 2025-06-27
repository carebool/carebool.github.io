// 탭 버튼 클릭 이벤트
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// 검색 버튼 클릭 이벤트
document.querySelector('.search-btn').addEventListener('click', function() {
    alert('검색 기능이 실행됩니다.');
});

// 지도 마커 클릭 이벤트
document.querySelectorAll('.fire-marker').forEach(marker => {
    marker.addEventListener('click', function() {
        const text = this.textContent.trim();
        alert(`${text} 지역의 상세 정보를 확인합니다.`);
    });
});

// 테이블 행 클릭 이벤트
document.querySelectorAll('.data-table tbody tr').forEach(row => {
    row.addEventListener('click', function() {
        const cells = this.querySelectorAll('td');
        const date = cells[0].textContent;
        const location = cells[1].textContent + ' ' + cells[2].textContent;
        alert(`${date} ${location} 화재 상세 정보를 확인합니다.`);
    });
});

// 지도 마커 호버 효과
document.querySelectorAll('.fire-marker').forEach(marker => {
    marker.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
        this.style.zIndex = '1000';
    });
    marker.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
        this.style.zIndex = 'auto';
    });
});