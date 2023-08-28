function setCookie(name, value) {
    document.cookie = `${name}=${value};path=/`;
}

function toggleTheme() {
    const currentTheme = document.querySelector("link[href*='theme']").getAttribute("href");
    const newTheme = currentTheme.includes("light") ? "dark" : "light";
    document.querySelector("link[href*='theme']").setAttribute("href", `/static/assets/sass/${newTheme}_theme.css`);
    
    // Set the theme preference as a cookie
    setCookie("theme", newTheme);
}
