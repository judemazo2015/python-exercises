def collapse_first_repeat(text):
    if text == '':
        return ''
    def helper(i, excluded):
        if i == len(text):
            return ''
        if excluded == None and text.count(text[i]) > 1:
            return helper(i, i)
        if i != excluded:
            return text[i] + helper(i+1,excluded)
        else:
            return ''+ helper(i+1,excluded)
    return helper(0,None)


res = (
    collapse_first_repeat("banana"),
    collapse_first_repeat("hello"),
    collapse_first_repeat("abcde"),
    collapse_first_repeat("aabbcc"),
    collapse_first_repeat("a"),
    collapse_first_repeat(""),
)
print(*res, sep='\n')