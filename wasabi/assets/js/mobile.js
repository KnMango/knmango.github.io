<script language="javascript"> //Go to Mobile Page
    // Mobile���θ� �����ϱ� ����
    var uAgent = navigator.userAgent.toLowerCase(); 

    // �Ʒ��� ����� ��ġ���� ����� ������ ���������� ��ũ��Ʈ
    var mobilePhones = new Array('iphone', 'ipod', 'ipad', 'android', 'blackberry', 'windows ce','nokia', 'webos', 'opera mini', 'sonyericsson', 'opera mobi', 'iemobile');
    for (var i = 0; i < mobilePhones.length; i++)
        if (uAgent.indexOf(mobilePhones[i]) != -1)
           document.location = "https://knmango.github.io/wasabi/mobile_wasabi";
</script>