# Final Project

## Overview
The purpose of this final project is for you to apply what you have learnt in this course. To make your learning meaningful it is important that you write the code on your own and try to explore and apply as many concepts as you have learned in doing this project.
You have the option to choose among the following categories:
1. Vehicle Rent Program
1. Minesweeper Game
1. Create Your Own Utility/Productivity Program

All the the above categories **must be implemented as a web-based application using Flask**.

You need to choose only **ONE** of them. Please see the criteria and deliverable for each of those options in the subsequent sections.

## Deliverables

1. Flask Python codes: You need to deploy your Flask code and submit your code to Vocareum. Ensure that your deployment in Vocareum works.
1. Readme.md: Inside your folder, create a file called Readme.md . Use Markdown to write your document and format it accordingly. Make sure to include the following in your documentation:
    - Brief description of the software, i.e. what it does.
    - How to use the software. Include steps how to run it and how to use all the features.
    - Design of the software. Include: 1) Software specifications, 2) any UML diagrams (search for online tools to draw UML class diagram), 3) Features, modules, etc.
1. 15 minutes presentation: Demo your software and how you design the software on the last day of this course.

**Due-date: 9th of September 2021, 9AM.**

## Rubrics

| Category                       | 0-1                                                                                                                                                                    | 2-3                                                                                                                                                 | 4-5                                                                                                                                                                                                                                 |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Problem and Solution           | Only some features of basic Minesweeper / Vehicle Rental were implemented. Program in the Open-Ended category is too simple and/or is not useful. | All features for basic Minesweeper / Vehicle Rental / Open-Ended Program were implemented. | Interesting / useful / user-friendly / close to real-life applications extra features for Minesweeper / Vehicle Rental / Open-Ended Program were implemented.
| Code and Documentation         | The code is poorly/not documented. Not written using procedural nor object-oriented design. Not following PEP8. Not modular.                                           | There are appropriate comments explaining the code. There is a mix of object-oriented and procedural programming.                                     | The code is well written, follows PEP8 and is modular. The code is well documented either using docstring or comments. The code is designed and written using the object-oriented paradigm.                                                       |
| Design and Optimization        | Student is unable to explain the design of the code.                                                                                                                   | Student can explain the design of the software in terms of its functions and structures.                                                            | Student can explain the design of the software in both Readme.md and presentation. Student put effort in designing the data structures and choosing the algorithms. Student can explain the choice and design of the class diagram. |
| Presentation and Communication | Student does not present clearly on the work and/or unable to answer questions related to the work.                                                                      | Student can present the work and is able to answer some questions related to the work.                                                                 | Student communicates well during the presentation and is able to answer the questions related to the work.                                                                                                                                 |

## Web-based Minesweeper Game

In this project, you will implement a Minesweeper Game using Flask.  You should use object oriented design to implement this game. The program should prompt users for the commands to be executed. There are three basic kinds of commands: 1) open, 2) flag, 3) quit. The quit command is executed by typing quit in the prompt. The open and flag command should allow the user to choose the cell, i.e. which row and which column. For example, a user can open row A and col 3 or flag row B and col 31.

### Reference

- [Minesweeper Online](http://minesweeperonline.com/)
- [Wikipedia article on Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game))

### Concepts to Apply

In implementing this program, you should try to apply the following concepts:

- Object-oriented design: Try to design your program as objects. Use UML diagrams to specify the relationship between the classes that you use. See if you have any of the following relationships:
    - *has-a* relationship
    - *is-a* relationship
- Property: Try to implement your object using property instead of just attributes.
- Data Structures: Try to implement some of the data structures either using Python's built-in types or create your own data types.
- Recursion: Try to use recursion in your algorithm to open up the surrounding tiles.
- Modularization: Try to create different functions or methods in your class and modularize your code to some unit tasks.
- Compositions: Try to call another functions or methods from within a function or a method.

### Extra Features

You can try to implement the following in your game:

- Allow user to specify the size of the grid
- Allow user to specify the ratio of the mines


## Vehicle Rental Program

### The Problem

The problem is to develop an object-oriented design and implementation of a web-based program capable of maintaining reservations for a vehicle rental agency. The agency rents out three types of vehicles: 

- cars, 
- vans, and 
- moving trucks. 

The program should allow users to:

- check for available vehicles
- request rental charges by vehicle type
- get the cost of renting a particular type vehicle for a specified period of time, and
- make/cancel reservations


### Reference

See the full problem for a similar text-based problem in: [Vehicle Rental Problem](https://sutdapac-my.sharepoint.com/:b:/g/personal/oka_kurniawan_sutd_edu_sg/EQeebPYHPUBOo7PIeOJDKrsBURo53xBvwBIvi-lq2ToLCA?e=UXgblf)

### Concepts to Apply

In implementing this program, you should try to apply the following concepts:

- Object-oriented design: Try design your program as objects. Use UML diagrams to specify the relationship between the classes that you use. See if you have any of the following relationships:
    - *has-a* relationship
    - *is-a* relationship
- Inheritance: One specific object-oriented feature in this problem is to use inheritence for the different `Vehicle` subclasses. 
- Property: Try to implement your object using property instead of just attributes.
- Data Structures: Try to implement some of the data structures either using Python's built-in types or create your own data types. **One of the feature is to find and retrieve vehicle information**. Instead of using Python's `list`, can you use other data type to make this operation more efficient?
- Modularization: Try to create different functions or methods in your class and modularize your code to some unit tasks.
- Compositions: Try to call another functions or methods from within a function or a method.
- Database: Try to save your data into a database and retrieve it when you need it.

### Extra Features

You can try to implement the following in your game:

- Add option to sort your view based on a particular column. For example, in *Checking Available Vehicles*, you can sort the view based on the *models*, or *number of passengers*, or *number of doors*, etc.
- Add an option to view *past rental* which displays the past rental the user has made on the system.

## Open-Ended Utility / Productivity Program

This is an *open-ended* category. This means that you are free to do any kind of software you would like to build under the category of *utility* or *productivity*. Some examples of this software are those that make your life or day-to-day tasks easier or more productive. Some examples are (but not limited to only these):

- **Note Taking Software**: You can write a web-based note taking software where you can quickly save short text for you to take note or recall. You can save these texts and search the text using some keyword. You can add features like reminder and make it into a to-do list software.
- **Quick Calculator Software**: You may tend to do some specific calculation again and again. As an example, it can be your financial calculator for investment or retirement savings. You can write a Python program to do these tasks. 
- **Family Tree Software**: You can create a software to store information on your family tree. This can be useful when someone in your family wants to retrieve information related to this. You can let the user to add or edit information, search for a name and retrieve the relationship of this person, or browser through the family tree to find out the different names and people in the family.
- **Conversion Software**: You can create some software to convert data from one format to another. For example, you can download your Bank account or credit card statements in CSV or PDF and format or filter it for your own use like automatically categorizing your expenses and income. 
- ...and many others

In choosing this category you need to explain the following:

- Why do you choose to write this software? Make sure the reason is meaningful and not just for the sake of this assignment.
- Where do you get your inspiration? You don't need to be original. You may have used some of the software in your web applications or desktop, and you can write a simplified text-based version of it. 
- How do you design your software using object-oriented? How do you modularize your code?
- What kind of data structures do you use and why?
