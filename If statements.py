age = int(input("Please enter your age: "))

# Check if they are old enough to vote,drive,buy alchohol,and recive a senior discount
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")
if age >= 18:
    print("You are old enough to Vote.")
else:
    print("You are not old enough to Vote.")  
if age >= 21:
    print("You are old enough to buy alcohol.")
else:
    print("You are not old enough to buy alcohol.")  
if age >= 65:
    print("You are old enough for a senior discount.")
else:
    print("You are not old enough for a discount.")       