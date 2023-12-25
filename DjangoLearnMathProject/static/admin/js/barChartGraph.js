// Bar Chart
const labels = ["Trignometry", "Calculus", "Integration", "Geometry", "Algebra","Matrix", "Functions" ,"Graphs", "Pre Cal", "Algebra 2", "Trignometry", "Geometry", "Ratios", "Functions", "Integ"];
const values = [60000, 70000, 70000, 75000, 80000, 25000, 80000, 75000, 60000, 80000, 80000, 75000, 80000, 100000, 80000];

// Bar chart setup 
const barChartData = {
  labels: labels,
  datasets: [{
    data: values,
    backgroundColor: 'rgba(116, 63, 203, 1)',
    barThickness:'12',
    barThickness: 20,
    borderRadius: 10
  }]
};

// Bar chart config 
const barChartConfig = {
  type: 'bar',
  data: barChartData,
  options: {
      maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      title: {
        display: true,
        text: 'No. of People vs Categories',
        color:'#3D4857',
        align: 'start',
        padding:{
          bottom:25
        },
        font:{
          size: 16,
          weight: 700,
          // lineHeight: 20,
          // family: 'Roboto'
        },
      },
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
};

// Bar chart render
const myBarChart = new Chart(
  document.getElementById('myBarChart'),
  barChartConfig
);