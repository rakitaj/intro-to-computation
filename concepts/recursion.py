class Recursive():
        
    @staticmethod
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * Recursive.factorial(n - 1)

    @staticmethod
    def fibonacci(n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return Recursive.fibonacci(n - 1) + Recursive.fibonacci(n - 2)

class Iterative():
    
    @staticmethod
    def factorial(n: int) -> int:
        result = 1
        for i in range(n, 0, -1):
            result = result * i
        return result
