function showYoutube(){
    document.getElementById('video-container').classList.remove('d-none');
}

function showError(){
  document.getElementById('video-container').classList.remove('d-none');
  document.getElementById('wrong-message-box').classList.remove('d-none')
  document.getElementById('wrong-answer').classList.add('option-selected-wrong')
  // document.getElementsByClassName('justify-center-sm')
}