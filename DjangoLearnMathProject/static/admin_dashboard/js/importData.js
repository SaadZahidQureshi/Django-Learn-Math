function importData() {
    // Create input element
    let input = document.createElement('input');
    input.type = 'file';

    // console.log(document.querySelector('.upload-img-text'))

    // Set onchange handler
    input.onchange = () => {
        let files = input.files;

        if (files.length > 0) {
            // Assuming you have an image element with the class 'profile-img'
            let categoryImg = document.querySelector('.category-img');
            document.querySelector('.upload-category-img-container').classList.add('d-none')
            document.querySelector('.upload-img-text').classList.add('d-none')
            categoryImg.classList.remove('d-none')
            // Create a FileReader to read the selected file
            let reader = new FileReader();
            // Set the onload handler to set the selected image to the 'profile-img' element
            reader.onload = function (e) {
                categoryImg.src = e.target.result;
            };

            // Read the selected file as a data URL
            reader.readAsDataURL(files[0]);
        }
    };

    // Trigger the file input click
    input.click();
}
