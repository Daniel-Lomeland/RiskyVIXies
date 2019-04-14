var apiKey = "fdPDrAaPm8chiPPsbMRx";

/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

  
/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} data
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */

 function unpack(data, index) {
  return data.map(function(row) {
    return row[index];
  });
}

function successHandle(response){
  var dates = unpack(response.dataset.data, 0)
  var closing = unpack(response.dataset.data, 4)
  console.log(dates);
  console.log(closing);
  var trace = {
    type: "scatter",
    mode: "lines",
    x: dates,
    y: closing,
    name: "Amazon"
  }
  var layout = {
    
  }
  Plotly.newPlot("plot",[trace],layout)
}

function errorHandle(error){
  console.log(error);
}



/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {
  // @TODO: YOUR CODE HERE
  d3.json(url).then(successHandle, errorHandle);
}

buildPlot();
