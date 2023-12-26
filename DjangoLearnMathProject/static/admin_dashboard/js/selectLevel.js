document.addEventListener('DOMContentLoaded', function() {
        
    var items = document.getElementsByClassName('list-items');
    var selectedYear = document.getElementById('level');
    var dropdownContent = document.querySelector('.dropdown-content-level');

    var years = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5','Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'];

    years.forEach((year)=>{
        var listitems= document.createElement('li');
        listitems.setAttribute('value', year);
        listitems.classList.add('list-items');
        listitems.textContent = year


        listitems.addEventListener('click', function(){
            var selectedValue = this.getAttribute('value');
            console.log(selectedValue);
            selectedYear.textContent = selectedValue
        })
        dropdownContent.appendChild(listitems);
    })

});
