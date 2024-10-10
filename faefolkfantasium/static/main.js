// main.js
console.log("JavaScript file is loaded!");
document.addEventListener("mousemove", function(e) {
    const sparkle = document.createElement("div");
    sparkle.classList.add("sparkle");
    document.body.appendChild(sparkle);

    // Position the sparkle where the cursor is
    sparkle.style.left = `${e.pageX}px`;
    sparkle.style.top = `${e.pageY}px`;

    // Remove the sparkle after animation ends
    setTimeout(() => {
        sparkle.remove();
    }, 1000); // Duration of sparkle animation
});



