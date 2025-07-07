import re

def main():
    text = "My cards are 1234-5678-9012-3456 and 9876-5432-1098-7654."
    print(subbed(text))

def subbed(text):
    return re.sub(r"\b\d{4}-\d{4}-\d{4}-(\d{4})\b",r"****-****-****-\1", text)

if __name__=="__main__":
    main()