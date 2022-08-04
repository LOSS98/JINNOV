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