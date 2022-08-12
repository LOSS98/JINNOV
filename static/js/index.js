button2 = document.getElementById('scroll');
var state = 0;
button2.addEventListener('click', function(){
    console.log('zizi');
    var h = window.innerHeight; 
    window.scroll(0,h*1.12);
});