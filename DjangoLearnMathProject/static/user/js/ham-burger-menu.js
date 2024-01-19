
function showMenu(){
  document.querySelector('.container-fluid > nav').classList.toggle('nav-sm-d-none');
  document.querySelector('.container-fluid > nav').classList.remove('shadow-sm');


  $(document.getElementsByClassName('round-slider')).roundSlider({
    sliderType: "min-range",
    value: 90,
    width: 4,
    radius: 15,
    showTooltip: true,
    editableTooltip: false,
    svgMode: true,
    pathColor: "#eee",
    borderWidth: 0,
    startValue: 0,
    rangeColor: '#5AA139',
    tooltipColor: 'black',
    startAngle: 270,    
})


  return false;
}

// ham_burger_menu = document.querySelector('.ham-burger-menu')
// navbar = document.querySelector('.navbar')
// Function to toggle the menu
// function showMenu() {
//   const nav = document.querySelector('.container-fluid > nav');
//   nav.classList.toggle('nav-sm-d-none');
//   nav.classList.remove('shadow-sm');

//   // Your roundSlider initialization code...

//   return false;
// }

// Event listener to close the menu when clicking outside the navbar
// document.body.addEventListener('click', function (event) {
//   const nav = document.querySelector('.container-fluid > nav');
//   const navMenu = document.querySelector('.navbar');

//   // Check if the clicked element is not part of the navbar or its children
//   if (!navMenu.contains(event.target) && nav.classList.contains('nav-sm-d-none') === false) {
//     nav.classList.add('nav-sm-d-none');
//     nav.classList.remove('shadow-sm');
//   }
// });

// // Event listener to prevent the menu from closing when clicking inside the navbar
// document.querySelector('.navbar').addEventListener('click', function (event) {
//   event.stopPropagation();
// });

// // Event listener for the hamburger menu button
// document.querySelector('.navbar-toggler').addEventListener('click', showMenu);

