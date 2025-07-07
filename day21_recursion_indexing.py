def get_sum(digit, sum, i):
    if i == len(str(digit)):
        return sum
    sum += int(str(digit)[i])
    i+=1
    return get_sum(digit, sum, i)

print(get_sum(1234, 0, 0))