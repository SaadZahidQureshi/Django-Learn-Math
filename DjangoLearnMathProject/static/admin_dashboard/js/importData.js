


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
    $('.dropdown-item').on('click', function () {
      var selectedValue = $(this).text();
      document.getElementById('selectedcategory').value = $(this).data('value')
      $('.dropdown-toggle').text(selectedValue);
    });
  });



document.getElementById('options_btn').addEventListener('click', function(){
    a = document.getElementById('option_a').value
    b = document.getElementById('option_b').value
    c = document.getElementById('option_c').value
    d = document.getElementById('option_d').value
console.log(a,b,c,d)
    document.getElementById('options_a').textContent = a
    document.getElementById('options_b').textContent = b
    document.getElementById('options_c').textContent = c
    document.getElementById('options_d').textContent = d

})