def collapse_first_repeat(text, first_checked):
    if text == '':
        return ''
    if text.count(text[0]) > 1 and first_checked == False:
        return ''+ collapse_first_repeat(text[1:], True)
    return text[0] + collapse_first_repeat(text[1:],first_checked)

res = (
    collapse_first_repeat("banana",False),
    collapse_first_repeat("hello",False),
    collapse_first_repeat("abcde",False),
    collapse_first_repeat("aabbcc",False),
    collapse_first_repeat("a",False),
    collapse_first_repeat("",False),
)
print(*res, sep='\n')