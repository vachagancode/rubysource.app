window.addEventListener("DOMContentLoaded", () => {
    function Scroller() {
        coursesNavLink = document.getElementById("courses")
        coursesNavLink.addEventListener("click", () => {
            document.documentElement.scrollTop = 1048;
        });
        copyrightNavLink = document.getElementById("copyright")
        copyrightNavLink.addEventListener("click", () => {
            document.documentElement.scrollTop = 2701;
        });
        resourcesNavLink = document.getElementById("resources")
        resourcesNavLink.addEventListener("click", () => {
            document.documentElement.scrollTop = 1801;
        });
    }
    function InformationOnHover() {
        
    }

    function App() {
        Scroller();
    }

    App();
});