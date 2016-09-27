var baseURL = "http://acf7984ae549511e69b640206bb85836-1252824845.eu-central-1.elb.amazonaws.com:5000/orchestrate/api/v1.0/";
//var baseURL = "http://localhost:5000/orchestrate/api/v1.0/";

function sendGetRequest(endpoint) {
  $.get(baseURL + endpoint, function(data, status){
       alert("Data: " + data + "\nStatus: " + status);
   });
}

function sendPostRequest(endpoint) {
  $.post(baseURL + endpoint, function(data, status){
       //alert("Data: " + data + "\nStatus: " + status);
       $( ".list-group" ).append( "<li class='list-group-item'>"+data+"<span class='glyphicon glyphicon-ok' aria-hidden='true'></span></li>" );
       redirect();
   });
}

function redirect() {
  if($('.list-group-item').length == 2){
    setTimeout("window.location.href = 'map.html';", 2000);
  }
}

function init() {
  $.get(baseURL + 'getServiceEndPoint', function(data, status){
      url = data + ':9090';
      initRos(url);
  });
}

function initRos(url) {
    // Connect to ROS.
    var ros = new ROSLIB.Ros({
      url : 'ws://' + url
    });

    // Create the main viewer.
    var viewer = new ROS2D.Viewer({
      divID : 'nav',
      width : 900,
      height : 900
    });

    // Setup the nav client.
    var nav = NAV2D.OccupancyGridClientNav({
      ros : ros,
      rootObject : viewer.scene,
      viewer : viewer,
      serverName : '/move_base'
    });
}
