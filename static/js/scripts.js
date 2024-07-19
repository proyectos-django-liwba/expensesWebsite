
document.addEventListener('DOMContentLoaded', function () {

    let navbarHeight = document.getElementById('navbar').offsetHeight;
    navbarHeight += 2;
    console.log(navbarHeight)
    const sidebar = document.getElementById('sidebar');
    sidebar.style.minHeight = `calc(100vh - ${navbarHeight}px)`;

    console.log(sidebar)

});


