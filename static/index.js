window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("Navbar").style.background = "rgba(255,255,255,0.1)";
    document.getElementById("Navbar").style.backdropFilter = "blur( 10.5px )";
    document.getElementById("Navbar").style.transition = "0.5s";
  } else {
    document.getElementById("Navbar").style.background = "transparent";
  }
}
