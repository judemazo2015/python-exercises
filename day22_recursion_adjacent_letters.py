def remove_adjacent(text):

    if text == '':
            return ''
    def helper(i):
        if i >= len(text)-1:
            return text[i]
        return text[i] + helper(i+1) if text[i] != text[i+1] else helper(i+1)
    return helper(0)

res = (
remove_adjacent("aabbcc"),
remove_adjacent("bookkeeper"),
remove_adjacent("mississippi"),
remove_adjacent("a"),
remove_adjacent("")
)
print(*res, sep='\n')   