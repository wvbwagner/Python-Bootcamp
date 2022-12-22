student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

def checkGrades(value):
    if value <= 70:
        grade = 'Fail'
    elif value <= 80:
        grade = 'Acceptable'
    elif value <= 90:
        grade = 'Exceeds Expectations'
    else:
        grade = 'Outstanding'
    return grade

for names, grades in student_scores.items():
    student_grades[names] = checkGrades(grades)

print(student_grades)