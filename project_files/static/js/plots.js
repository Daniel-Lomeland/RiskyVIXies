// Trace1 for the Greek Data
var trace1 = {
    x: data.map(row => row.date),
    y: data.map(row => row.vix_close),
    text: data.map(row => row.date),
    name: "VIX",
    type: "line"
  };
  
//   Trace 2 for the Roman Data
  var trace2 = {
    x: data.map(row => row.date),
    y: data.map(row => row.sentiment_score),
    text: data.map(row => row.date),
    name: "Sentiment Score",
    type: "line"
  };
  
  // Combining both traces
  var data = [trace1, trace2];
  
  // Apply the group barmode to the layout
  var layout = {
    title: "VIX vs. Positivity",
    xaxis: { title: "Date" },
    yaxis: { title: "VIX" },
    yaxis2: {
        title: 'Sentiment Score',
        titlefont: {color: 'orange'},
        tickfont: {color: 'orange'},
        anchor: 'x',
        overlaying: 'n',
        side: 'right'
      }
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", data, layout);