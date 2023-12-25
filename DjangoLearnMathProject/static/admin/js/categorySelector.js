document.addEventListener('DOMContentLoaded', function() {
        
    var items = document.getElementsByClassName('list-items');
    var selectedYear = document.getElementById('category');
    var dropdownContent = document.querySelector('.dropdown-content');

    var years = ['Calculus1', 'Calculus2', 'Trignometery', 'Algebra', 'Geometery','Calculus1', 'Calculus2', 'Trignometery', 'Algebra', 'Geometery'];

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
