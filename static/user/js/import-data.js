// function importData() {
//     // Create input element
//     let input = document.createElement('input');
//     input.type = 'file';

//     // Set onchange handler
//     input.onchange = () => {
//         let files = input.files;

//         if (files.length > 0) {
//             // Assuming you have an image element with the class 'profile-img'
//             let profileImg = document.querySelector('.profile-img');
//             // Create a FileReader to read the selected file
//             let reader = new FileReader();
//             // Set the onload handler to set the selected image to the 'profile-img' element
//             reader.onload = function (e) {
//                 // let profileImginput = document.querySelector('#profile_image');
//                 // console.log(profileImginput)
//                 // console.log(e.target.result)
//                 profileImg.src = e.target.result;
//             };

//             // Read the selected file as a data URL
//             reader.readAsDataURL(files[0]);
//         }
//     };

//     // Trigger the file input click
//     input.click();
// }

// function deletePic(){
//     let profileImg = document.querySelector('.profile-img');

//     fetch('http://127.0.0.1:8000/auth/delete_profile_picture/', {
//         method: 'POST',
//         credentials: 'same-origin',  // Include this line for CSRF protection
//     })
//     .then(response => response.json())
//     .then(data => {
//         profileImg.src = data.default_image_url;
//     })
//     .catch(error => {
//         console.error('Error deleting profile picture:', error);
//     });
// }

var selectedImageUrl = ""; // Variable to store the selected image URL

function displayImage(input) {
    var file = input.files[0];

    if (file) {
        var objectUrl = URL.createObjectURL(file);
        document.getElementById('selectedImage').src = objectUrl;
        selectedImageUrl = objectUrl; // Store the URL in the variable
    }
}