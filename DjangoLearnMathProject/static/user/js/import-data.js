function importData() {
    // Create input element
    let input = document.createElement('input');
    input.type = 'file';

    // Set onchange handler
    input.onchange = () => {
        let files = input.files;

        if (files.length > 0) {
            // Assuming you have an image element with the class 'profile-img'
            let profileImg = document.querySelector('.profile-img');
            // Create a FileReader to read the selected file
            let reader = new FileReader();
            // Set the onload handler to set the selected image to the 'profile-img' element
            reader.onload = function (e) {
                profileImg.src = e.target.result;
            };

            // Read the selected file as a data URL
            reader.readAsDataURL(files[0]);
        }
    };

    // Trigger the file input click
    input.click();
}

function deletePic(){
    let profileImg = document.querySelector('.profile-img');
    // profileImg.src = "./static/user/assets/svg/profile%201-blue.svg";

    fetch('http://127.0.0.1:8000/learnmath/delete_profile_picture/', {
        method: 'POST',
        credentials: 'same-origin',  // Include this line for CSRF protection
    })
    .then(response => response.json())
    .then(data => {
        // Update image source with the default image URL
        // console.log(data.default_image_url)
        profileImg.src = data.default_image_url;
    })
    .catch(error => {
        console.error('Error deleting profile picture:', error);
    });
}

// profileImg.src = '{% static 'user/assets/svg/profile 1-blue.svg'%}';


/* <img class="profile-img rounded-50" src="/static/user/assets/svg/profile%201-blue.svg" alt="profile-img"></img> */
