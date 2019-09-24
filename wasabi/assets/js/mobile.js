var filter = "win16|win32|win64|mac|macintel";
if( navigator.platform  ){
        if( filter.indexOf(navigator.platform.toLowerCase())<0 ){
             location.href = "https://knmango.github.io/wasabi/main_mobile";
        }
 }