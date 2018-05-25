class Recursive():
        
    # Recursive implementation of factorial
    @staticmethod
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * Recursive.factorial(n - 1)

class Iterative():
    
    # Iterative implementation of factorial
    @staticmethod
    def factorial(n: int) -> int:
        result = 1
        for i in range(n, 0, -1):
            result = result * i
        return result
