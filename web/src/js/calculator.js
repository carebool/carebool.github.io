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
    
    // 실제로는 다른 페이지로 이동해야 하지만, 여기서는 알림으로 대체
    if (tabIndex === 0) {
        alert('공공보험 페이지로 이동합니다.');
    } else if (tabIndex === 2) {
        alert('맞춤 보험료 확인 페이지로 이동합니다.');
    }
}

// 보험료 계산 함수
function calculatePremium() {
    const age = document.getElementById('age').value;
    const amount = document.getElementById('amount').value;
    const period = document.getElementById('period').value;
    const insuranceType = document.querySelector('input[name="insurance_type"]:checked').value;
    
    if (!age || !amount || !period) {
        alert('모든 필수 항목을 입력해주세요.');
        return;
    }
    
    // 결과 업데이트
    document.getElementById('result-age').textContent = age + '세';
    document.getElementById('result-amount').textContent = formatAmount(amount);
    document.getElementById('result-period').textContent = period + '년';
    document.getElementById('result-type').textContent = insuranceType === 'public' ? '일반 화재보험' : '민간 화재보험';
    
    // 간단한 보험료 계산 (실제로는 복잡한 계산 로직이 들어감)
    const basePremium = parseInt(amount) * 0.001;
    const ageFactor = age < 30 ? 0.8 : age < 50 ? 1.0 : 1.2;
    const periodFactor = period;
    const typeFactor = insuranceType === 'public' ? 0.9 : 1.1;
    
    const monthlyPremium = Math.round(basePremium * ageFactor * periodFactor * typeFactor);
    document.getElementById('premium-amount').textContent = `월 ${monthlyPremium.toLocaleString()}원`;
    
    // 애니메이션 효과
    const resultSection = document.querySelector('.result-section');
    resultSection.style.animation = 'none';
    setTimeout(() => {
        resultSection.style.animation = 'slideIn 0.5s ease-out';
    }, 10);
}

// 금액 포맷 함수
function formatAmount(amount) {
    const amountNum = parseInt(amount);
    if (amountNum >= 10000) {
        return (amountNum / 10000) + '억 원';
    } else if (amountNum >= 1000) {
        return (amountNum / 1000) + '천만 원';
    } else {
        return amountNum + '만 원';
    }
}

// 입력 값 변경 시 실시간 계산
document.getElementById('age').addEventListener('input', calculatePremium);
document.getElementById('amount').addEventListener('input', calculatePremium);
document.getElementById('period').addEventListener('input', calculatePremium);
document.querySelectorAll('input[name="insurance_type"]').forEach(radio => {
    radio.addEventListener('change', calculatePremium);
});

// 페이지 로드 시 초기 계산
document.addEventListener('DOMContentLoaded', function() {
    calculatePremium();
});