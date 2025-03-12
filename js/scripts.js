// Simple JavaScript for interactivity (e.g., smooth scrolling, animations)
document.addEventListener("DOMContentLoaded", function () {
    console.log("Website loaded!");

    // Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Toggle Mobile Menu
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.getElementById("navMenu");

    if (hamburger && navMenu) {
        hamburger.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });

        // Close Menu When Clicking Outside
        document.addEventListener("click", function (e) {
            if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove("active");
            }
        });
    }
});
