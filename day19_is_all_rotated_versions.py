def is_all_rotation(matrix):
    rotations = get_rotations(matrix)
    for row in matrix[1:]:
        if "".join(row) not in rotations:
            return False
    return True

def get_rotations(matrix):
    first, size = matrix[0], len(matrix[0])
    rotations = []
    for _ in range(size):
        temp = first[0]
        for i in range(size):
            first[i] = first[i+1] if i < size-1 else ""
        first[-1] = temp
        rotations.append("".join(first))  
    return rotations

print(is_all_rotation([
        ['a', 'b', 'c', 'd'],
        ['c', 'd', 'a', 'b'],
        ['d', 'a', 'b', 'c']
        ]
    ))

print(is_all_rotation([
        ['x', 'y', 'z'],
        ['z', 'x', 'y'],
        ['y', 'x', 'z']
        ]
    ))