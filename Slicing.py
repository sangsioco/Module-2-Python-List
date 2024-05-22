temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1: Extract temperatures for the second week

second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:", second_week_temperatures)

# Task 2: Extract all temperatures above 100

temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", temperatures_above_100)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list

reversed_temperatures = temperatures[::-1]
reversed_slice = reversed_temperatures[4:10]
print("Temperatures from the 5th to the 10th day of the reversed list:", reversed_slice)