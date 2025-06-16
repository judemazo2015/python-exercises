names = ['Zoe', 'Alice', 'John']
scores = [70, 95, 88]

players = sorted(list(zip(names,scores)), key=lambda index: index[1], reverse=True)

print(players)