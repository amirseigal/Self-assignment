def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"{n}! = {factorial(n)}")
