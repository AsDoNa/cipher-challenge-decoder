document.getElementById("settings-button").addEventListener("click", function() {
    var submenu = document.getElementById("settings-section");
    var settings_button = document.getElementById("settings-button");
    if (settings_button.classList.contains("submenu-closed")) {
        settings_button.classList.remove("submenu-closed");
        settings_button.classList.add("submenu-opened");
        submenu.style.opacity = 1;
    } else {
        settings_button.classList.remove("submenu-opened");
        settings_button.classList.add("submenu-closed");
        submenu.style.opacity = 0;
    }
});