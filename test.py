
students = ['Andrew', 'Bobby', 'Charlie', 'David', 'Eve']

grades = {
    'Andrew': 85,
    'Bobby': 45,
    'Charlie': 70,
    'David': 38,
    'Eve': 90
}



for student in students:
    grade = grades.get(student)
    print(grade)
    if grade <= 50:
        print(f'{student} passed with a grade of {grade}.')
    else:
        print(f'{student} failed with a grade of {grade}.')