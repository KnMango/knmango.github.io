document.addEventListener('DOMContentLoaded', async function() {
  try {
    const response = await fetch('https://knmango.github.io/archive/assets/footer.html');
    const html = await response.text();
    
    // footer 요소를 찾아서 내용을 교체
    const footerElement = document.querySelector('footer');
    if (footerElement) {
      footerElement.outerHTML = html;
    } else {
      // footer 요소가 없는 경우 body 끝 부분에 삽입
      document.body.insertAdjacentHTML('beforeend', html);
    }
  } catch (error) {
    console.error('푸터를 불러오는 중 오류가 발생했습니다:', error);
  }
}); 