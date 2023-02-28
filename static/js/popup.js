var acc = document.getElementById("accept-button")
var den = document.getElementById("deny-button")

function loadScript(a){
    var b=document.getElementsByTagName("head")[0],c=document.createElement("script");
    c.type="text/javascript",c.src="https://tracker.metricool.com/resources/be.js",c.onreadystatechange=a,c.onload=a,b.appendChild(c)
}

function set_cookie(){
    loadScript(function(){beTracker.t({hash:"22528a9b2f84460fcc104b4da4d2ff66"})});
}

if(has_agreed){
    if(agreement == "1"){
        set_cookie()
    } 
}
if(!has_agreed){
    document.getElementById("cookie-popup").style.display = "block"
}

acc.addEventListener("click", (e)=>{
    document.getElementById("cookie-popup").style.display = "none"
    document.cookie = "agreement=1; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/"
    set_cookie()
})

den.addEventListener("click", (e)=>{
    document.getElementById("cookie-popup").style.display = "none"
    document.cookie = "agreement=0;expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/"
})