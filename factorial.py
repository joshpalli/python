def factorial(n):
    if n < 0:
        return None # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        return result
    
def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        result = factorial(n)
        if result is None:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {n} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()