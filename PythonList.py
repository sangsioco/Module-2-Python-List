# Task 1: Filter out students with grades below 80 and print their details

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i] < 80:
        print(f'{students[i]}, {grades[i]}, {activities[i]}')

# Task 2: Add remaining students' names to a new list named students_approved

students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        students_approved.append(students[i])

# Task 3: Print the list students_approved

print("students_approved:", students_approved)