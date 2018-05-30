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

The method a computer uses to find an answer can be very different from what we would do if we had to calculate it by hand.

For the calculate square root programs, brute force works at first and then we need to refine our algorithm. A fast processor can't overcome an algorithm that isn't suited for the job.

Binary numbers don't map 1 to 1 to decimal numbers. Thinking in decimal and working with binary numbers can cause issues. For example try:
```python
.1 + .2 == .3
```
Python uses an internal repreesntation called floating point to represent not integer numbers.

## Floating point
Think of floating point as a pair of numbers. The first is the significant digits of the number (like chemistry if that analogy helps) and the second is the exponent multiplier.

From the book an example in the decimal system (not binary) is the number **1.949** It can be represented by **(1949, -3)** which expands to **1949 x 10^-3** and is equal to **1.949**. If this number had 2 signifigant digits it would be **(19, -1)** would expand to **19 * 10^-1** and be equal to 1.9

It's harded to figure out the binary equivilant. 

## Polynomials
The degree is the exponent, the degree of the polynomial is the largest exponent.
Newton-Raphson aka Newton's method 

# 4: Functions, scoping, and abstraction
Functions allow us to change our programs from long sequences of instructions to small pieces of reusable and composable code. Along with if/else statements and while/for loops they are the fundamental building blocks of programs.

Scoping is what allows us to call a function times with different values for the parameters. The parameters we call a function with have their values bound to that instance of the function so you can call the same function with a different set of values.

Python has lexical scoping which is "the meaning of an unqualified name can be completely determined by looking at the program text." In short, by reading the program and knowing its scoping rules you can determine the which variables a function will rely on.

## Specifications
Writing code which tests your *program code* is important. Over the long run it's faster than typing test cases into the Python prompt over and over, and it forces you to formalize your program by writing down test cases which it must pass. The act of writing test cases can make you consider edge cases and how you want your program to behave in response to certain imputs.

Functions provide decomposition and abstraction.
- **Decomposition** - Functions which are small and may be repeated used, or reused in other places.
- **Abstraction** - Hides detail, allows us to use a function as if it were a black box. After we write (and test) **def square(x):** we don't need to worry about or remember the implementation. This frees our mind to work on other problems. The abstraction has to be useful to both the creator and user.

## Recursion
For a recursive function there is a base case and the recursive case. You can have as many base cases as you need. For example in the Fibonacci sequence there are two.

Great quote from the book about prblem solving and writing code
> Once we went from the vague statement of a problem about bunnies to a set of recursive equations, the code almost wrote itself. Finding some kind of abstract way to express a solution to the problem at hand is very often the hardest step in building a useful program.

## Global variables
Global variables are helpful when you need to communicate outside of a function or class, or span many of them. Examples of this are keeping track of the number of times a function has executed, or the classic example of a logger.

The issue with global variables is that anything can change their values, the changes are not limited to the scope of the code you're looking at. A new team being used for this is non-local reasoning, meaning you need to understand what is happening in another part of the codebase which is potentially unrelated to the one you are looking at.

---

A module is another python file, it's a good way of organizing code. Each module has its scope, it can contains functions and classes with, potentially, the same name as your own file. Keep this in mind and be careful about importing everything from a module .

Python provides a built-in set of function to open, read, and write files. Remember to close a file when finished writing to it.

# 5: Structured types, mutability, and higher-order functions
*int* and *float* are scalar types. A scalar type is one that has no accessible internal structure. In comparison, str is a structured (non-scalar) type. 

Know the difference between typle, dictionary, list, and range (which is an enumeration). One cool thing about Python is a for statement can be used to iterate over these objects.

Lists are mutable, tuples are immutable.

Range is the trickiest, it's for a sequence of integers like [1, 2, 3, 4, ...] it can count "backwards" as well as in increments different from 1.

Multiple assignment can bind multiple variables to a function that returns multiple values. The amount of values returned needs to be known ahead of time.
```python
def x_and_y():
    return (3, 4)

x, y = x_and_y()
# x = 3 and y = 4
```

Value vs object equality is tricky, object equality tests to see if an object is in the same location of memory.

Don't mutate (add/remote/change) values in a list in a loop. The internal pointer keeping track of the index in the list can end up being too far ahead or behind.

## Functions as objects
Functions can be passed as a parameter just like any other object or value. When using a function as an argument it's a style of coding called **higher-order programming**.

Take a look at the Python built-in function map for an easy way to apply a function to all elements of a collection.

## Lambdas
A lambda function is a function that is not bound to a name.
```python
lambda x, y: x + y
# Returns the sum of both x and y.
```
---

Dictionaries, or dicts for short, are incredibly useful unordered sets of key/value pairs. You index into them using a key value instead of a positional index.

Each key maps to a value. The lookup time is what makes dicts unique, it takes a constant amount of time to get the value for any key, unlike a list where you might need to traverse the whole thing to find a value at the end.

# 6: Testing and debugging
**Testing** - Running a program to determine if it is behaving like you expect
**Debugging** - Fixing a program you know is not running correctly



# Python cheat sheet
**In Python whitespace is important!! It's part of the syntax. Bad whitespace can and will cause a program to not execute.**

Get the type of the object.
```python
type(5)
<type 'int'>
```

For loops using the range(start, stop) statement have a default step of 1. You can change this by using the range(start, stop, step) statement.
