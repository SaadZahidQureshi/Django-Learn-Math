function showYoutube(){
    document.getElementById('video-container').classList.remove('d-none');
}

function showError(){
  document.getElementById('video-container').classList.remove('d-none');
  document.getElementById('wrong-message-box').classList.remove('d-none')
  document.getElementById('wrong-answer').classList.add('option-selected-wrong')
  // document.getElementsByClassName('justify-center-sm')
}


var resendBtn = document.getElementById('resendLink');
        // Function to add "disabled" class to the anchor tag and start the countdown
  function disableLinkAndStartCountdown(countdownTime) {
    var resendLink = document.getElementById('resendLink');
    resendLink.classList.add('disabled');

    // Update the link text with the countdown
    function updateCountdown() {
        resendLink.innerHTML = 'Resend OTP in ' + countdownTime + ' seconds';
        countdownTime--;

        // If the countdown reaches 0, remove the "disabled" class
        if (countdownTime < 0) {
            resendLink.classList.remove('disabled');
            resendLink.innerHTML = 'Resend OTP';              
            
        } else {
            // Call the function recursively after 1 second
            setTimeout(updateCountdown, 1000);
        }
    }

    // Start the countdown
    updateCountdown();
}

// Function to simulate the OTP resend process (replace this with your actual resend logic)
function resendOTP() {
    // Simulate the OTP resend process, replace this with your actual logic
    // For example, you can make an API call to resend the OTP here
    // ...

    email = document.getElementById('varification_email').value
    console.log(email)

    getNewOTP(email)
  // resendOTP(email)



    // Get the last saved timestamp from localStorage
    var savedTimestamp = localStorage.getItem('timestamp');
    print('save time stamp',savedTimestamp)
    // Calculate the time difference between now and the saved timestamp
    var currentTime = new Date().getTime();
    var elapsedTime = savedTimestamp ? Math.floor((currentTime - parseInt(savedTimestamp)) / 1000) : 0;

    // Set the initial countdown time (180 seconds) minus the elapsed time
    var countdownTime = 20 - elapsedTime;

    // Save the current timestamp to localStorage
    localStorage.setItem('timestamp', currentTime);

    // After successfully resending, disable the link and start the countdown
    disableLinkAndStartCountdown(countdownTime);
}

// Initially check if there is a countdown time in localStorage and start the countdown
var storedCountdownTime = localStorage.getItem('timestamp');
if (storedCountdownTime !== null) {
    var currentTime = new Date().getTime();
    var elapsedTime = Math.floor((currentTime - parseInt(storedCountdownTime)) / 1000);
    var remainingCountdownTime = 20 - elapsedTime;

    // Check if the remaining countdown time is greater than 0
    if (remainingCountdownTime > 0) {
        disableLinkAndStartCountdown(remainingCountdownTime);
    } else {
        localStorage.removeItem('timestamp'); // Remove expired timestamp
    }
}



function getNewOTP(email) {
  // Send email to Django view using AJAX
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'resendOTP/', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = function () {
      var response = JSON.parse(xhr.responseText);
      alert(response.message);
  };
  xhr.send('email=' + email);
}