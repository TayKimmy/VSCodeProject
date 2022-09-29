---
toc: true
layout: post
description: This is a post that has the notes for the Collegeboard videos on program design
categories: [markdown, Week 6]
title: Collegeboard Program Design Notes
---
## Collegeboard Notes

### Essential Knowledge
- A development process can be ordered and intentional or exploratory in nature
- There are multiple development processes. The following phrases are commonly used when developing a program:
    - Investigating and refleting
    - Designing
    - Prototyping
    - Testing
- A development process that is iterative requires refinement and revision based on feedback, testing, or reflection throughout the process. This may require revisiting earlier phrases of the process.
- A development proess that is incremental is one that breaks the problem into smaller pieces and makes sure each piece works before adding it to the whole.
- The design of a program incorporates investigation to determine its requirements.
- Investigation in a development process is useful for understanding and identifying the program constraints, as well as the concerns and interests of the people who will use the program.
- Some ways investigation can be performed are as follows:
    - Collecting data through surveys
    - User testing
    - Inteviews
    - Direct observations
- Program requirements describes how a program functions and may include a description of user interactions that a program must provide

---

### How is a Program Developed?
Rarely a solo endeavor
- Usually developed by teams of people
It all starts with an idea
- Programs are developed with a specific purpose in mind
- Developers follow specific steps and stick to their plan
- Sometimes the development is more exploratory than anything, and the steps are dictated by what happens (both good and bad)
    - Think about early AI projects, like personal assistants
Developers start investigating the problem/purpose and reflect
- Investigation is an important step in the process
- Developers must:
    - Determine the requirements of the program
    - Understand the constraints
    - Understand the user concerns and interests
- How do developers investigate?
    - Surveys
    - User testing
    - Interviews
    - Direct observations
After initial investigation and reflection,
- Developers design the program by
    - Brainstorming (draw on investigation)
    - Storyboarding the program
    - Planning user experience
    - Laying out the user interface
    - Organizing into modules
    - Develop a testing strategy
- Developers decide on the program requirements that
    - Describe how a program should behave
    - Include a list of user interactions
- The program specifications outline all of the requirements
- Developers create a prototype of the program (or components):
    - An incremental process is frequently used so developers can refine small parts (modules) of the program
Testing, testing, and more testing!
- Developers test the program every step of the way
- Testing occurs at the
    - Micro level
    - Macro level
- Developers refine and revise through testing, feedback, and reflection

---

### When does documentation happen?
Documentation happens throughout the development of the program:
- At the beginning: list specifications
- During: to keep track of process
- After: to explain the overall process
Documentation throughout can improve:
- Efficiency of overall programming process
- Programmers' ability to test and refine the program
- Programmers' response to bugs

---

### Collegeboard quiz results
This is the screenshot of the results of the quiz I took on Collegeboard

![]({{ site.baseurl }}/images/Fastpages-collegeboard-design.png)

---

## Final Project Design

### Idea/Brain Write
A random quiz generator. Save notes in the website and the alogrithm uses the notes to genrate questions for a quiz. The quiz is then scored and the topics missed are highlighted.
Me and my team reviewed over the different possible final project ideas that we made and this is the best one we came up with.

---

### Outline and how it fits requirements
Program Purpose and Function
-The purpose of the program is to randomly generate questions based on a user's notes of key terms/dates/ideas and definitions. The program will take the user's notes and, based on it, select the key terms and output multiple quiz questions which will be displayed randomly. It will score the quiz and tell you what you got wrong and what you need to study on.

Data Abstraction
- The program will contain lists and dictionaries. Every key term will have a definition and these will be stored in a dictionary which will be stored in a list. Or they will be stored in a local database and we will use the objects in the database to create the quiz.

Managing Complexity
- The dictionaries and databases will manage the complexity of the program by organizing the data inputted by the user. It will also help calling back to create the quiz.

Procedural Abstraction
- A function will be created to call back to the data inputted by the user. The function will iterate over the dictionary/database and use the values in them as a parameter to make a quiz.

Algorithm Implementation
- Like stated before, the program will contain a function that uses iteration and sequencing to make a quiz based off the data inputted by the user that is saved in a database or dictionary.

Testing
- The function will be called each time the user inputs a note and each time the user generates a quiz. When the user inputs a note, the function is called and saves the note inside a dictionary or database. When the user presses the button that generates the quiz, the function is again called and iterates through the user's notes to generate a quiz that is related to the key terms the user inputted.

---

### Wire Frame Development
