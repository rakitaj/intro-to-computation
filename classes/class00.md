# Class 00

## Goal of this course
We're here to learn the fundamentals of computer science and software development. I say computer science and software development because in my mind they are two different pursuits. 

Computer science is the study of what computers can do, it includes topics like complexity analysis, algorithms, data structures. It can include programming language study and design, compiler construction, and many other topics not directly relevant or applicable to work a professional programmers does.

Software development is problem solving using a programming language. It's the gettings things done part of the equation. Debugging, testing, test driven development, refactoring, dependency management, and using your tools well are all software development skills.

## Is this the course for you?
This course is for someone who either wants to learn computer science basics and how to program or someone who has been out of school for a long enough time to want a refresher that starts at the very beginning. If you're an experienced programmer it might be too slow paced for you, especially at the beginning.

## Dev environment setup
Look at the README.md in the root of the repository. Section **Dev environment setup**

## What did I just do?
At a very high level, you installed Python, created a virtual environment for Python in a certain location, and then installed all of the course's dependencies into that location.

Using venv to create a virtual environment, and pip to install packages from a requirements file might feel a little overwhelming at first, and it is, but part of software development is knowing your operating system, your environment, and your programming language and its tools. All of this combined knowledge is what we need to actually do our job.

### What is venv?
Venv is a tool which create an independent Python installation, along with all of its included code, in the directory you specify. This makes it easy for different Python projects to have their own set of packages, and not interfere with each other.

If you didn't use a virtual environment of some sort, the packages get installed to the global instance of Python. Being installed in the global instance of Python makes it much harder to have multiple projects on the same machine. It's a good practice to use a separate virtual environment for each project.

### What is requirements.txt?
This is a list of all the packages you need without versions specified. It's convenient because with one command *pip install -r requirements.txt* you can install all packages at the same time. If this list is kept up to date it makes new developers setup for the project much easier. Explicit dependencies and they are all in one place.

### What are mypy and pylint?
They are tools to help you write bug-free and correct Python. Look up more information on their websites if interested.

### What is pytest?
Pytest is our unit testing framework of choice. It makes test writing easy with auto discovery of tests that conform to a naming pattern, and it uses the included assert statement.

If you're ambitious, you can start writing tests now or if you want to wait testing is covered in depth in class 6.

# Exercises
## Exercise 1
Print "Hello, world!" to the console.
