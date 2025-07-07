people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading', 'hiking']
]

ppl_sharing = {}
for person, set_hobs in zip(people,hobbies):
    ppl_sharing[person] = []
    for hob in set_hobs:
        for i in range(len(people)):
            if hob in hobbies[i] and people[i]!=person and people[i] not in ppl_sharing[person]:
                ppl_sharing[person].append(people[i])

print(ppl_sharing)
        