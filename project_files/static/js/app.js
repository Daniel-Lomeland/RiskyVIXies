// Predict the VIX button reference
var button = d3.select("#click-me");

// Triggered when Predict the VIX is clicked
function handleClick() {
    console.log("VIX Prediction: +++");
    var x = document.getElementById("predict-table").rows.length;
    if (x > 1){ 
        deleteRow();
    }
    var tbody = d3.select("tbody");
    var row = tbody.append("tr");
    var cell = tbody.append("td");
    cell.text("4/25/2019");
    var cell = tbody.append("td");
    cell.text("+4.7586%");
    var cell = tbody.append("td");
    cell.text(":-(");
}

button.on("click", handleClick);