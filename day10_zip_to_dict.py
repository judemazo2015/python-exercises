keys = ['name', 'age', 'city']
values = ['Alice', 30, 'Manila']
zipped = list(zip(keys,values))

person = dict(zipped)

print(person)