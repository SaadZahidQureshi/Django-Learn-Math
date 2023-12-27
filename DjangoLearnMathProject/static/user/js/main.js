function showYoutube(){
    document.getElementById('video-container').classList.remove('d-none');
}

function showError(){
  document.getElementById('video-container').classList.remove('d-none');
  document.getElementById('wrong-message-box').classList.remove('d-none')
  document.getElementById('wrong-answer').classList.add('option-selected-wrong')
  // document.getElementsByClassName('justify-center-sm')
}

// user email verification modal show

let otpForm = document.getElementById('otp-form')
let successModal = document.getElementById('trigermodal');
let errorAlert = document.querySelector('.alert')
let inputOpt = document.getElementById('input-otp')
// console.log(inputOpt)
otpForm.addEventListener('submit', function (event){
  event.preventDefault()

  var formData =new FormData(otpForm);

  fetch('http://127.0.0.1:8000/auth/codeVerify/', {
    method: 'POST',
    body : formData,
  })
  .then(response => response.json())
  .then(data =>{
    // console.log(data),.
    if (data.success){
      successModal.click()
    }
    else{
      errorAlert.classList.remove('d-none')

    }
  })
  .catch(error => console.error(error))
})
document.getElementById('ok-modal-button').addEventListener('click', function(){
  window.location.href= 'http://127.0.0.1:8000/auth/signup/'
})
