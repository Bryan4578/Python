# constants
POUND_TO_KG = 0.453592
INCH_TO_METER = 0.0254

# calculate BMI
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    return bmi

# Main function 
def main():
    #user input for weight
    while True:
        try:
            weight_pounds = float(input("Enter your weight in pounds: "))
            if weight_pounds <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number for weight.")

    #user input for height
    while True:
        try:
            height_inches = float(input("Enter your height in inches: "))
            if height_inches <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number for height.")

    #weight to kilograms
    weight_kg = weight_pounds * POUND_TO_KG
    #height to meters
    height_m = height_inches * INCH_TO_METER

    # BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # results
    print(f"Your BMI is {bmi:.2f}.")
    print(f"You are categorized as: {category}.")

# Run the main function
main()
