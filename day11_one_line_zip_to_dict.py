people = ['Alice', 'Bob', 'Charlie', 'David']
hobbies = [
    ['reading', 'gaming', 'hiking', 'golf'],
    ['gaming', 'cooking'],
    ['reading', 'chess'],
    ['gaming', 'reading']
]

print({h[0]:list(set(name for hobs, name in zip(hobbies,people) for hob in hobs if h[0] == hob[0])) for hobs, _ in zip(hobbies, people) for h in hobs}) 