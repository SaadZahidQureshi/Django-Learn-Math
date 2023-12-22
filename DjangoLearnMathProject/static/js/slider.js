const sliderList = document.getElementById('slider-list');
// console.log('test1')
// Sample data for slider items
const sliderData = [
  { text: 'Level 1', name: 'level-1', href: '../html/question.html'+'?id=level-1' },
  { text: 'Level 2', name: 'level-2', href: '../html/Question-with-image.html'+'?id=level-2' },
  { text: 'Level 3', name: 'level-3', href: '../html/Question-wrong-ans.html'+'?id=level-3' },
  { text: 'Level 4', name: 'level-4', href: '../html/question.html'+'?id=level-4' },
  { text: 'Level 5', name: 'level-5', href: '../html/Question-with-image.html'+'?id=level-5' },
  { text: 'Level 6', name: 'level-6', href: '../html/Question-wrong-ans.html'+'?id=level-6' },
  { text: 'Level 7', name: 'level-7', href: '../html/question.html'+'?id=level-7' },
  { text: 'Level 8', name: 'level-8', href: '../html/Question-with-image.html'+'?id=level-8' },
  { text: 'Level 9', name: 'level-9', href: '../html/Question-wrong-ans.html'+'?id=level-9' },
  { text: 'Level 10', name: 'level-10', href: '../html/question.html'+'?id=level-10' },
  { text: 'Level 11', name: 'level-11', href: '../html/Question-with-image.html'+'?id=level-11' },
  { text: 'Level 12', name: 'level-12', href: '../html/Question-wrong-ans.html'+'?id=level-12' },
  { text: 'Level 13', name: 'level-13', href: '../html/question.html'+'?id=level-13' },
  { text: 'Level 14', name: 'level-14', href: '../html/Question-with-image.html'+'?id=level-14' },
  { text: 'Level 15', name: 'level-15', href: '../html/Question-wrong-ans.html'+'?id=level-15' },
  { text: 'Level 16', name: 'level-16', href: '../html/question.html'+'?id=level-16' },
  // Add more data as needed
];

// window.addEventListener('load', function(){
//   sliderList.innerHTML = ''; // Clear existing items

//   sliderData.forEach((item, index) => {
//       const listItem = document.createElement('a');
//       listItem.className = 'slider-items text-center text-decoration-none';
//       listItem.innerText = item.text;
//       listItem.href = item.href;
//       listItem.dataset.name = item.name;

//       sliderList.appendChild(listItem);
//   });
// })
// Dynamically generate slider items
function generateSliderItems() {
  sliderList.innerHTML = ''; // Clear existing items

  sliderData.forEach((item, index) => {
      const listItem = document.createElement('a');
      listItem.className = 'slider-items text-center text-decoration-none';
      listItem.innerText = item.text;
      listItem.href = item.href;
      listItem.dataset.name = item.name;

      sliderList.appendChild(listItem);
  });

}

generateSliderItems();

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

  // if(this.window.innerWidth < 768 && currentIndex <= 12){
  //   const newPosition = -currentIndex * itemWidth;//
  //   sliderList.style.transform = `translateX(${newPosition}px)`;
  // }
  // if(this.window.innerHeight > 768 && currentIndex <=7){
  //   const newPosition = -currentIndex * itemWidth;//
  //   sliderList.style.transform = `translateX(${newPosition}px)`;
  // }

    const newPosition = -currentIndex * itemWidth;//
    sliderList.style.transform = `translateX(${newPosition}px)`;
    
}


window.addEventListener('load', function() {

  const url = window.location.href.split('?');
  const id = url[url.length-1].split('=')
  let uni_id =id[id.length-1]

  if(uni_id[uni_id.length-1] == '#'){
    uni_id = uni_id.slice(0,-1)
  }
  let selectedIndex = -1
  const items = document.querySelectorAll('.slider-items');
  // console.log(typeof(items))
  items.forEach((item,index) =>{
    if(item.getAttribute('data-name') == uni_id){
      selectedIndex = index
      currentIndex = selectedIndex
      console.log(selectedIndex)
      // if (currentIndex <= 7) {
      //   currentIndex = sliderItems.length-itemsDisplayed;
      // }
      updateSlider()
      
      items.forEach(item =>{
        item.classList.remove('slider-active')
      })
      item.classList.add('slider-active')
    }
  })

})


