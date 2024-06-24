
def calculate_square():
    while True:
        try:
            
            number = float(input("Please enter a number: "))
            
            square = number * number
            
            print(f"The square of {number} is {square}.")
            break
        except ValueError:
            
            print("Invalid input! Please enter a valid number.")

def main():
    calculate_square()

if __name__ == "__main__":
    main()
