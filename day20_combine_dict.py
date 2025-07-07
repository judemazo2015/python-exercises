def combine_dict(d1,d2):
    return {key:(d1[key]+value) if key in d1 else value for key, value in (d1|d2).items()}

d1 = {'a': 3, 'b': 2, 'c': 1}
d2 = {'a': 4, 'b': 1, 'd': 5}

print(combine_dict(d1,d2))
