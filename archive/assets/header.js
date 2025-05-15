document.addEventListener('DOMContentLoaded', async function() {
  try {
    const response = await fetch('https://knmango.github.io/archive/assets/header.html');
    const html = await response.text();
    
    // header 요소를 찾아서 내용을 교체
    const headerElement = document.querySelector('header');
    if (headerElement) {
      headerElement.outerHTML = html;
    } else {
      // header 요소가 없는 경우 body 시작 부분에 삽입
      document.body.insertAdjacentHTML('afterbegin', html);
    }

    // 드롭다운 메뉴 기능 추가
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
      const button = dropdown.querySelector('button');
      const menu = dropdown.querySelector('.dropdown-menu');
      
      if (button && menu) {
        button.addEventListener('click', () => {
          menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
        });

        // 다른 드롭다운 메뉴 클릭 시 현재 메뉴 닫기
        document.addEventListener('click', (e) => {
          if (!dropdown.contains(e.target)) {
            menu.style.display = 'none';
          }
        });
      }
    });
  } catch (error) {
    console.error('헤더를 불러오는 중 오류가 발생했습니다:', error);
  }
}); 