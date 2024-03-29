// Comportamento da sidebar
let btn__menu = document.getElementById('btn_menu');

if (sidebar.classList.contains('sidebar_active')) {
    document.getElementById('content__page').style.marginLeft = "300px";
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('sidebar_active');
    if (sidebar.classList.contains('sidebar_active')) {
        document.getElementById('content__page').style.marginLeft = "300px";
    } else {
        document.getElementById('content__page').style.marginLeft = "0";
    }
}

btn__menu.addEventListener('click', toggleSidebar);


/* color link sidebar - background active */
const listLinks = document.querySelectorAll('.links__sidebar');

function linkActive() {
    listLinks.forEach((link) => {
        link.classList.remove('active');
    })

    this.classList.add('active');
}

listLinks.forEach((elemento) => {
    elemento.addEventListener('click', setInterval(linkActive, 2000))
})