// Predict the VIX button reference
var button = d3.select("#click-me");

// Triggered when Predict the VIX is clicked
function handleClick() {
    var predictionUrl = "http://127.0.0.1:9999/api";

    d3.json(predictionUrl).then(function (response) {
        var prediction = response;
        var face = "";
        console.log(prediction);
         
        if (prediction > 2.5) {
            face = "<img src='../static/images/fear.png' alt='fear'>"
          } else if (prediction > -3) { 
            face = "<img src='../static/images/neutral.png' alt='neutral'>"
          } else {
            face = "<img src='../static/images/happy.png' alt='happy'>"
          }


        var x = document.getElementById("predict-table").rows.length;
        if (x > 1) {
            deleteRow();
        }
        var tbody = d3.select("tbody");
        var row = tbody.append("tr");
        var cell = tbody.append("td");
        cell.text(prediction);
        var cell = tbody.append("td");
        cell.html(face);
    })
}

button.on("click", handleClick);