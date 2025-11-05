// typing.js - Terminal typing animation
document.addEventListener("DOMContentLoaded", function() {
    const typedElements = document.querySelectorAll(".typed-text");
    
    typedElements.forEach(el => {
        const text = el.textContent;
        el.textContent = "";
        let i = 0;
        
        const interval = setInterval(() => {
            if (i < text.length) {
                el.textContent += text[i];
                i++;
            } else {
                clearInterval(interval);
            }
        }, 15); // typing speed in milliseconds
    });
});
