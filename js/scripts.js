// Simple JavaScript for interactivity (e.g., smooth scrolling, animations)
document.addEventListener("DOMContentLoaded", function () {
    console.log("Website loaded!");

    // Example: Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth"
            });
        });
    });

    // Toggle Mobile Menu
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.getElementById("navMenu");

    if (hamburger && navMenu) {
        hamburger.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }
});
