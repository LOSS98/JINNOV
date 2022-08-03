console.log('init');
element = document.getElementById('contact-us-button');
element.addEventListener("mouseover",function(){
    console.log('h');
    element.classList.remove("classic");
    element.classList.add("anim");
});
element.addEventListener("mouseout",function(){
    console.log('n');
    element.classList.remove("anim");
    element.classList.add("classic");
});


window.onscroll = function(e) {
    scroll = window.scrollY;
    console.log(scroll);
    if(scroll==0){
        header = document.getElementById('header');
        header.classList.remove('vanish');
    }
    else{
        header = document.getElementById('header');
        header.classList.add('vanish');
    }
}