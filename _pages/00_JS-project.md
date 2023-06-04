---
toc: true
layout: page
title: JS Tutorial
categories: [Week 37]
---

<html>
<head>
  <title>Movie Search App</title>
</head>
<body>
  <h1>Movie Search</h1>

  <form id="movieForm">
    <label for="movieInput">Movie Title:</label>
    <input type="text" id="movieInput" required>
    <button type="submit">Search</button>
  </form>

  <div id="movieContainer"></div>

  <script>
    function fetchMovieData(movieTitle) {
      var apiUrl = "https://api.themoviedb.org/3/search/movie?api_key=5f87798890b72c6ac53b262ba43ed8c6&query=" + movieTitle;

      var request = new XMLHttpRequest(); // XMLHttpRequest is used to request data from a server
      request.open("GET", apiUrl, true); // type of request, the url, true is asynchronous (does not have to wait for server response) and false is synchronous
      request.onload = function() { // anonymous function
        if (request.status >= 200 && request.status < 400) { // if request is successful
          var data = JSON.parse(request.responseText);
          displayMovieData(data);
        } else {
          document.getElementById("movieContainer").textContent = "Error fetching movie data.";
        }
      };
      request.onerror = function() { // anonymous function - will not be referenced anywhere else
        document.getElementById("movieContainer").textContent = "Error fetching movie data.";
      };
      request.send();
    }

    function displayMovieData(data) {
      if (data.results && data.results.length > 0) {
        var movie = data.results[0]; // extract relevant info
        var movieInfo = "<h2>" + movie.title + " (" + movie.release_date.substring(0, 4) + ")</h2>";
        movieInfo += "<img src='https://image.tmdb.org/t/p/w500" + movie.poster_path + "' alt='Movie Poster'><br>"; // image of the movie poster
        movieInfo += "<p><strong>Original Title:</strong> " + movie.original_title + "</p>"; // original title in original language
        movieInfo += "<p><strong>Overview:</strong> " + movie.overview + "</p>"; // summary of the plot
        movieInfo += "<p><strong>Popularity:</strong> " + movie.popularity + "</p>"; // the popularity is determined by the API provider - TMDB
        movieInfo += "<p><strong>Vote Average:</strong> " + movie.vote_average + "</p>"; // Average rating out of 10 - higher is better
        movieInfo += "<p><strong>Original Language:</strong> " + movie.original_language + "</p>"; // original language of the movie
        movieInfo += "<p><strong>Release Date:</strong> " + movie.release_date + "</p>"; // original release date
        movieInfo += "<p><strong>Vote Count:</strong> " + movie.vote_count + "</p>"; // how many people voted for the movie - more is better
        movieInfo += "<p><strong>Genre(s):</strong> " + getGenres(movie.genre_ids) + "</p>"; // a helper function and retrieves the genres from movie.genre_ids
        movieInfo += "<p><strong>Runtime:</strong> " + movie.runtime + " minutes</p>"; // How long movie is


        document.getElementById("movieContainer").innerHTML = movieInfo; // printing data onto the page
      } else {
        document.getElementById("movieContainer").textContent = "Movie not found.";
      }
    }

    function getGenres(genreIds) { // takes in an array as input
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

      var genres = []; // empty new list for the genres
      genreIds.forEach(function(genreId) { // is like a for loop, and iterates over each element in the array, and for each one it executes the function
        if (genreNames[genreId]) { // if the element in the array is also inside the genres dict
          genres.push(genreNames[genreId]); // adds that element into the new list using push
        }
      });

      return genres.join(", "); // return list of genres
    }

    document.getElementById("movieForm").addEventListener("submit", function(event) { // when the form is submitted, it displays the data
      event.preventDefault();
      var movieTitle = document.getElementById("movieInput").value;
      fetchMovieData(movieTitle);
    });
  </script>
</body>
</html>
