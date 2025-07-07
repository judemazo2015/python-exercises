import re

def main():
    text = "These variables are user_id, account_number, and max_value_limit."
    print(subbed(text))

def subbed(text):

    return re.sub(r'([a-zA-Z]+)((?:_[a-zA-Z]+)+)',lambda m: f'{m.group(1)}{"".join(word.title() for word in m.group(2).split("_"))}', text)


if __name__=="__main__":
    main()