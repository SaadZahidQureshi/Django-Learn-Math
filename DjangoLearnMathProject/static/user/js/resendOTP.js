

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


function resendOTP() {
  email = document.getElementById('varification_email').value
  console.log(email)
  getNewOTP(email)

  var currentTime = new Date().getTime();
  localStorage.setItem('timestamp', currentTime);
  var savedTimestamp = localStorage.getItem('timestamp');
  var elapsedTime = savedTimestamp ? Math.floor((currentTime - parseInt(savedTimestamp)) / 1000) : 0;
  var countdownTime = 20 - elapsedTime;
  disableLinkAndStartCountdown(countdownTime);

}


function disableLinkAndStartCountdown(countdownTime) {
    var resendbtn = document.getElementById('resendLink');
    resendbtn.classList.add('disabled');
    function updateCountdown() {
        resendbtn.innerHTML = 'Resend Code in ' + countdownTime + ' seconds';
        countdownTime--;
        if (countdownTime < 0) {
            resendbtn.classList.remove('disabled');
            resendbtn.innerHTML = 'Resend Code';              
            
        } else {
            // Call the function recursively after 1 second
            setTimeout(updateCountdown, 1000);
        }
    }
    updateCountdown();
}


function getNewOTP(email) {
    console.log('opt for this '+email+' is being generated...')
    $.ajax({
      type: "GET",
      url: 'http://127.0.0.1:8000/auth/resendOTP/',
      data: {
          "email": email,
      },
      dataType: "json",

      success: function (data) {

        if (data.error){
            alert('Email cannot be Null')
        }else{
          console.log('OTP sent of this email address '+data.email)
        }
        
      }
      
  });
  }
  