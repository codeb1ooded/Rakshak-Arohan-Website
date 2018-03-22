function drawCircle(point, radius, dir) {
var d2r = Math.PI / 180;   // degrees to radians
var r2d = 180 / Math.PI;   // radians to degrees
var earthsradius = 3963; // 3963 is the radius of the earth in miles

   var points = 32;

   // find the raidus in lat/lon
   var rlat = (radius / earthsradius) * r2d;
   var rlng = rlat / Math.cos(point.lat() * d2r);


   var extp = new Array();
   if (dir==1)	{var start=0;var end=points+1} // one extra here makes sure we connect the
   else		{var start=points+1;var end=0}
   for (var i=start; (dir==1 ? i < end : i > end); i=i+dir)
   {
      var theta = Math.PI * (i / (points/2));
      ey = point.lng() + (rlng * Math.cos(theta)); // center a + radius x * cos(theta)
      ex = point.lat() + (rlat * Math.sin(theta)); // center b + radius y * sin(theta)
      extp.push(new google.maps.LatLng(ex, ey));
      bounds.extend(extp[extp.length-1]);
   }
   // alert(extp.length);
   return extp;
   }

var map = null;
var bounds = null;

  // Define a symbol using SVG path notation, with an opacity of 1.
  var lineSymbol = {
    path: 'M 0,-1 0,1',
    strokeOpacity: 1,
    scale: 4
  };

function initialize() {
  var myOptions = {
    zoom: 10,
    center: new google.maps.LatLng(, ),
    mapTypeControl: true,
    mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
    navigationControl: true,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map_canvas"),
                                myOptions);

  bounds = new google.maps.LatLngBounds();

  var donut = new google.maps.Polyline({
                 path: drawCircle(new google.maps.LatLng(20.537,78.9629), 100, 1),
                 strokeOpacity: 0,
                 icons: [{
                   icon: lineSymbol,
                   offset: '0',
                   repeat: '20px'
                 }],
                 strokeWeight: 2,
                 fillColor: "#FF0000",
                 fillOpacity: 0.35
     });
     donut.setMap(map);

 map.fitBounds(bounds);

}