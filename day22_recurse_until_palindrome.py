def add_until_palindrome(num):
    if str(num) == str(num)[::-1]:
        return num
    return add_until_palindrome(num + int(str(num)[::-1]))


results = (
    add_until_palindrome(56),   #121
    add_until_palindrome(57),   #363
    add_until_palindrome(1),    #1
    add_until_palindrome(89),   #8813200023188
)

print(*results, sep='\n')
