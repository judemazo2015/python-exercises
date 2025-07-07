def longest_streak(data):
    streaks = []
    
    m = 0
    while m < len(data):
        streak = []
        for i in range(m, len(data)):
            if data[i] not in streak and streak != []:
                m = i
                break
            streak.append(data[i])
        else:
            m = len(data)            
        streaks.append(streak)

    return streaks

sales = ["apple", "apple", "banana", "banana", "banana", "apple", "apple", "apple", "apple", "grape", "grape"]
print(longest_streak(sales))