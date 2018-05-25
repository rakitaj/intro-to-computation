class Recursive():
        
    # Recursive implementation of factorial
    @staticmethod
    def factorial(n: int) -> int:
        if n == 1:
            return 1
        else:
            return n * Recursive.factorial(n - 1)

class Iterative():
    
    # Iterative implementation of factorial
    @staticmethod
    def factorial(n: int) -> int:
        result = n
        for i in range(n - 1, 1):
            result = result * n
        return result
