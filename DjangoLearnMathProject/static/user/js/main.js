function showYoutube(){
    document.getElementById('video-container').classList.remove('d-none');
}

function showError(){
  document.getElementById('video-container').classList.remove('d-none');
  document.getElementById('wrong-message-box').classList.remove('d-none')
  document.getElementById('wrong-answer').classList.add('option-selected-wrong')
  // document.getElementsByClassName('justify-center-sm')
}

// // user email verification modal show

// let otpForm = document.getElementById('otp-form')
// let successModal = document.getElementById('trigermodal');
// let errorAlert = document.querySelector('.alert')
// let inputOpt = document.getElementById('input-otp')
// // console.log(inputOpt)
// otpForm.addEventListener('submit', function (event){
//   event.preventDefault()

//   var formData =new FormData(otpForm);

//   fetch('http://127.0.0.1:8000/auth/codeVerify/', {
//     method: 'POST',
//     body : formData,
//   })
//   .then(response => response.json())
//   .then(data =>{
//     // console.log(data),.
//     if (data.success){
//       successModal.click()
//     }
//     else{
//       errorAlert.classList.remove('d-none')

//     }
//   })
//   .catch(error => console.error(error))
// })
// document.getElementById('ok-modal-button').addEventListener('click', function(){
//   window.location.href= 'http://127.0.0.1:8000/auth/signup/'
// })


email = document.getElementById('varification_email')
timeout = document.getElementById('timeout').textContent
resendbtn = document.getElementById('resendbtn')

console.log(resendbtn)
console.log(email.value)
console





document.addEventListener('DOMContentLoaded', function(){



  function getCurrentDateTime() {
    const currentDate = new Date();
    
    const year = currentDate.getFullYear();
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    const day = currentDate.getDate().toString().padStart(2, '0');
  
    const hours = currentDate.getHours().toString().padStart(2, '0');
    const minutes = currentDate.getMinutes().toString().padStart(2, '0');
    const seconds = currentDate.getSeconds().toString().padStart(2, '0');
    const milliseconds = currentDate.getMilliseconds().toString().padStart(3, '0');
  
    // Generate microseconds separately
    const microseconds = (Math.floor(Math.random() * 1000000)).toString().padStart(6, '0');
  
    const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}.${milliseconds}${microseconds}`;
    
    return formattedDateTime;
  }
  

  console.log('time save in db : ',timeout)
  currentime = getCurrentDateTime();
  console.log('current time ',currentime )
  console.log(currentime > timeout)
  console.log(timeout - currentime)

  if(currentime>= timeout){
    resendbtn.classList.remove('d-none')
  }



  resendbtn.addEventListener('click', function(){
    const data = {
      'eamil': email,
      'expiry': timeout
    }


    fetch('{% url "resendOTP" %}'),{
      method : 'POST',
      headers : {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: JSON.stringify(data)
    }
  })



})
