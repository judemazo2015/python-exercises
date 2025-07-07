people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading', 'hiking']
]

hobs_dict = {}
for hobs, person in zip(hobbies,people):
    tuple_key = tuple(sorted(hobs))
    if tuple_key in hobs_dict:
        hobs_dict[tuple_key].append(person)
    else:
        hobs_dict[tuple_key] = [person]

print(hobs_dict)