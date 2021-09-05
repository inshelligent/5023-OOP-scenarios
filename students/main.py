import grades

studList = []

# TODO: Change this code to create a Student object, rather than dictionary
michael = grades.Student('Michael',80,70,70,True)
print('id(michael):',id(michael))
studList.append(michael)

# Creates a dictionary for a student named Angela
# TODO: Change this code to create a Student object, rather than dictionary
angela = grades.Student('Angela',60,65,75,True)
print('id(angela):',id(angela))
# Adds the dictionary for Angela to the students list
studList.append(angela)

# Creates a dictionary for a student named Natalie
# TODO: Change this code to create a Student object, rather than dictionary
natalie = grades.Student('Natalie',60,65,75,False)
print('id(natalie):',id(natalie))
# Adds the dictionary for Natalie to the students list
studList.append(natalie)

# Print the names and marks for each of the students
print('\nStudents:\n')
# TODO: Change code in loop to access Student objects' attributes, rather than dictionary
for student in studList:
    print('---')
    print(f"Name: {student.name}")
    print(f"English: { student.english_mark }")
    print(f"Science: { student.science_mark }")
    print(f"Mathematics: { student.mathematics_mark }")
    if student.completed_assessments:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print(f"Average: {student.average_mark()}")
    print('---\n')







