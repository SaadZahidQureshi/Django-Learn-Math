    var options = document.querySelectorAll('.options');
    var selectedoption = false
    question_id = document.querySelector('.question-id').textContent
    category_id = document.querySelector('.category-id').textContent
    level_no = document.querySelector('.level_no').textContent
    baseurl = document.querySelector('.baseurl').textContent
    stored_option = document.querySelector('.stored_option').textContent

    modal_btn = document.querySelector('.modal-button')
    options.forEach(function(option) {
      option.addEventListener("click", function() {
        if (!selectedoption){
          selectedoption = true
          var selected_option = this.getAttribute("data-value");
          options.forEach(function(option) {
            option.classList.remove('option-selected');
            option.classList.remove('option-selected-wrong');
          });
          if (selected_option == stored_option) {
            this.classList.add('option-selected');
            var myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
            myModal.show();

            hour = document.querySelector('#hour').textContent
            minut = document.querySelector('#minut').textContent
            second = document.querySelector('#second').textContent
            console.log(hour, minut, second)
            time = hour+':'+minut+':'+second
            modal_btn.href = baseurl+'?level='+level_no+'&selected_option='+selected_option+'&qsid='+question_id+'&category_id='+category_id+'&time='+time
          } else {
            this.classList.add('option-selected-wrong');
            showError();

            hour = document.querySelector('#hour').textContent
            minut = document.querySelector('#minut').textContent
            second = document.querySelector('#second').textContent
            time = hour+':'+minut+':'+second
            checkAnswer(category_id ,level_no, selected_option, question_id, time)
          }
        }
      });
    });


     
    function checkAnswer(category_id ,level_no, selected_option, qsid, time) {
        $.ajax({
          type: "GET",
          url: baseurl+'?level='+level_no+'&selected_option='+selected_option+'&qsid='+question_id+'&category_id='+category_id+'&time='+time,
          data: {
              "category_id": category_id,
              "level_no": level_no,
              "selected_option": selected_option,
              "qsid": qsid,
              'time': time
          },
          dataType: "json",
    
          success: function (data) {
    
            if (data.error){
                alert('Error')
            }else{
              console.log('response ', data)
            }
            
          }
          
      });
      }