import re

def main():
    text = """
        <section>Introduction</section>
        <section>Background</section>
        <section>Conclusion</section>
    """
    print(subbed(text))

def subbed(text):

    i = [0]
    return re.sub(r'(<section)>',lambda m: m.group(1)+f' id="section-{i[0]}">' if not i.__setitem__(0, i[0] + 1) else '', text)


if __name__=="__main__":
    main()