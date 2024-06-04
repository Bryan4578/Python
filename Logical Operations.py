#Have user input a number 
number1 = int(input("Please enter a number"))
number2 = int(input("please enter a second number"))
#And examples
if number1 > 0 and number2 > 0:
    print("Both numbers are greater than 0: True")
else:
    print("Both numbers are greater than 0: False")
if number1 > 100 and number2 > 100:
    print("Bothe numbers are greater than 100: True")
else:
    print("Both numbers are greater than 100: False")  
# Or example 
if number1 % 2 == 0 or number2 % 2 == 0:
    print("At least one of the numbers is even.")
else:
    print("Neither of the numbers are even.")
if number1 > 100 or number2 > 100:
    print("One of the numbers is greater than 100")
#Not example
if not number1 > 0:
    print("number1 is not greater than 0")
else:
    print("number1 is greater than 0")
number1 = number1
number2 = number2
result = not (number1 == number2)
print("number1 is equal to number2",  result)


