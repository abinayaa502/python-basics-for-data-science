subjects = ["Python", "AI", "Data Science", "Maths"]

print("Subjects:")
for subject in subjects:
    print("-", subject)
  
subjects.append("Machine Learning")
print("\nAfter adding a subject:", subjects)

subjects.remove("Maths")
print("\nAfter removing a subject:", subjects)

print("\nFirst subject:", subjects[0])
print("Last subject:", subjects[-1])
