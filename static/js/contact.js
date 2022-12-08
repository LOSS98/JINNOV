for (const element of document.getElementsByClassName("rounded-button")) {
  element.addEventListener("mouseover", function () {
    element.classList.remove("classic");
    element.classList.add("anim");
  });
  element.addEventListener("mouseout", function () {
    element.classList.remove("anim");
    element.classList.add("classic");
  });
}