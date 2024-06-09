# Heart Rate Tracker 
time_slots = ["Morning", "Miday", "Afternoon", "Evening"]
heart_rates = []
for time in time_slots:
    heart_rate = int(input(f"Enter your heart rate for {time} (BPM): "))
    heart_rates.append([time, heart_rate])
total_heart_rate = 0
for heart_rate in heart_rates:
    total_heart_rate += heart_rate[1]
average_heart_rate = total_heart_rate / len(heart_rates)
print("\nAverage heart rate:", average_heart_rate)
