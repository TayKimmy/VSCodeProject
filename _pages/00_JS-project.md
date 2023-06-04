---
toc: true
layout: page
title: JS Tutorial
categories: [Week 37]
---

<html>
<head>
  <title>Weather Forecast Display</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <h1>Weather Forecast</h1>

  <form id="locationForm">
    <label for="locationInput">Location:</label>
    <input type="text" id="locationInput" required>
    <button type="submit">Get Weather</button>
  </form>

  <div id="weatherContainer"></div>

  <script>
    // Function to fetch weather data from weatherstack API
    function fetchWeatherData(location) {
      var apiKey = "4d8dad4f0e7affa082ea6e906009369e";
      var apiUrl = "http://api.weatherstack.com/current" + apiKey + "&query=" + location;
      $.ajax({
        url: apiUrl,
        dataType: "json",
        success: function(data) {
          displayWeatherData(data);
        },
        error: function() {
          $("#weatherContainer").text("Error fetching weather data.");
        }
      });
    }
    // Function to display weather data on the page
    function displayWeatherData(data) {
      var weather = data.current;
      var location = data.location.name + ", " + data.location.country;

      var weatherInfo = "Location: " + location + "<br>";
      weatherInfo += "Temperature: " + weather.temperature + "°C<br>";
      weatherInfo += "Humidity: " + weather.humidity + "%<br>";
      weatherInfo += "Wind Speed: " + weather.wind_speed + " km/h<br>";
      weatherInfo += "Weather Description: " + weather.weather_descriptions[0] + "<br>";
      $("#weatherContainer").html(weatherInfo);
    }
    $("#locationForm").submit(function(event) {
      event.preventDefault();
      var location = $("#locationInput").val();
      fetchWeatherData(location);
    });
  </script>
</body>
</html>
