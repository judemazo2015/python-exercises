def is_mirrored(matrix):
    temp=[]
    for row in matrix:
        if (
            ("".join([row[j] for j in range(len(row)//2)])) !=
              ("".join([row[j] for j in range(len(row)//2, len(row))]))[::-1]
        ):
            return False
    return True

print(is_mirrored([
        ['a', 'b', 'b', 'a'],
        ['c', 'd', 'd', 'c'],
        ['x', 'y', 'y', 'x'],
        ['m', 'n', 'n', 'm']
        ]
    ))

print(is_mirrored([
        ['a', 'b', 'c', 'a'],
        ['c', 'd', 'd', 'c'],
        ['x', 'y', 'z', 'x'],
        ['m', 'n', 'n', 'm']
        ]
    ))