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
        console.log('필터 변경:', filterType);
        updateChart(filterType);
    });
});

// 차트 업데이트 함수
function updateChart(filterType) {
    const bars = document.querySelectorAll('.bar-group');
    
    // 간단한 데모용 데이터 변경
    bars.forEach((bar, index) => {
        const damageBar = bar.querySelector('.bar.damage');
        let height;
        
        switch(filterType) {
            case 'month':
                height = Math.random() * 60 + 20;
                break;
            case 'region':
                height = Math.random() * 50 + 30;
                break;
            default: // year
                const yearHeights = [85, 60, 75, 50, 80, 35, 70, 45, 30, 25, 20, 15, 12, 10, 8, 6];
                height = yearHeights[index] || 5;
        }
        
        if (damageBar) {
            damageBar.style.height = height + '%';
        }
    });
}

// 바 차트 호버 효과
document.querySelectorAll('.bar').forEach(bar => {
    bar.addEventListener('mouseenter', function() {
        this.style.opacity = '0.8';
    });
    bar.addEventListener('mouseleave', function() {
        this.style.opacity = '1';
    });
});

// 테이블 행 클릭 이벤트
document.querySelectorAll('.stats-table tbody tr').forEach(row => {
    row.addEventListener('click', function() {
        const cells = this.querySelectorAll('td');
        if (cells[0].textContent.trim()) {
            alert(`${cells[0].textContent} 상세 정보: 건수 ${cells[1].textContent}건, 면적 ${cells[2].textContent}ha`);
        }
    });
});