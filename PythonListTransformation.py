# Task 1: Sort the grades in descending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Task 2: Calculate the average grade

average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# Task 3: Replace grades below 80 with "Failed"

processed_grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Processed grades:", processed_grades)

