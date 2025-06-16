users = [
    ['alice@gmail.com', 'Alice'],
    ['bob@yahoo.com', 'Bob'],
    ['alice@gmail.com', 'Alicia'],
    ['dave@outlook.com', 'Dave'],
    ['bob@yahoo.com', 'Robert']
]

emails, names = zip(*users)

email_dicts = {}
for email, name in zip(emails, names):
    if email in email_dicts:
        email_dicts[email].append(name)
    else:
        email_dicts[email] = [name]

result = {email: names for email, names in email_dicts.items() if len(names) > 1}

print(result)
