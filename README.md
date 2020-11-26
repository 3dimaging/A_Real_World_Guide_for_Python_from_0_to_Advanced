# A_Real_World_Guide_for_Python_from_0_to_Advanced

The real world of python learner: you may have only 30 min per day to learn Python programming. It is quite often that sometimes you may not have no time at all. When you have time to go back where you left, you will find you forget everything. Because of the working load, family duties and other unexpected staff to deal with, you can be still at the entry level after a year of learning and have to start over again.

This tutorial is to help you to break the strange cycle and really improve your programming skill through the journely of mastering Python.

First, I want to mention something important, but you may not pay attention to before reading this tutorial.

- Active vs. Passive learning

    Active learning is to explore this field by yourself. You keep asking yourself questions and try to find the answer over internet and take notes.
    
    Passive learning is to follow the teachers to learn what you should learn, but do not ask why you should learn.

- The framework of Knowledge is more important than the Knowledge itself. 

    The framework is the basic structure of a course or field. It is quite obvious for the people with special training in the field. However, if a layman want to learn this field by himself, to build the framework is the most important part.
    
    To do this, try to focus on some simple books with knowleges well organized. I may also want to follow this post. The aim of this post also try to build the framework, but at the same time I will point out the difficult and important knowleges for python programming.
    
- The best website to learn python (highly recommend)

    https://www.python-course.eu/


## step 0: basic setup

### create an account on https://stackoverflow.com

    This is a website you will visit everyday. This is an important website to ask any question. The answers are usually already there.
    The only thing you need to do is Google your question.
    
### create an OneNote or Evernote account.

    Then have their clippers installed to your web browser. If you find your anwser on web, save it by the clippers
    
### have a notebook (paper or electronic) to write down what you know and you need to know.

    At the begining, you may just write down some keywords in your brain. later on, you will write down the knowledge tree to show the
    connections of the key words to each other. 
    

## step 1: get to know Python

"Everything is an Object." --- Don't be fooled. That just means using "." in your code. Forget object now. 

### material to read

Two books: "PFundamentals of Python Programming" and "An introduction of computation and programming in python".

- https://cs.appstate.edu/~rmp/cs2435/pythonbook.pdf
- https://www.amazon.com/exec/obidos/ASIN/0262529629/ref=nosim/mitopencourse-20
 
  https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/index.htm

### the best way to learn python

First, find a piece of code online, then type in all the lines on your computer, and check the results. Yes, just copy others' codes. During copying, you will gradually understand the logic behind it. Don't just copy and paste, actually type all the code by yourself.

### know well the function "print()"

## step 2: Data structure and loop

### set up Python environment

### Data structure

- list: list slice
- array: array slice, multi-dimension arrays
- dictionary: easy to use, not important
- string: the most hard part, please learn how to use regular expression.

### if...else...

### for loop

### function

### the common mistakes

- The common mistakes here is the indent, which affect the scope of a loop. It is easy to make a loop run forever by a mistaken indent.
- Get confused by the scope of variables outside a function and inside a function.

### the hard part

- string is hard to master at this stage. this part include lots of manipulation of string, which is quite common in daily work.

## step 3: the three founding pillars of Python

At this section, please read the book, "Python for Data Analysis".

### Numpy

#### material to read

### Pandas

#### material to read

### Matplotlib

#### material to read

## step 4: getting serious about programming

### Find a handy IDE

- Jupyter Notebook
   Everybody uses it.

- Pycharm
  Very good ide but it can easily slow down my i7 workstation

- Vscode
  Lightweight, but powerful. recommend

- Emacs
  The only drawback of Emacs is too much power. It is such a powerful editor that people find it hard to handle. We only want to drive a car to New York, it gives us an airplane. It will take 5 years to learn to fly, but we only need 5 months to learn driving a car.

### Good habits for coding

#### 1. Before writing code, write down the plan in words/sentences (e.g., algorithm)
A code snippet or a big applications can be divided into small pieces with each piece realzing a small function. Like lego, put the small pieces together.

- First, write down the goal
- Second, draw a flow chart of how to realize it
- Third, identify the function to be realized.

You do not need to realized all the functions at once. Instead, you can pretend others are finished, just focus on one function each time and test each function when finished. 
Then put them together.

#### 2. When you write your code, write down what you thought, what needs to be done.

Put some TODO label in the code when you write the code. Some important ideas come when you actuall write code.
#### 3. Add code headers to show the authors, date created, purpose the code, variables, notes, copy right, coding (UTF-8) etc.
#### 4. Add annotations for all the variables (type), functions (input, output), classes
#### 5. Code body needs to include the following
##### 5.1 Progress bar or time estimation for a function needs lots of time
##### 5.2 Design the error capture (Try )
##### 5.3 Speed up the procedure by parallel the function like multiprocessing
##### 5.4 Setup log files
##### 5.5 Check the vulnerability or rubustness of the code by designing all the possible test data.
##### 5.6 Use "Assert" to do testing or other methods for testing.

#### 6. When some results need to be saved.
##### 6.1 Always has a timestamp for the results. Otherwise, the saved results can be overided when run the code multiple times.
##### 6.2 Give a consistent name for the file. It is good to include to include some global variables to the name.
##### 6.3 Put the results in an organized folder.

### Get familiar with common modules

#### sys

#### re

#### os

## step 5: Building block accumulation

Programming is like building Legos. You have lots of building units and use them to make a castle, car or anything you think is cool. But the building units are the same. Programming follows the same logic. So what's the building unit for Python programming? 

The bulding blocks are the samll functions to realize something specific. For example, we need to get a list of files with their absolute paths. We will create a simple function to realize it or you find it on Overflow. Write it down as your reference in the future. You need to come back to review it and make it better when you need it in your projects.

A good starting point is to read a book, "Python Cookbook" and digest it and take your notes for future use.

## step 6: Objecte Oriented Programming

I found this part is the hardest one. People get scared away by the strange names like, self, __init__, etc.


### basic rules

### magic functions

## step 7: specialized areas

### Data Science

### Computer Vision

### Machine Learning

## step 8: ramp up a package

### Documentation Tools

### Logging

### Testing
