# Class 2
With functions and conditions covered we can build many different programs. Some might be harder if we stay away from using typical programming constructs like while loops, for loops, and objects but they're all doable. 

The key is recognizing you can use recursion, which is a function calling itself, to loop like a while loop. Some problems can also be solved in their own unique way using recursion.

Check out **class02.py** for two runnable examples.

Many constructs in programming languages exist to solely make your life easier. If you really had to, you could pass around numbers and strings one parameter at a time and achieve your end goal with functions and if/else statements.

# Exercises
## Exercise 1
1. Write a function that counts down from n to 0 and prints the number it's on as it goes, stopping at 0. Do not using a while or for loop.
2. Write another function that counts from 0 up to n, stopping at n.

## Exercise 2
Write a function that returns the sum of all numbers between 0 and n.
Hint: This function needs an accumulator parameter in addition to n.
```python
def sum(n: int, total: int) -> int:
    # Your code here
```

## Exercise 3 - Harder
Write a function that computes the Fibonacci number for n.
[Wikipedia Fibonacci article](https://en.wikipedia.org/wiki/Fibonacci_number)