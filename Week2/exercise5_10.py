# Find the highest score
# Author: Brian Hamburg

# get number of students
students = eval(input("Enter the number of students: "))

# get first student's name and score
currentStudent = input("Enter a student name: ")
currentScore = eval(input("Enter a student score: "))

# loop through all the students' names and scores
for i in range(students - 1):
    student = input("Enter a student name: ")
    score = eval(input("Enter a student score: ")) 

    if score > currentScore:
        currentStudent = student
        currentScore = score

# print result
print(currentStudent + " had the highest score with " + str(currentScore))
