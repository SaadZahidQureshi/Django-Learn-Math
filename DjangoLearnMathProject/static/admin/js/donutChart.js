// const label = ["Wrong Ans", "Correct Ans"];
const values2 = [50, 50];
const color = ["#F14336", "#28B446"];
total = values2.reduce((accumulator, currentValue) => accumulator + currentValue)
label = values2.map(value => Math.round((value / total) * 100) +'%');
label[0]= label[0]+' Wrong Ans'
label[1]= label[1]+' Correct Ans'


// Doughnut chart data
const doughnutData = {
  labels: label,
  datasets: [
    {
      // label: label,
      data: values2,
      backgroundColor: color,
    },
],
};


//show text in center of doughnut chart
const textCenter ={
  id: 'textCenter',
  afterDatasetsDraw(chart, args, plugins){
    const {ctx, data, chartArea :{top, bottom, left, right, width, height}, scales:{x,y}}=chart;
    ctx.save();
    ctx.font= 'bold 20px';
    ctx.Color = 'red'
    text = '100%'
    // ctx.top = 50
    ctx.fillText(text, chart.getDatasetMeta(0).data[0].x-20, chart.getDatasetMeta(0).data[0].y)
  }
}

const doughnutConfig = {
  type: 'doughnut',
  data : doughnutData,
  options: {
    // cutoutPercentage: 40,
    maintainAspectRatio: false,
    plugins:{
      layout:{
        padding:{
          top:50
        }
      },
      legend:{
        display:true,
        reverse: true,
        position: 'bottom',
        

        labels:{
        }
      }
    },
    // plugins: [textCenter]
  },
};




const myDoughnutChart = new Chart(
  document.getElementById("myDonutChart"),
  doughnutConfig
);







