const sliderList = document.getElementById('slider-list');
const sliderItems = document.querySelectorAll('.slider-items');
const totalItems = sliderItems.length;
let currentIndex = 0;
let itemsDisplayed = calculateItemsDisplayed();
const itemWidth = sliderItems[0].offsetWidth;

function calculateItemsDisplayed() {
  // Adjust this function based on your desired logic for different viewport widths
  return window.innerWidth < 768 ? 4 : 10; // Example: 4 items on mobile, 10 items on desktop
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % totalItems; //first time it (0+1)%16 = 1
  if ( currentIndex == sliderItems.length+1 - itemsDisplayed ){
    currentIndex =0;
  }
  updateSlider();

}

function prevSlide() {
  currentIndex = (currentIndex - 1 + totalItems) % totalItems; // (0-1+16) = 15%16 = 15
  if (currentIndex == 15) {
    currentIndex = sliderItems.length-itemsDisplayed;
  }
  updateSlider();
}

function updateSlider() {

    const newPosition = -currentIndex * itemWidth;//
    sliderList.style.transform = `translateX(${newPosition}px)`;
    
}


window.addEventListener('load', function() {

  const urlParams = new URLSearchParams(window.location.search);
  level = urlParams.get('level')

  if (level == null){
    level_no = document.querySelector('.level_no').textContent
    level =level_no
  }
  let selectedIndex = -1
  const items = document.querySelectorAll('.slider-items');
  // console.log(typeof(items))
  items.forEach((item,index) =>{
    if(item.getAttribute('data-name') == level){
      selectedIndex = index
      currentIndex = selectedIndex
      updateSlider()
      
      items.forEach(item =>{
        item.classList.remove('slider-active')
      })
      item.classList.add('slider-active')
    }
  })

})


