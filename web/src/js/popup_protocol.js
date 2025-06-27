// 팝업 닫기
function closePopup() {
    const overlay = document.getElementById('popupOverlay');
    overlay.style.opacity = '0';
    overlay.style.transform = 'scale(0.95)';
    setTimeout(() => {
        overlay.style.display = 'none';
    }, 300);
}

// ESC 키로 팝업 닫기
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closePopup();
    }
});

// 외부 클릭 시 팝업 닫기
document.getElementById('popupOverlay').addEventListener('click', function(e) {
    if (e.target === this) {
        closePopup();
    }
});

// 긴급 연락처 클릭
function callEmergency(number) {
    if (confirm(`${number}에 연결하시겠습니까?`)) {
        window.open(`tel:${number}`, '_self');
    }
}

// 긴급신고 버튼
function handleEmergencyCall() {
    if (confirm('119 긴급신고 센터로 연결하시겠습니까?')) {
        window.open('https://www.119.go.kr/centerapp/po/por/rcp/RcpMain.jsp', '_blank');
    }
}

// 위치공유 버튼
function handleLocationShare() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                
                const mapUrl = `https://map.naver.com/v5/?c=${lng},${lat},15,0,0,0,dh`;
                window.open(mapUrl, '_blank');
                
                alert(`현재 위치가 지도에 표시됩니다.\n위도: ${lat.toFixed(6)}\n경도: ${lng.toFixed(6)}`);
            },
            function(error) {
                alert('위치 정보를 가져올 수 없습니다. 설정을 확인해주세요.');
            }
        );
    } else {
        alert('이 브라우저는 위치 서비스를 지원하지 않습니다.');
    }
}

// 상세정보 버튼
function handleMoreInfo() {
    window.open('https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/contents/prevent/SDIJKM5401.html?menuSeq=127', '_blank');
}

// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚨 CAREBOOL 긴급 재난 알림이 수신되었습니다.');
    
    document.querySelector('.btn-primary').focus();

    updateTimestamp();
    setInterval(updateTimestamp, 60000);

    if (navigator.vibrate) {
        navigator.vibrate([200, 100, 200, 100, 200]);
    }
});

// 실시간 시간 업데이트
function updateTimestamp() {
    const now = new Date();
    const timeString = now.toLocaleString('ko-KR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    
    const timeElement = document.querySelector('.detail-value');
    if (timeElement && timeElement.textContent.includes('2025년')) {
        timeElement.textContent = timeString;
    }
}

// 연락처 항목 호버 효과
document.querySelectorAll('.contact-item').forEach(item => {
    item.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-2px) scale(1.02)';
    });
    
    item.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});