function display(data) {
    const city = "Tobyhanna, PA";
    let nTemp = data.periods[0].temperature + "&deg; F";
    let sShortForeCast = data.periods[0].shortForecast;
    let bIsDayTime = data.periods[0].isDaytime
    let oDate = new Date();
    let oStartTime = new Date(data.periods[0].startTime);
    let oEndTime = new Date(data.periods[0].endTime);
    let sStartTime = oStartTime.getHours() + ":" + oStartTime.getMinutes() + "0";
    let sEndTime = oEndTime.getHours() + ":" + oEndTime.getMinutes() + "0";
    const aMonths = ["January", "February","March","April","May","June",
        "July","August","September","October","November","December"
    ];
    const aWeekDay = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

    let font_color;
    let bg_color;
    let minutes = oDate.getMinutes() < 11 ? "0" + oDate.getMinutes() : oDate.getMinutes();

    let today = aWeekDay[oDate.getDay()].toUpperCase() + " " + 
        aMonths[oDate.getMonth()].toUpperCase().substring(0, 3) + " " + oDate.getDate() +" <br>" +
        oDate.getHours() + ":" + minutes;
     
    if(bIsDayTime) {
      font_color = "#EAB703";
      bg_color = "#0337EA";

      if (sShortForeCast === "Sunny") {  
        $(".weathercon").html(
          "<img src= 'sun.svg'alt='sun'height='100' width= '100' />"
        );
      } else {
        $(".weathercon").html(
          "<img src= 'clouds.svg'alt='clouds'height='100' width= '100' />"
        );
      }
    } else {
      font_color = "#44c3de";
      bg_color = "#000000";

      $(".weathercon").html(
        "<img src= 'moon.svg'alt='moon'height='100' width= '100' />"
      );

    }// end if(bIsDayTime)
    // render to page
    $(".location").html(city);
    $(".temp").html(nTemp);
    $(".date").html(today);
    $("#range").html(sStartTime + " - " + sEndTime);
    $(".box").css("background", bg_color);
    $(".location").css("color", font_color);
    $(".temp").css("color", font_color);

    $("#forecast").html(sShortForeCast);
  } // end display(data)


 
function getGovWeather(sURL){
    fetch(sURL)
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('Looks like there was a problem. Status Code: ' +
                response.status);
                return;
            }
            response.json().then(function(data) {
                display(data.properties);
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });

}// end getGovWeather(sURL)

(function () {
    // https://www.weather.gov/documentation/services-web-api
    getGovWeather("https://api.weather.gov/gridpoints/PHI/33,130/forecast/hourly")
}());


