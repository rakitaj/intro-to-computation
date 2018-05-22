# Class 01
Functions are the building blocks of abstraction, and abstraction is key to building a good program. When you call print("My name is John") you don't care how that string gets printed, you only care about it working.

# Exercises
## Exercise 1
1. Write a function that squares the number you pass in.
2. Write a function that cubes the number you paass in.

What would happen if a function called **def square(x)** actually added one to the number and returned it?

## Exercise 2
1. Write a function that sums up all of its parameters
2. Write a function that concatenates all of its string parameters

## Exercise 3 - Harder
Is there a way you can generalize the functions from exercise 2 while making sure they each have a name specific to their function? Ex:
```python
def sum_integers(a, b, c, d):
    pass

def concatenate_strings(a, b, c, d):
    pass
```