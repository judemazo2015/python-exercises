import re

def main():
    text = "This is **bold**, and so is **important text**, but not *italic*."
    print(subbed(text))

def subbed(text):
    return re.sub(r"\*\*(.*?)\*\*",r"<strong>\1</strong>", text)

if __name__=="__main__":
    main()