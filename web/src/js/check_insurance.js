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
    
    if (tabIndex === 0) {
        alert('공공보험 페이지로 이동합니다.');
    } else if (tabIndex === 1) {
        alert('내 보험료 계산 페이지로 이동합니다.');
    }
}

// 보험 검색 함수
function searchInsurance() {
    const age = document.getElementById('age').value;
    const region = document.getElementById('region').value;
    const monthlyPayment = document.getElementById('monthly_payment').value;
    const period = document.getElementById('period').value;
    
    if (!age || !region || !monthlyPayment || !period) {
        alert('모든 필수 항목을 입력해주세요.');
        return;
    }
    
    // 애니메이션 효과
    const resultsSection = document.querySelector('.results-section');
    resultsSection.style.animation = 'none';
    setTimeout(() => {
        resultsSection.style.animation = 'slideIn 0.5s ease-out';
    }, 10);
    
    alert('입력하신 조건에 맞는 보험 상품을 찾았습니다!');
}

// 상세보기 버튼 클릭 함수
document.addEventListener('DOMContentLoaded', function() {
    const detailBtns = document.querySelectorAll('.detail-btn');
    detailBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // 상세보기 페이지로 이동하는 로직을 추가해야 합니다.
            alert('상세보기 페이지로 이동합니다.');
        });
    });
});