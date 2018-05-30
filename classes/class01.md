# Class 01
Functions are the building blocks of abstraction, and abstraction is key to building a good program. It allows you to "black box" parts of your program, which makes it easier to reason and think about. 

When you call print("My name is John") you don't care how that string gets printed, you only care about it working. Or when you write email.is_valid() you don't need to know all of the rules and checks it's doing, you only need to know if the email passes or not.

As we learn more about Python, think about how your new skills can be used to write easy to understand, and easy to change code.

# Exercises
## Exercise 1
1. Write a function that squares the number you pass in.
2. Write a function that cubes the number you pass in.

What would happen if a function called **def square(x)** actually added one to the number and returned it?

## Exercise 2
1. Write a function that returns the sum of its parameters
2. Write a function that concatenates all of its string parameters

## Exercise 3 - Harder
Is there a way you can generalize the functions from exercise 2 while making sure they each have a name specific to their function?

Can you test them?

Ex:
```python
def sum_integers(a, b, c, d):
    pass

def concatenate_strings(a, b, c, d):
    pass
```