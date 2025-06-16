students = [
    ['Alice', 92],
    ['Bob', 85],
    ['Charlie', 78],
    ['David', 88],
    ['Eva', 91],
    ['Frank', 67],
    ['Grace', 88],
    ['Helen', 85],
    ['Isaac', 78],
    ['Jack', 92]
]

names, grades = zip(*students)

groupings = {}

for name, grade in zip(names, grades):
    grade = 'A' if grade>=90 else 'B' if grade>=80 else 'C' if grade>=70 else 'D'    
    if grade in groupings:
        groupings[grade].append(name)
    else:
        groupings[grade] = [name]

results = {grade:name for grade, name in groupings.items()}

print(groupings)