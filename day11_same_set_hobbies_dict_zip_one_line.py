people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading', 'hiking']
]

hobs_dict ={tuple(sorted(hobs)):[person for group_hobs, person in zip(hobbies,people) if (tuple(sorted(hobs)) == tuple(sorted(group_hobs)))] for hobs in hobbies}


print(hobs_dict)