---
toc: true
layout: page
title: JS Tutorial
categories: [Week 37]
---

<html>
<head>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">
    <style>
    body {
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    form {
      margin-bottom: 20px;
    }
    input[type="text"] {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 4px;
      background-color: #4CAF50;
      color: #fff;
      border: none;
      cursor: pointer;
    }
    .movie-container {
      margin-bottom: 20px;
    }
    .movie-series-table {
      width: 100%;
      border-collapse: collapse;
    }
    .movie-series-table th,
    .movie-series-table td {
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    .movie-series-table th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>Movie Search</h1>

  <h2>Search for a Single Movie</h2>
  <form id="movieForm">
    <input type="text" id="movieInput" placeholder="Enter movie title">
    <button type="submit">Search</button>
  </form>
  <div id="movieContainer"></div>

  <h2>Search for a Movie Series</h2>
  <form id="seriesForm">
    <input type="text" id="seriesInput" placeholder="Enter series title">
    <button type="submit">Search</button>
  </form>
  <div id="seriesContainer"></div>

  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
  <script>
    function fetchMovieData(movieTitle) {
      var apiUrl = "https://api.themoviedb.org/3/search/movie?api_key=5f87798890b72c6ac53b262ba43ed8c6&query=" + movieTitle;
      var request = new XMLHttpRequest(); // XMLHttpRequest used to request data from a server
      request.open("GET", apiUrl, true);  // type of request, the url, true is asynchronous (does not have to wait for server response) and false is synchronous
      request.onload = function() {
        if (request.status >= 200 && request.status < 400) { // if request is successful
          var data = JSON.parse(request.responseText); // converts the JSON string from the API into a JS variable
          displayMovieData(data);
        } else {
          document.getElementById("movieContainer").textContent = "Error fetching movie data.";
        }
      };
      request.onerror = function() {
        document.getElementById("movieContainer").textContent = "Error fetching movie data.";
      };
      request.send();
    }
    function displayMovieData(data) {
      if (data.results && data.results.length > 0) {
        var movie = data.results[0]; // extract relevant info            substring() extracts characters within the identified indices
        var movieInfo = "<h2>" + movie.title + " (" + movie.release_date.substring(0, 4) + ")</h2>"; // At the top, it will display the movie name and the year released
        movieInfo += "<img src='https://image.tmdb.org/t/p/w500" + movie.poster_path + "' alt='Movie Poster'><br>"; // image of the movie
        movieInfo += "<p><strong>Original Title:</strong> " + movie.original_title + "</p>";  // original title of the movie
        movieInfo += "<p><strong>Overview:</strong> " + movie.overview + "</p>";  // summary of the movie plot
        movieInfo += "<p><strong>Popularity:</strong> " + movie.popularity + "</p>"; // the popularity is determined by the API provider - TMDB
        movieInfo += "<p><strong>Vote Average:</strong> " + movie.vote_average + "</p>"; // Average rating out of 10 - higher is better
        movieInfo += "<p><strong>Original Language:</strong> " + movie.original_language + "</p>"; // Original language of the movie
        movieInfo += "<p><strong>Release Date:</strong> " + movie.release_date + "</p>"; // original release date
        movieInfo += "<p><strong>Vote Count:</strong> " + movie.vote_count + "</p>"; // How many people voted for the movie
        movieInfo += "<p><strong>Genre(s):</strong> " + getGenres(movie.genre_ids) + "</p>"; // the different genres in an array is sent to a helper function
        document.getElementById("movieContainer").innerHTML = movieInfo; // displays the data on the page
      } else {
        document.getElementById("movieContainer").textContent = "Movie not found.";
      }
    }
    function getGenres(genreIds) { // takes in an array as an input
      var genreNames = {
        28: "Action",
        12: "Adventure",
        16: "Animation",
        35: "Comedy",
        80: "Crime",
        99: "Documentary",
        18: "Drama",
        10751: "Family",
        14: "Fantasy",
        36: "History",
        27: "Horror",
        10402: "Music",
        9648: "Mystery",
        10749: "Romance",
        878: "Science Fiction",
        10770: "TV Movie",
        53: "Thriller",
        10752: "War",
        37: "Western"
      };
      var genres = []; // new empty list
      genreIds.forEach(function(genreId) { // similar to for loop, iterates over each element and for each one executes the function
        if (genreNames[genreId]) { // if the element in the array is in the genres dict
          genres.push(genreNames[genreId]); // adds tht element into new list using push
        }
      });
      return genres.join(", ");
    }
    document.getElementById("movieForm").addEventListener("submit", function(event) { // when form is submitted, the data is displayed
      event.preventDefault();
      var movieTitle = document.getElementById("movieInput").value;
      fetchMovieData(movieTitle);
    });
    function fetchMovieSeriesData(seriesTitle) {
      var apiUrl = "https://api.themoviedb.org/3/search/movie?api_key=5f87798890b72c6ac53b262ba43ed8c6&query=" + encodeURIComponent(seriesTitle); 
      var request = new XMLHttpRequest(); // requests data
      request.open("GET", apiUrl, true); // fetches the data from the url
      request.onload = function() { 
        if (request.status === 200) { // if request is successful - more specific than before
          var data = JSON.parse(request.responseText); // JS variable from JSON data
          fetchSeriesMovieData(data);
        } else {
          document.getElementById("seriesContainer").textContent = "Error fetching movie series data.";
        }
      };
      request.onerror = function() {
        document.getElementById("seriesContainer").textContent = "Error fetching movie series data.";
      };
      request.send();
    }
    function fetchSeriesMovieData(data) {
      if (data.results && data.results.length > 0) { // checks that data contains info and is not empty
        var movieSeries = data.results;
        var creditsDataPromises = movieSeries.map(function(movie) { // creates an array of promises, which each fetch data for a movie in the series through a separate API request
          var apiUrl = "https://api.themoviedb.org/3/movie/" + movie.id + "/credits?api_key=5f87798890b72c6ac53b262ba43ed8c6";
          return fetch(apiUrl).then(function(response) { // each request from each promise
            return response.json();
          });
        });
        Promise.all(creditsDataPromises).then(function(creditsData) { // All promises are resolved and a new function is called with the movies series and the data
          displayMovieSeriesData(movieSeries, creditsData);  
        }).catch(function(error) { // if an error appears
          document.getElementById("seriesContainer").textContent = "Error fetching movie series data.";
        });
      } else {
        document.getElementById("seriesContainer").textContent = "No movie series found.";
      }
    }
    function displayMovieSeriesData(movieSeries, creditsData) {
      var table = document.createElement("table"); // creates a JS table
      table.classList.add("movie-series-table"); // styles the table
      var tableHeader = table.createTHead(); // a header is created 
      var headerRow = tableHeader.insertRow(); // Rows are added to the table
      var columns = ["Title", "Popularity", "Vote Count", "Vote Average", "Poster"]; // column titles
      for (var i = 0; i < columns.length; i++) { // iterates through column array and continues until i is greater than length of columns
      // basically, rows are created for every column
        var th = document.createElement("th"); // rows are added underneath the headers
        th.textContent = columns[i]; // data is added to the rows
        headerRow.appendChild(th); // the rows are displayed
      }
      var tableBody = table.createTBody(); // the body of the table is created
      for (var j = 0; j < movieSeries.length; j++) { // another for loop but iterates through the data
      // this way, every single row with contain data since the loop stops once all the data is iterated through
        var movie = movieSeries[j]; // the data is assigned to a variable
        var row = tableBody.insertRow(); // rows are added to the body
        var titleCell = row.insertCell(); 
        titleCell.textContent = movie.title; // the title is displayed in new cells at the rows
        var popularityCell = row.insertCell();
        popularityCell.textContent = movie.popularity; // the popularity is displayed
        var voteCountCell = row.insertCell();
        voteCountCell.textContent = movie.vote_count; // the vote count is displayed
        var voteAverageCell = row.insertCell();
        voteAverageCell.textContent = movie.vote_average; // the vote average is displayed
        var posterCell = row.insertCell();
        var posterImage = document.createElement("img"); // An image element is created
        posterImage.src = "https://image.tmdb.org/t/p/w200" + movie.poster_path; // the image is shown
        posterImage.alt = "Movie Poster"; // if image is not shown
        posterCell.appendChild(posterImage); // the image is displayed on the table
      }
      document.getElementById("seriesContainer").appendChild(table); // the table is displayed on the website
      $('.movie-series-table').DataTable(); // initializes the DataTables plugin - enables sorting and searching
  } 
    document.getElementById("seriesForm").addEventListener("submit", function(event) { // when the second form is submitted, the table is displaysed
      event.preventDefault();
      var seriesTitle = document.getElementById("seriesInput").value;
      fetchMovieSeriesData(seriesTitle);
    });
  </script>
</body>
</html>
