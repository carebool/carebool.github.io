// 탭 전환 함수
function switchTab(tabIndex) {
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach((tab, index) => {
        if (index === tabIndex) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });
}

// 지역 선택 변경 시 결과 업데이트
document.getElementById('regionSelect').addEventListener('change', function() {
    const selectedRegion = this.value;
    updateResults(selectedRegion);
});

// 결과 업데이트 함수
function updateResults(region) {
    const resultsList = document.getElementById('resultsList');
    const regionData = {
        'seoul': { name: '서울특별시', phone: '02-2133-8034' },
        'busan': { name: '부산광역시', phone: '051-888-1234' },
        'daegu': { name: '대구광역시', phone: '053-803-1234' },
        'incheon': { name: '인천광역시', phone: '032-440-1234' },
        'gwangju': { name: '광주광역시', phone: '062-613-1234' },
        'daejeon': { name: '대전광역시', phone: '042-270-1234' },
        'ulsan': { name: '울산광역시', phone: '052-229-1234' },
        'gyeonggi': { name: '경기도', phone: '031-8008-1234' }
    };

    if (region && regionData[region]) {
        const data = regionData[region];
        resultsList.innerHTML = `
            <div class="result-item">
                <div class="result-location">${data.name}</div>
                <div class="result-period">운영기간: 2025-01-01 ~ 2025-12-31</div>
                <div class="result-contact">연락처: ${data.phone}</div>
            </div>
        `;
    } else {
        // 전체 결과 표시
        resultsList.innerHTML = `
            <div class="result-item">
                <div class="result-location">서울특별시</div>
                <div class="result-period">운영기간: 2025-01-01 ~ 2025-12-31</div>
                <div class="result-contact">연락처: 02-2133-8034</div>
            </div>
            <div class="result-item">
                <div class="result-location">부산광역시</div>
                <div class="result-period">운영기간: 2025-01-01 ~ 2025-12-31</div>
                <div class="result-contact">연락처: 051-888-1234</div>
            </div>
            <div class="result-item">
                <div class="result-location">대구광역시</div>
                <div class="result-period">운영기간: 2025-01-01 ~ 2025-12-31</div>
                <div class="result-contact">연락처: 053-803-1234</div>
            </div>
            <div class="result-item">
                <div class="result-location">인천광역시</div>
                <div class="result-period">운영기간: 2025-01-01 ~ 2025-12-31</div>
                <div class="result-contact">연락처: 032-440-1234</div>
            </div>
        `;
    }
}

// 결과 항목 클릭 이벤트
document.addEventListener('click', function(e) {
    if (e.target.closest('.result-item')) {
        const item = e.target.closest('.result-item');
        const location = item.querySelector('.result-location').textContent;
        alert(`${location}의 상세 정보를 확인합니다.`);
    }
});

// 페이지 로드 시 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    const processSteps = document.querySelectorAll('.process-step');
    const resultItems = document.querySelectorAll('.result-item');
    
    processSteps.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'scale(0.9)';
        setTimeout(() => {
            el.style.transition = 'all 0.4s ease';
            el.style.opacity = '1';
            el.style.transform = 'scale(1)';
        }, index * 100);
    });

    resultItems.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateX(-10px)';
        setTimeout(() => {
            el.style.transition = 'all 0.3s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateX(0)';
        }, (index * 100) + 500);
    });
});