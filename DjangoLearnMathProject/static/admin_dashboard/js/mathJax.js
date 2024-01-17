MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      processEscapes: true
    },
    CommonHTML: { linebreaks: { automatic: true } },
    "HTML-CSS": { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });


  document.getElementById('inputquestion').addEventListener('input', function() {
    var mathInputValue = this.value;
    var outputElement = document.getElementById('inputquestiontextarea');
ng
    var newSpan = document.createElement('span');
    newSpan.innerHTML = mathInputValue.replace(/\n/g, '<br/>').replace(/\s/g, '&nbsp;');

    MathJax.Hub.Typeset(outputElement);
  });

