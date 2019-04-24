// Trace1 for VIX data
var trace1 = {
    x: data.map(row => row.date),
    y: data.map(row => row.vix_close),
    // text: data.map(row => row.date),
    mode: 'lines',
    line: {
        color: '#4B8937',
        width: 3
    },
    name: "VIX",
    // type: "line"
  };
  
//   Trace 2 for Sentiment Score
  var trace2 = {
    x: data.map(row => row.date),
    y: data.map(row => row.sentiment_score),
    // text: data.map(row => row.date),
    name: "Positivity",
    // type: "line",
    yaxis: "y2",
    mode: 'lines',
    line: {
        color: '#FF7700',
        width: 1,
        dash: "dot"
    }
  };
  
  // Combining both traces
  var data = [trace1, trace2];
  
  // Apply the group barmode to the layout
  var layout = {
    title: "VIX vs. Positivity",
    xaxis: { 
        title: "Date", 
        tickangle: "-45",
    },
    yaxis: { 
        title: "VIX Closing Value (Source: CBOE)" ,
        titlefont: {color: '#4B8937'},
        tickfont: {color: '#4B8937'},
        color: '#4B8937'
    },
    yaxis2: {
        title: 'Sentiment Score',
        titlefont: {color: '#FF7700'},
        tickfont: {color: '#FF7700'},
        anchor: 'x',
        overlaying: 'y',
        side: 'right'
      },
      autosize: false,
      width: 1200,
      height: 800,
      margin: {
        l: 50,
        r: 50,
        b: 100,
        t: 100,
        pad: 4
      },
      showlegend: true,
      legend: {
          x: 1.1,
          y: 1,
          traceorder: 'normal',
          font: {
              family: 'sans-serif',
              size: 12,
              color: '#000'
          },
          bordercolor: '#DDD1C7',
          borderwidth: 1
      }
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", data, layout);