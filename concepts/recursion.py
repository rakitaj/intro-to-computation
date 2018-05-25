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

    @staticmethod
    def palindrome(string: str) -> bool:
        if len(string) <= 1:
            return True
        else:
            if string[0] == string[-1]:
                return Recursive.palindrome(string[1:-1])
            else:
                return False

class Iterative():
    
    @staticmethod
    def factorial(n: int) -> int:
        result = 1
        for i in range(n, 0, -1):
            result = result * i
        return result
