
// question page timer

function updateCounter() {
  var startTime = new Date().getTime();

  function update() {
      var currentTime = new Date().getTime();
      var elapsedTime = currentTime - startTime;

      // Convert milliseconds to seconds
      var seconds = Math.floor(elapsedTime / 1000);

      var hour = Math.floor(seconds/3600);
      var minut = Math.floor((seconds % 3600) / 60);
      var second = Math.floor(seconds % 60);

      // Display the time counter in the specified container
      var counterContainer = document.getElementById("time-counter-container");
      document.getElementById('hour').innerText = hour;
      document.getElementById('minut').innerText = minut;
      // document.getElementById('second').innerText = second;

      if(second <10){
        document.getElementById('second').innerText = `0${second}`;
      }
      else{
      document.getElementById('second').innerText = second;

      }
      if(minut <10){
        document.getElementById('minut').innerText = `0${minut}`;
      }
      else{
      document.getElementById('minut').innerText = minut;

      }
      if(hour <10){
        document.getElementById('hour').innerText = `0${hour}`;
      }
      else{
      document.getElementById('hour').innerText = hour;

      }

      // counterContainer.innerHTML = "Time elapsed: " + seconds + " seconds";
  }

  // Update the counter every second
  setInterval(update, 1000);
}

// Start the counter when the page is fully loaded
window.onload = function () {
  updateCounter();
};