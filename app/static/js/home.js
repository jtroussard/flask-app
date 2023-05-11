document.addEventListener("DOMContentLoaded", function() {
    var fadeImg = document.getElementById("fade-img");
    fadeImg.style.opacity = 0;
  
    // Add the fade-in animation to the image
    fadeImg.style.animation = "fadeIn 1s";
  
    // Set the opacity to 1 after a short delay
    setTimeout(function() {
      fadeImg.style.opacity = 1;
    }, 100);
  });
  