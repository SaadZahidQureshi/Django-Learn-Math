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
    profileImg.src = '../assets/svg/profile 1-blue.svg';
}