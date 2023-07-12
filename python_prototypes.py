# Input the temperatures for each day
temperatures = []
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    temp = float(input("Enter the temperature for " + day + ": "))
    temperatures.append(temp)

# Calculate the average temperature
average_temperature = sum(temperatures) / len(temperatures)

# Print the average temperature
print("Average temperature of the week:", average_temperature)
