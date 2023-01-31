---
toc: true
layout: post
description: This is a blog post containing my part of the final project and how it fits into Collegeboard criteria
categories: [markdown, Week 20]
title: Create Performance Task Tri 2
---

## My Aspect
My aspect of the final project is a live ranking and likes list - similar to the Jokes APi from the APCSP Website.
Basic Info:
- Users can look at live data and which cars are most liked and dislike
- Rankings are constantly updated
Screenshot:
![]({{ site.baseurl }}/images/live-ranking-list.png)

---

## How it fits Collegeboard Criteria
Program Purpose and Function
- My program will have input and output - the input is when the user clicks the like or dislike of a certain model and the output is the test that says whatever car is most liked/disliked - and a definite purpose and function. The purpose of the program is for people to see which cars are most popular currently and which cars are most disliked. Users can press any like/dislike button of any model, and when they reload the page, a new most liked/disliked car appears at the bottom of the page.

Data Abstraction
- I will use a list to store data about how many users have clicked the buttons. I will then access the list later on to find out which car is most liked and disliked.

Managing Complexity
- I will use a list to manage complexity that stores the amount of times a button has been clicked. Without this list, I would have to manually store each button click in an individual variable. This would make the code longer, inefficient, and harder to read.

Procedural Abstraction
- I will develop a procedure with parameters that are used. This procedure will determine which button has been clicked the most, and this will be separate from the like and dislike button. Whichever like button is clicked the most, that car is the most liked car, and whichever dislike button is clicked the most, that car is the most disliked car.

Algorithm implementation
- My procedure will contain an algorithm that includes sequencing, selection, and iteration. Using a ```for loop```, I iterate through all the buttons. I use selection by using an ```if statement```, and I find the highest values by seeing if it was previously used. This algorithm will be performed in a sequential manner.

Testing
- The program will have two separate calls to the procedure - a like button and a dislike button being clicked. The conditions that are tested are that the number of clicks increases and may result in new cars at the bottom.

---

### Video Ideas
I will create a video showing the table and what it outputs. I will show clicking different buttons and, after reloading the page, show how the two cars outputted on the bottom of the page may change if the number of likes/dislikes also changes.