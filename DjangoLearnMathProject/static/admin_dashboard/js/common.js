
document.addEventListener("DOMContentLoaded", function() {
  // Function to get query parameters from the URL
  function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
  }

  // Check if the showAlert parameter is present in the URL
  const showAlertParam = getQueryParam("showAlert");
//   console.log(showAlertParam)
  if (showAlertParam === "true") {
    // The showAlert parameter is present, display the alert
    const alertBox = document.querySelector('.alert.alert-success');
    if (alertBox) {
      alertBox.classList.remove('d-none');
    }
  }
});


document.addEventListener("DOMContentLoaded", function() {
  // Function to get query parameters from the URL
  function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    // console.log(urlParams)
    // console.log(urlParams.get(name))
    return urlParams.get(name);
  }

  // Check if the showAlert parameter is present in the URL for update category
  const showAlertUpdateParam = getQueryParam("updateAlert");

  if (showAlertUpdateParam === "true") {
    // The showAlert parameter is present for update category, display the update alert
    const updateAlertBox = document.querySelector('.alert.alert-success-update');
    if (updateAlertBox) {
      updateAlertBox.classList.remove('d-none');
      setTimeout(function() {
        updateAlertBox.classList.add('d-none');
      }, 5000);
    }
  }

  // Check if the addAlert parameter is present in the URL for add category
  const showAlertAddParam = getQueryParam("addAlert");

  if (showAlertAddParam === "true") {
    // The addAlert parameter is present for add category, display the add alert
    const addAlertBox = document.querySelector('.alert.alert-success-add');
    if (addAlertBox) {
      addAlertBox.classList.remove('d-none');
      setTimeout(function() {
        addAlertBox.classList.add('d-none');
      }, 5000);
    }
  }


  // Check if the addAlert parameter is present in the URL for add category
  const showAlertAddLevelParam = getQueryParam("addlevelAlert");
  if (showAlertAddLevelParam === "true") {
  console.log(document.querySelector('.alert.alert-success-add-level'))

    // The addAlert parameter is present for add category, display the add alert
    const addAlertBox = document.querySelector('.alert.alert-success-add-level');
    console.log(showAlertAddLevelParam)
    if (addAlertBox) {
      addAlertBox.classList.remove('d-none');
      setTimeout(function() {
        addAlertBox.classList.add('d-none');
      }, 5000);
    }
  }
  
  // Check if the addAlert parameter is present in the URL for add category
  const showAlertUpdateLevelParam = getQueryParam("updatelevelAlert");
  if (showAlertUpdateLevelParam === "true") {
  console.log(document.querySelector('.alert.alert-success-add-level'))

    // The addAlert parameter is present for add category, display the add alert
    const addAlertBox = document.querySelector('.alert.alert-success-update-level');
    console.log(showAlertUpdateLevelParam)
    if (addAlertBox) {
      addAlertBox.classList.remove('d-none');
      setTimeout(function() {
        addAlertBox.classList.add('d-none');
      }, 5000);
    }
  }

    // Check if the addAlert parameter is present in the URL for add category
    const showAlertAddQuestionParam = getQueryParam("questionAddedAlert");
    if (showAlertAddQuestionParam === "true") {
    console.log(document.querySelector('.alert.alert-success-add-question'))
  
      // The addAlert parameter is present for add category, display the add alert
      const addAlertBox = document.querySelector('.alert.alert-success-add-question');
      console.log(showAlertAddQuestionParam)
      if (addAlertBox) {
        addAlertBox.classList.remove('d-none');
        setTimeout(function() {
          addAlertBox.classList.add('d-none');
        }, 5000);
      }
    }


      // Check if the addAlert parameter is present in the URL for add category
      const showAlertUpdateQuestionParam = getQueryParam("questionUpdateAlert");
      if (showAlertUpdateQuestionParam === "true") {
      console.log(document.querySelector('.alert.alert-success-update-question'))
    
        // The addAlert parameter is present for add category, display the add alert
        const addAlertBox = document.querySelector('.alert.alert-success-update-question');
        console.log(showAlertUpdateQuestionParam)
        if (addAlertBox) {
          addAlertBox.classList.remove('d-none');
          setTimeout(function() {
            addAlertBox.classList.add('d-none');
          }, 5000);
        }
      }

});





