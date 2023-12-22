
function showMenu(){
  document.querySelector('.container-fluid > nav').classList.toggle('nav-sm-d-none');
  document.querySelector('.container-fluid > nav').classList.remove('shadow-sm');
  $(document.getElementsByClassName('round-slider')).roundSlider({
    sliderType: "min-range",
    value: 90,
    width: 4,
    radius: 15,
    showTooltip: true,
    editableTooltip: false,
    svgMode: true,
    pathColor: "#eee",
    borderWidth: 0,
    startValue: 0,
    rangeColor: '#5AA139',
    tooltipColor: 'black',
    startAngle: 270,    
})


  return false;
}