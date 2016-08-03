var baseURL = "http://acf7984ae549511e69b640206bb85836-1252824845.eu-central-1.elb.amazonaws.com:5000/orchestrate/api/v1.0/";
//var baseURL = "http://localhost:5000/orchestrate/api/v1.0/";

function sendGetRequest(endpoint) {
  $.get(baseURL + endpoint, function(data, status){
       alert("Data: " + data + "\nStatus: " + status);
   });
}

function sendPostRequest(endpoint) {
  $.post(baseURL + endpoint, function(data, status){
       alert("Data: " + data + "\nStatus: " + status);
   });
}
