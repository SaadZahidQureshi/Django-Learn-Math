MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      processEscapes: true
    },
    CommonHTML: { linebreaks: { automatic: true } },
    "HTML-CSS": { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });

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
    console.log(mathInputValue)
    var outputElement = document.getElementById('inputquestiontextarea');
    console.log(outputElement)
    // Clear previous output
    outputElement.innerHTML = '';

    // Create a new span element for rendering
    var newSpan = document.createElement('span');
    newSpan.innerHTML = mathInputValue.replace(/\n/g, '<br/>').replace(/\s/g, '&nbsp;');
    outputElement.textContent = mathInputValue;

    // Append the new span to the output element
    // outputElement.appendChild(newSpan);

    // Use MathJax to typeset the math content
    MathJax.Hub.Typeset(outputElement);
  });