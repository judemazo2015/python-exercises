a = [2, 4, 6]
b = [5, 3, 1]

products = [a*b for a,b in zip(a,b)]
print(products)