button = document.getElementById('menubox');
var state = 0;
button.addEventListener('click', function(){
    element = document.getElementById('navmenu');
    bara = document.getElementById('menua');
    barb = document.getElementById('menub');
    barc = document.getElementById('menuc');
    console.log(state);
    if(state===0){
        element.classList.remove("closed");
        element.classList.add("open");
        bara.classList.add("a");
        barb.classList.add("b");
        barc.classList.add("c");
        state = 1;
    }
    else if(state===1){
        element.classList.remove("open");
        element.classList.add("closed");
        bara.classList.remove("a");
        barb.classList.remove("b");
        barc.classList.remove("c");
        state = 0;
    }
});