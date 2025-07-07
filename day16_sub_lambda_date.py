import re

def main():
    text = "Events: 25/06/2025, 01/01/2000, and 9/9/1999 should become ISO format."
    print(subbed(text))

def subbed(text):
    return re.sub(r"(\d{1,2})/(\d{1,2})/(\d{4})",lambda x: f"{x.group(3)}-{int(x.group(2)):02d}-{int(x.group(1)):02d}", text)

if __name__=="__main__":
    main()