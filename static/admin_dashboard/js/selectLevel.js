

document.addEventListener('DOMContentLoaded', function() {
    var items = document.querySelectorAll('.list-items.levels');
    levelselected = document.getElementById('levelselected')
    levelinput = document.getElementById('levelinput')
    searchForm = document.getElementById('searchForm')

    items.forEach((item)=>{

        item.addEventListener('click', function(){
            var selectedValue = this.getAttribute('data-value');
            console.log(selectedValue)
            levelselected.textContent = 'Level '+selectedValue
            levelinput.value = selectedValue
            searchForm.submit()
        })
    })

});

