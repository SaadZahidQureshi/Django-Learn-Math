

document.addEventListener('DOMContentLoaded', function() {
    function handleItemClick(items, showElement, inputElement) {
        items.forEach((item) => {
            item.addEventListener('click', function() {
                var selectedValue = this.getAttribute('data-value');
                
                // Check if the clicked item belongs to the 'levels' class
                if (this.classList.contains('levels')) {
                    levelselected.textContent = selectedValue;
                    levelinput.value = selectedValue;
                } else {
                    showElement.textContent = selectedValue;
                    inputElement.value = selectedValue;
                }
                
                searchForm.submit();
            });
        });
    }

    var levelItems = document.querySelectorAll('.list-items.levels');
    levelselected = document.getElementById('levelselected');
    levelinput = document.getElementById('levelinput');
    searchForm = document.getElementById('searchForm');

    handleItemClick(levelItems, levelselected, levelinput);

    var categoryItems = document.querySelectorAll('.list-items');
    showcategory = document.getElementById('categoryselected');
    categoryinput = document.getElementById('categoryinput');

    handleItemClick(categoryItems, showcategory, categoryinput);
});
