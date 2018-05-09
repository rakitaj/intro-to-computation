def countdown_recursion(n: int) -> None:
    if n >= 0:
        print(n)
        countdown_recursion(n - 1)

# While loop
def countdown_while(n: int) -> None:
    while n >= 0:
        print(n)
        n = n - 1

print("Begin recursoin")
countdown_recursion(5)

print("Begin while")
countdown_while(5)