XV: Overview of what you will have when finished with this book

# 1: Getting started
Declarative knowledge vs imperative knowledge -> How to vs fact
Algorithm -> Steps with control flow
Computation -> 
Fixed program computer -> Has the same program all the time, can operate on different data
Stored program computer -> The heart of the machine is an interpreter, can execute valid instructions
Turing machines -> Turing completeness -> All programming languages which are turing complete are equivilant on a fundamental level
Syntax -> The language and order of keywords, primatives, literals, and any other parts of the programming language
Static syntax -> As far as I can tell static analysis of the program. Can be static typing, linter, or other type of code analysis
Semantics -> The meaning of the program, what it will do

# 2: Introduction to Python
Python is a high level, general purpose, interpreted language
Don't focus on Python, focus on the concepts, the specific language isn't important.
Expressions evaluate to values.

Understand variables, assignment, and the order of evaluation aka the order of operations.

IDE -> Integrated Development Environment -> A text editor which helps you write code. It has extra features like syntax highlighting, debugging, and sometimes code completion built in.

You can use any **text manipulation** program to write Python. Some are better than others. IDLE is an IDE which is included, Visual Studio Code with the Python extension is also great.

Branching is a fundamental concept of writing and reading/understanding code. You'll see it as an if/else statement.

Type checking in Python is weaker than in a statically typed language like Java but it's still there. 
For example 
``` python
if 5 < "three"
# throws type exception - you can't compare an int and a string
```

Character encoding is tricky, Unicode is a worldwide standard and can have different internal character encodings. UTF-8 is the standard one used in Python unless instructed otherwise.

Iteration can be achieved with a while loop. A for loop is really a different way of expressing this same concept.
```python
josh_coffee_limit = 5
while josh_coffee_limit > 0:
    buy_josh_a_coffee()
    josh_coffee_limit = josh_coffee_limit - 1
```

# 3: Some Simple Numerical Programs
If looking for the answer using exhaustive enumeration, make sure the program will terminate for a given input.

Exhaustive enumeration is also known as brute force.

# Python cheat sheet
**In Python whitespace is important!! It's part of the syntax. Bad whitespace can and will cause a program to not execute.**

Get the type of the object.
```python
type(5)
<type 'int'>
```

