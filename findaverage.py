# find average marks
def find_average_marks(marks_list):
    sum_of_marks = sum(marks_list)
    total_subjects = len(marks_list)
    average_marks = sum_of_marks / total_subjects
    return average_marks


# calculate grade
def find_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'Failed'
    return grade


marks = [55, 64, 73, 84, 91]
student_average_marks = find_average_marks(marks)
print("average marks ", student_average_marks)

your_grade = find_grade(student_average_marks)
print("Your grade is: ", your_grade)
