function toggleDarkMode() {
    document.body.classList.toggle('dark-mode'); /*cualquier tag que contenga este la cambia*/

    var navLinks = document.querySelectorAll('.nav-link'); /*hace los cambios del navlink cuando contenga dark-mode clase a un texto blanco de lo contrario lo convierte en negro*/
    for (var i = 0 ; i < navLinks.length; i++) {
        if (document.body.classList.contains('dark-mode')) {
            navLinks[i].classList.remove('text-dark');
            navLinks[i].classList.add('text-white');
        } else {
            navLinks[i].classList.remove('text-white');
            navLinks[i].classList.add('text-dark');
        }
    }
}