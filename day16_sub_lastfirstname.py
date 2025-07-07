import re

def main():
    text = "Guests: Smith, John; Doe, Jane; Dela Cruz, Maria."
    print(replace_words(text))

def replace_words(text):
    return re.sub(r"([a-zA-Z ]+), ([a-zA-Z]+)",r" \2 \1", text)

if __name__=="__main__":
    main()