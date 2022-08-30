button2 = document.getElementById('scroll');
var state = 0;
button2.addEventListener('click', function(){
    var w = window.innerWidth;
    var h = window.innerHeight;
    if(w > 1260){
        window.scroll(0,h*1.12);
    }
    else if(h > 1000 && h > w){
        window.scroll(0,h);
    }
    else if(w < 1260 ||(h < 1000 && h > w)){
        window.scroll(0,h*1.02);
    }
    
});