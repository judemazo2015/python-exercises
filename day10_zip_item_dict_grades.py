students = [
    ['Alice', 85],
    ['Bob', 91],
    ['Charlie', 85],
    ['David', 72],
    ['Eva', 91],
    ['Frank', 72],
    ['Grace', 88]
]

names, grades = zip(*students)
grades_dict = {}

for grade, name in zip(grades, names):
    if grade in grades_dict:
        grades_dict[grade].append(name)
    else:
        grades_dict[grade] = [name]

final_dict = {grade:name for grade, name in grades_dict.items()}

print(final_dict)
