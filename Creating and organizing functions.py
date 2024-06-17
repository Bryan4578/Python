def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    result = factorial(number)
    print(f"The factorial of {number} is {result}.")

main()
