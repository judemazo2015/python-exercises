people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading', 'hiking']
]

ppl_with_shared_hobbies  = {
    person: [
        name for hobs, name in zip(hobbies,people)
        for hob in hobs
        if hob in set_hobs and name!=person
        ]
    for person, set_hobs in zip(people,hobbies)
}

for i in ppl_with_shared_hobbies:
    ppl_with_shared_hobbies[i] = list(set(ppl_with_shared_hobbies[i]))

print(ppl_with_shared_hobbies)