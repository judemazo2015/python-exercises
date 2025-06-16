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

highest_students = {}

for n, g in zip(names, grades):
    score = g
    g = 'A' if g >= 90 else 'B' if g >= 80 else 'C' if g >= 70 else 'D'
    if g in highest_students:
        highest_students[g].append((n,score))
    else:
        highest_students[g] =  [(n,score)]

results = {
    grade: max(name, key=lambda index: (index[1], sum(ord(char) for char in index[0])))[0]
    for grade, name in highest_students.items()
}

print(results)