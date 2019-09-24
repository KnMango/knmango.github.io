<script language="javascript"> //Go to Mobile Page
    // Mobile여부를 구분하기 위함
    var uAgent = navigator.userAgent.toLowerCase(); 

    // 아래는 모바일 장치들의 모바일 페이지 접속을위한 스크립트
    var mobilePhones = new Array('iphone', 'ipod', 'ipad', 'android', 'blackberry', 'windows ce','nokia', 'webos', 'opera mini', 'sonyericsson', 'opera mobi', 'iemobile');
    for (var i = 0; i < mobilePhones.length; i++)
        if (uAgent.indexOf(mobilePhones[i]) != -1)
           document.location = "https://knmango.github.io/wasabi/mobile_wasabi";
</script>