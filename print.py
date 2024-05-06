def factorial(n):
    if n == 0:
        return 1
    elif not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

while True:
    try:
        n = int(input("Type N: "))
        result = factorial(n)
        print(f"Factorial {n} is {result}")
        break
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        break3