people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading']
]

hobs = {}

for name, hob in zip(people, hobbies):
    for h in hob:
        if h in hobs:
            hobs[h].append(name)
        else:
             hobs[h] = [name]
names = [name for _,names in hobs.items() for name in names]
results = {hob:stud for hob, stud in hobs.items() if any(names.count(s)>1 for s in stud) and len(stud)>1}

print(results)
