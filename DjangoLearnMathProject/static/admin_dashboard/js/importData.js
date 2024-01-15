


function importData(){
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
      var selectedValue = $(this).text();
      console.log($(this).text())
      document.getElementById('selectedcategory').value = $(this).data('value')
      $('.dropdown-toggle').text(selectedValue);
    //   $('#selectedcategory').val(selectedValue)
    });

  });

