def flatten_list(data):
    nums = []
    
    while data:
        if isinstance(data[0], list):
            for el in data.pop(0)[::-1]:
                data.insert(0,el)
        else:
            nums.append(data.pop(0))
    return nums

nested = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(nested))