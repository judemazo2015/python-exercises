def get_sales(data):
    seen = set()
    return {item: data.count(item) for item in data if not (item in seen or seen.add(item))}

print(get_sales([
        "apple", "banana", "apple", "orange", "banana", "apple", 
        "banana", "banana", "grape", "orange", "apple"
        ]
    ))