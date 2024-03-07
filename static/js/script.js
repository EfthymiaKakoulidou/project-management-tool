function toggleMenu() {
  var navbar = document.querySelector('.navbar');
  var navbarHeight = navbar.offsetHeight;
  var navbarCollapse = document.querySelector('.navbar-collapse');

  if (navbarCollapse.classList.contains('show')) {
    // Hide the menu
    navbarCollapse.classList.remove('show');
    navbar.style.marginBottom = '0';
  } else {
    // Show the menu
    navbarCollapse.classList.add('show');
    navbar.style.marginBottom = navbarHeight;
  }
}