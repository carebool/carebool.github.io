// 탭 버튼 클릭 이벤트
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// 필터 버튼 클릭 이벤트
document.querySelectorAll('.chart-filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.chart-filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        const filterType = this.dataset.filter;
        updateChart(filterType);
    });
});

// 차트 업데이트 함수
function updateChart(filterType) {
    const pieChart = document.querySelector('.pie-chart');
    const centerLabel = document.querySelector('.pie-center-label');
    const legend = document.querySelector('.pie-legend');
    
    if (filterType === 'year') {
        // 년도별로 변경 시 바 차트로 전환하는 시뮬레이션
        alert('년도별 차트로 전환됩니다.');
    } else if (filterType === 'region') {
        // 지역별 데이터로 변경
        pieChart.style.background = `conic-gradient(
            #ff4444 0deg 144deg,
            #ff6b6b 144deg 216deg,
            #ffb3b3 216deg 288deg,
            #ffd6d6 288deg 360deg
        )`;
        centerLabel.textContent = '40%';
    } else {
        // 원인별 (기본)
        pieChart.style.background = `conic-gradient(
            #ff4444 0deg 122deg,
            #ff6b6b 122deg 212deg,
            #ffb3b3 212deg 284deg,
            #ffd6d6 284deg 328deg,
            #ffe6e6 328deg 360deg
        )`;
        centerLabel.textContent = '34%';
    }
}

// Excel 다운로드 함수
function downloadExcel() {
    alert('Excel 파일이 다운로드됩니다.');
}

// 테이블 행 클릭 이벤트
document.querySelectorAll('.stats-table tbody tr').forEach(row => {
    row.addEventListener('click', function() {
        const cells = this.querySelectorAll('td');
        if (cells[0].textContent.trim()) {
            alert(`${cells[0].textContent} 상세 정보: 건수 ${cells[1].textContent}건, 면적 ${cells[2].textContent}ha`);
        }
    });
});

// 파이 차트 호버 효과
document.querySelector('.pie-chart').addEventListener('mouseover', function() {
    this.style.transform = 'scale(1.05)';
    this.style.transition = 'transform 0.3s ease';
});

document.querySelector('.pie-chart').addEventListener('mouseout', function() {
    this.style.transform = 'scale(1)';
});