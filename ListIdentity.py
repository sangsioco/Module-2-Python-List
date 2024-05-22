# Task 1: Find students who both submitted their assignments and attended the class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_submitted_and_attended = list(set(submitted) & set(attended))
print("Students who both submitted and attended:", both_submitted_and_attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order

are_identical = set(submitted) == set(attended)
print("The two lists are identical in content:", are_identical)

# Task 3: Remove any student from the attended list who did not submit their assignment

attended_only_submitted = [student for student in attended if student in submitted]
print("Attended list after removing non-submitters:", attended_only_submitted)