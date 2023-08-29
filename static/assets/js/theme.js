function setCookie(name, value) {
    document.cookie = `${name}=${value};path=/`;
}

function toggleTheme() {
    
    const currentTheme = document.querySelector("link[href*='theme']").getAttribute("href");
    const newTheme = currentTheme.includes("light") ? "dark" : "light";
    
    // Set the theme preference as a cookie before changing the theme
    setCookie("theme", newTheme);

    // Change the theme by updating the CSS link
    const themeLink = document.querySelector("link[href*='theme']");
    themeLink.setAttribute("href", `/static/assets/sass/${newTheme}_theme.css`);
}
