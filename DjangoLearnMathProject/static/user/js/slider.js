const sliderList = document.getElementById('slider-list');
// console.log('test1')
// Sample data for slider items
// const sliderData = [
//   { text: 'Level 1', name: 'level-1', href: '../question'+'?id=level-1' },
//   { text: 'Level 2', name: 'level-2', href: '../question_with_image'+'?id=level-2' },
//   { text: 'Level 3', name: 'level-3', href: '../question_wrong_answer'+'?id=level-3' },
//   { text: 'Level 4', name: 'level-4', href: '../question'+'?id=level-4' },
//   { text: 'Level 5', name: 'level-5', href: '../question_with_image'+'?id=level-5' },
//   { text: 'Level 6', name: 'level-6', href: '../question_wrong_answer'+'?id=level-6' },
//   { text: 'Level 7', name: 'level-7', href: '../question'+'?id=level-7' },
//   { text: 'Level 8', name: 'level-8', href: '../question_with_image'+'?id=level-8' },
//   { text: 'Level 9', name: 'level-9', href: '../question_wrong_answer'+'?id=level-9' },
//   { text: 'Level 10', name: 'level-10', href: '../question'+'?id=level-10' },
//   { text: 'Level 11', name: 'level-11', href: '../question_with_image'+'?id=level-11' },
//   { text: 'Level 12', name: 'level-12', href: '../question_wrong_answer'+'?id=level-12' },
//   { text: 'Level 13', name: 'level-13', href: '../question'+'?id=level-13' },
//   { text: 'Level 14', name: 'level-14', href: '../question_with_image'+'?id=level-14' },
//   { text: 'Level 15', name: 'level-15', href: '../question_wrong_answer'+'?id=level-15' },
//   { text: 'Level 16', name: 'level-16', href: '../question'+'?id=level-16' },
//   // Add more data as needed
// ];


// Dynamically generate slider items
// function generateSliderItems() {
//   sliderList.innerHTML = ''; // Clear existing items

//   sliderData.forEach((item, index) => {
//       const listItem = document.createElement('a');
//       listItem.className = 'slider-items text-center text-decoration-none';
//       listItem.innerText = item.text;
//       listItem.href = item.href;
//       listItem.dataset.name = item.name;
//       sliderList.appendChild(listItem);
//   });

// }

// generateSliderItems();

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


