// 지역별 데이터 (이미지와 유사한 패턴으로 설정)
const regionData = [
    { name: '서울', damage: 80, incident: 120 },
    { name: '부산', damage: 45, incident: 95 },
    { name: '대구', damage: 35, incident: 85 },
    { name: '인천', damage: 25, incident: 65 },
    { name: '광주', damage: 40, incident: 75 },
    { name: '대전', damage: 15, incident: 50 },
    { name: '울산', damage: 20, incident: 45 },
    { name: '경기', damage: 30, incident: 70 },
    { name: '강원', damage: 90, incident: 130 },
    { name: '충북', damage: 110, incident: 140 },
    { name: '충남', damage: 35, incident: 80 },
    { name: '전북', damage: 25, incident: 60 },
    { name: '전남', damage: 40, incident: 90 },
    { name: '경북', damage: 55, incident: 105 },
    { name: '경남', damage: 65, incident: 115 },
    { name: '제주', damage: 15, incident: 40 }
];

function createBarChart() {
    const chartArea = document.getElementById('chartArea');
    chartArea.innerHTML = '';

    const maxDamage = Math.max(...regionData.map(d => d.damage));
    const maxIncident = Math.max(...regionData.map(d => d.incident));
    const maxValue = Math.max(maxDamage, maxIncident);

    regionData.forEach(region => {
        const container = document.createElement('div');
        container.className = 'bar-container';

        // 피해면적 막대
        const damageBar = document.createElement('div');
        damageBar.className = 'bar damage';
        const damageHeight = (region.damage / maxValue) * 350;
        damageBar.style.height = `${damageHeight}px`;
        damageBar.style.marginRight = '2px';
        damageBar.title = `${region.name} 피해면적: ${region.damage}`;

        // 발생건수 막대
        const incidentBar = document.createElement('div');
        incidentBar.className = 'bar incident';
        const incidentHeight = (region.incident / maxValue) * 350;
        incidentBar.style.height = `${incidentHeight}px`;
        incidentBar.title = `${region.name} 발생건수: ${region.incident}`;

        // 지역명 라벨
        const label = document.createElement('div');
        label.className = 'region-label';
        label.textContent = region.name;

        // 막대들을 나란히 배치
        const barsContainer = document.createElement('div');
        barsContainer.style.display = 'flex';
        barsContainer.style.gap = '1px';
        barsContainer.style.alignItems = 'flex-end';
        barsContainer.appendChild(damageBar);
        barsContainer.appendChild(incidentBar);

        container.appendChild(barsContainer);
        container.appendChild(label);
        chartArea.appendChild(container);

        // 클릭 이벤트
        container.addEventListener('click', () => {
            alert(`${region.name}\n피해면적: ${region.damage}\n발생건수: ${region.incident}`);
        });
    });
}

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
    if (filterType === 'year') {
        alert('년도별 차트로 전환됩니다.');
    } else if (filterType === 'cause') {
        alert('원인별 차트로 전환됩니다.');
    } else {
        createBarChart();
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

// 페이지 로드 시 막대 차트 생성
document.addEventListener('DOMContentLoaded', function() {
    createBarChart();
});