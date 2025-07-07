def collapse_all(text, collapsed):
    if text == '':
        return ''
    return (
        text[0] + collapse_all(text[1:], collapsed+text[0]) 
        if text[0] not in collapsed 
        else collapse_all(text[1:], collapsed)
    )

res = (
    collapse_all("banana",''),        # → "ban"
    collapse_all("abracadabra",''),   # → "abrcd"
    collapse_all("hello",''),         # → "helo"
    collapse_all("a",''),             # → "a"
    collapse_all("",''),              # → ""
)
print(*res, sep='\n')
