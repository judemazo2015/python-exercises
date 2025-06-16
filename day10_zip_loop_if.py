students = ['Ana', 'Ben', 'Cara', 'Dan']
grades = [85, 58, 92, 45]

for s,g in zip(students, grades):
    if g>=60:
        print(s)