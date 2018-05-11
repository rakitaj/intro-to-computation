# Class 03

# Exercises
## Exercise 1
Let *s* be a string of decimals separated by commas like
```python
s = "1.23,4.56,7.89"
```
Write a program to total up the sum of the decimal numbers

## Exercise 2
Write a function that returns a boolean indicating if an integer is an even number. This typically requires the use of the modulo operator.  
[Python v3.6 documentation on modulo](https://docs.python.org/3.6/reference/expressions.html)
[Stack overflow answer about % aka modulo in Python](https://stackoverflow.com/questions/4432208/how-does-work-in-python)
```python
def is_even(n: int) -> bool:
    # Your code here
```

## Exercise 3
Write a function that returns a boolean indicating if an integer is a prime number or net.
```python
def is_prime(n: int) -> bool:
    # Your code here
```

## Exercise 4 - Harder
Optimize the function you generated for exercise 3. Good places to start are
1. For my target number do I need to check it against every number?
2. For my target number is there a limit after which I can stop checking?
3. What algorithms can I use to determine primality? Feel free to research online, like you would for an issue while working :)