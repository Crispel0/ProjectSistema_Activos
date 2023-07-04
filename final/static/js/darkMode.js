function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');

    var navLinks = document.querySelectorAll('.nav-link');
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