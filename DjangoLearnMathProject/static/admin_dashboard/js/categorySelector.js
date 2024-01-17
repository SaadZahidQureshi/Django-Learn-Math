document.addEventListener('DOMContentLoaded', function() {
    var items = document.querySelectorAll('.list-items');
    showcategory = document.getElementById('categoryselected')
    categoryinput = document.getElementById('categoryinput')
    searchForm = document.getElementById('searchForm')

    items.forEach((item)=>{

        item.addEventListener('click', function(){
            var selectedValue = this.getAttribute('data-value');
            console.log(selectedValue);
            showcategory.textContent = selectedValue
            categoryinput.value = selectedValue
            searchForm.submit()
        })
    })

});
