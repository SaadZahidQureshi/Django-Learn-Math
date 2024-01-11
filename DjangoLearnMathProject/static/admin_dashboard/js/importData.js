// function importData() {
//     // Create input element
//     let input = document.createElement('input');
//     input.type = 'file';

//     // console.log(document.querySelector('.upload-img-text'))

//     // Set onchange handler
//     input.onchange = () => {
//         let files = input.files;

//         if (files.length > 0) {
//             // Assuming you have an image element with the class 'profile-img'
//             let categoryImg = document.querySelector('#selected_background_img');
//             // document.querySelector('.upload-category-img-container').classList.add('d-none')
//             // document.querySelector('.upload-img-text').classList.add('d-none')
//             // categoryImg.classList.remove('d-none')
//             // Create a FileReader to read the selected file
//             let reader = new FileReader();
//             // Set the onload handler to set the selected image to the 'profile-img' element
//             reader.onload = function (e) {
//                 categoryImg.style.backgroundImage = 'url(' + e.target.result + ')';
//                 categoryImg.style.backgroundRepeat = 'no-repeat';
//                 categoryImg.style.backgroundSize = 'cover';
//                 categoryImg.style.backgroundPosition = 'center';
//                 // categoryImg.style.background-i = e.target.result;
//             };

//             // Read the selected file as a data URL
//             reader.readAsDataURL(files[0]);
//         }
//     };

//     // Trigger the file input click
//     input.click();
// }


// var selectedImageUrl = ""; // Variable to store the selected image URL

// function displayImage(input) {
//     var file = input.files[0];

//     if (file) {
//         var objectUrl = URL.createObjectURL(file);
//         document.getElementById('selectedImage').src = objectUrl;
//         selectedImageUrl = objectUrl; // Store the URL in the variable
//     }
// }



function importData(){
    console.log('came herr-----------')
    document.getElementById('fileInput').click();
}
function displayImage(input) {
    var file = input.files[0];

    if (file) {
        var objectUrl = URL.createObjectURL(file);
        let categoryImg = document.querySelector('#img_category');

        
        if(categoryImg != null){
            categoryImg.src = ''

        }
        // document.getElementById('selectedImage').src = objectUrl;
        console.log('came herr too-----------')

        let background_categoryImg = document.querySelector('#selected_background_img');
        background_categoryImg.style.backgroundImage = 'url(' + objectUrl + ')';
        background_categoryImg.style.backgroundRepeat = 'no-repeat';
        background_categoryImg.style.backgroundSize = 'cover';
        background_categoryImg.style.backgroundPosition = 'center';
    }
}

$(document).ready(function () {
    // Add click event listener to category dropdown items
    $('.dropdown-item').on('click', function () {

      //console.log($('.dropdown-item'))
      var selectedValue = $(this).data('value');
      $('.dropdown-toggle').text(selectedValue);
      $('#selectedcategory').val(selectedValue)
      console.log($('#selectedcategory').val)
    });

  });

