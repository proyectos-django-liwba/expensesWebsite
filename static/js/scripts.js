document.addEventListener('DOMContentLoaded', function () {

    // Sidebar height adjustment
    if (document.getElementById('navbar') && document.getElementById('sidebar')) {
        let navbarHeight = document.getElementById('navbar').offsetHeight;
        navbarHeight += 2;
        //console.log(navbarHeight)
        const sidebar = document.getElementById('sidebar');
        sidebar.style.minHeight = `calc(100vh - ${navbarHeight}px)`;

        //console.log(sidebar)
    }

    // Update current year dynamically in footer and form auth
    if (document.getElementById('currentYear')) {
        document.getElementById('currentYear').textContent = new Date().getFullYear();
    }

});

$(document).ready(function () {
    $('.show-password').click(function () {
        const passwordField = $(this).siblings('.password-input');
        const type = passwordField.attr('type') === 'password' ? 'text' : 'password';
        passwordField.attr('type', type);
    });
});


