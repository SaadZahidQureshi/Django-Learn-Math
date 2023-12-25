document.addEventListener('DOMContentLoaded', function() {
        
    var items = document.getElementsByClassName('list-items');
    var selectedYear = document.getElementById('year');
    var dropdownContent = document.querySelector('.dropdown-content');

    var years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019' ,'2020', '2021', '2022', '2023'];

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
