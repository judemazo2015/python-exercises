def even_palindrome(num):
    sum = num + int(str(num)[::-1])
    if str(sum)==str(sum)[::-1] and all(int(d)%2 == 0 for d in str(sum)):
        return sum
    else:
        return even_palindrome(sum)
    

results = (
    even_palindrome(28),
    even_palindrome(12),
    even_palindrome(1), 
)

print(*results, sep='\n')
