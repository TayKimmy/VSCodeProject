---
toc: true
layout: post
description: This is a blog post that contains the written response for the Collegeboard CPT
categories: [markdown, Week 24]
title: Collegeboard CPT Written Response
---

### 3 a.

---

### 3.a.i
The program is designed to allow users to see which cars are most popular and trending that will then enable them to make informed decisions when buying electric cars.

---

### 3.a.ii
The video shows that users are able to add new cars to the table, and that the car will stay in the table until it is deleted. 

---

### 3.a.iii
The input of typing in a car name and pressing the button, or pressing the like/delete buttons result in an output that does what it is supposed to do.

---

### 3 b.

---

### 3.b.i
![]({{ site.baseurl }}/images/cpt-abstraction-1.png)

---

### 3.b.ii
![]({{ site.baseurl }}/images/cpt-abstraction-2.png)

---

### 3.b.iii
The name of the list that I chose is called schemas.

---

### 3.b.iv
The data in this list contains the user id, car name, and number of likes. This is stored in a dictionary that is stored in the list schemas. This list is used to create the database that will create the table in my program.

---

### 3.b.v
This list here enables the database to be built quickly and efficiently. Through this, it manages the complexity of the code by making it clearer and only having what it needs. Without this list, I would have to create each element individually and somehow add it to the database, making it much more complicated.

---

### 3 c.

---

### 3.c.i
![]({{ site.baseurl }}/images/cpt-procedure-1.png)

---

### 3.c.ii
![]({{ site.baseurl }}/images/cpt-procedure-2.png)

---

### 3.c.iii
The procedure called like_cars contributes to the functionality of the program because it adds the amount of likes of a car by 1 each time the respective like button is clicked. This updates the table and creates a live list.

---

### 3.c.v
![]({{ site.baseurl }}/images/cpt-algorithm-1.png)

---

### 3.c.vi.
This algorithm fetches the API, or the database that I created earlier, and iterates through it. The selection if statement looks to see if the response status has a certain value, and if it does, it prints an error message. When the algorithm iterates through the API in sequential order, the algorithm then recreates the table with the updated values.

---

### 3 d.

---

### 3.d.i
First Call:
The first call is add_row(data)

Second Call:
The second call is tr.appendChild(td)

---

### 3.d.ii
First call conditions:
The first call checks to make sure that there is an error before it is passed. Only if there is an error is this call passed.

Second call conditions:
The second call can only be passed if there are no errors, and if there are none, then data is collected from the JSON file and sent to the next function.

---

### 3.d.iii
Result of first call:
The first call adds to the table a new row.

Result of the second call:
The second call calls another function that will create the table and the buttons.