gpa = float(input('What is your GPA: '))
lowest_grade = float(input('What is your LowestGrade: '))

if gpa >= 0.85 and lowest_grade >= 0.70:
    honour_roll = True
else:
    honour_roll = False
    

if honour_roll: 
    print('Well Done')