#Lis of steps during the week
days = ["Monay", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []
for day in days:
    user_input = input(f"How many steps did you take on {day}? ")
    steps.append(int(user_input))
print("\nSteps recorded for each day:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")
total_steps = sum(steps)
print(f"\nTotal steps taken in the week: {total_steps}")
average = round(total_steps / len(steps))
print(f"Average steps taken per day: {average}")
