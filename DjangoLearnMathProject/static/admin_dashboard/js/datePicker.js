


document.addEventListener("DOMContentLoaded", function() {
    var datePickerButtons = document.querySelectorAll('.date-picker-button');
    var calendarContainer = document.getElementById('calendar');
    var calendarList = document.getElementById('calendar-list');
    var currentMonthYear = document.getElementById('current-month-year');

    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    var currentMonth = currentDate.getMonth();

    // Map to store selected dates for each button
    var selectedDates = new Map();

    // Function to generate calendar for the given month and year
    function generateCalendar(month, year) {
      calendarList.innerHTML = '';
      var daysInMonth = new Date(year, month + 1, 0).getDate();

      currentMonthYear.textContent = new Date(year, month).toLocaleString('default', { month: 'long', year: 'numeric' });

      for (var day = 1; day <= daysInMonth; day++) {
        var li = document.createElement('li');
        li.textContent = day;

        li.onclick = function(day) {
          
          return function() {
            selectDate(day, month, year);
          };
        
        }(day);
        
        calendarList.appendChild(li);
      }
    }

    // Function to show the calendar
    function showCalendar() {
      calendarContainer.style.display = 'block';
    }

    // Function to hide the calendar
    function hideCalendar() {
      calendarContainer.style.display = 'none';
    }

    // Function to select a date
    function selectDate(day, month, year) {
      if (day < 9){
        // console.log(typeof(day))
        day = '0'+day
      }
      if( month < 9){
        month =''+month
      }
      var targetButton = selectedDates.get('currentButton');
      datePickerButtons.forEach(function(button) {
        if (button.getAttribute('data-target') === targetButton) {
          
          // Clear existing text content of the button
          button.childNodes.forEach(child => {
              if (child.nodeType === Node.TEXT_NODE) {
                  button.removeChild(child);
              }
          });
      
          // Create a text node with the updated date
          const dateTextNode = document.createTextNode(year + '-' + (month + 1) + '-' + day);
      
          // Append the updated text node to the button
          button.appendChild(dateTextNode);
      
          // Update selected dates
          selectedDates.set(targetButton, new Date(year, month, day));
          console.log(dateTextNode);

          const startDateBtn = document.getElementById('startDateBtn');
          const startDate = startDateBtn.textContent.trim()
          
          const endDateBtn = document.getElementById('endDateBtn');
          const endDate = endDateBtn.textContent.trim()

          if(startDate === 'Starting Date' && endDate != null )
          {filter(start=null,end=endDate)
          // console.log('cont-1')
          }
          else if (endDate === 'Ending Date' && startDate != null )
          {filter(start=startDate, end=null) 
            // console.log('cont-2')
          }
          else if(endDate != null && startDate != null){
            // console.log('cont-3')
            filter(start=startDate, end=endDate) 
          }
      }
      });
      hideCalendar();
    }
    // Function to navigate to the previous month
    window.prevMonth = function() {
      currentMonth--;
      if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
      }
      generateCalendar(currentMonth, currentYear);
    };

    // Function to navigate to the next month
    window.nextMonth = function() {
      currentMonth++;
      if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
      }
      generateCalendar(currentMonth, currentYear);
    };

    // Event listeners for button clicks
    datePickerButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        var targetButton = button.getAttribute('data-target');
        selectedDates.set('currentButton', targetButton);
        generateCalendar(currentMonth, currentYear);
        showCalendar();
      });
    });

    // Event listener to close calendar when clicking outside
    document.addEventListener('click', function(event) {
      if (!calendarContainer.contains(event.target) && ![...datePickerButtons].includes(event.target)) {
        hideCalendar();
      }
    });

    // Initialize calendar with the current month and year
    generateCalendar(currentMonth, currentYear);
  });




  // ---------------------------------------------------------

  function filter(start=null, end=null){
    console.log('start date',start,'end date',end)

    const startDateBtn = document.getElementById('startDateBtn');
    const endDateBtn = document.getElementById('endDateBtn');

    const submitForm = () =>{
       const startDate = start
      const endDate = end
      
      const queryParams = new URLSearchParams();
      if (startDate) queryParams.set('start_date', startDate);
      if (endDate) queryParams.set('end_date', endDate);

      const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
      window.location.href = newUrl;
    }
    
    submitForm();
    
    startDateBtn.textContent = start
    endDateBtn.textContent = end

  }


  document.addEventListener('DOMContentLoaded',function(){

    const searchInput = document.getElementById('searchInput');
    const searchForm = document.getElementById('searchForm');
    
    const submitForm = () => {
      const searchQuery = searchInput.value.trim();
      // const startDate = start
      // const endDate = end 

      const queryParams = new URLSearchParams();
      if (searchQuery) queryParams.set('search', searchQuery);
      // if (startDate) queryParams.set('start_date', startDate);
      // if (endDate) queryParams.set('end_date', endDate);

      const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
      window.location.href = newUrl;
    };

    // searchInput.textContent = searchQuery
    searchInput.addEventListener('keyup', function(event) {
      if (event.key === 'Enter') {
        submitForm();
      }
    });

    // startDateBtn.addEventListener('click', submitForm);
    // endDateBtn.addEventListener('click', submitForm);

  })
  // document.addEventListener('DOMContentLoaded', function() {
  //   const searchInput = document.getElementById('searchInput');
  //   const startDateBtn = document.getElementById('startDateBtn');
  //   const endDateBtn = document.getElementById('endDateBtn');
  //   const searchForm = document.getElementById('searchForm');

  //   // Function to submit the form with query parameters
  //   const submitForm = () => {
  //     const searchQuery = searchInput.value.trim();
  //     const startDate = startDateBtn.textContent // assuming you store the selected date in a data attribute
  //     const endDate = endDateBtn.textContent // assuming you store the selected date in a data attribute

  //     console.log(startDate, endDate)

  //     const queryParams = new URLSearchParams();
  //     if (searchQuery) queryParams.set('search', searchQuery);
  //     if (startDate) queryParams.set('start_date', startDate);
  //     if (endDate) queryParams.set('end_date', endDate);

  //     const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
  //     window.location.href = newUrl;
  //   };

  //   // Event listener for key events on the search input
  //   searchInput.addEventListener('keyup', function(event) {
  //     if (event.key === 'Enter') {
  //       submitForm();
  //     }
  //   });


  //   // Event listener for focusout event on date selection buttons
  //   // startDateBtn.addEventListener('focusout', submitForm);
  //   // endDateBtn.addEventListener('focusout', submitForm);
  // });

 