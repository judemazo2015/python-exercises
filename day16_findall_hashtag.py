import re

def main():
     text = "Loving the #sunset and #beach_vibes123! But not #, or #!! or #🔥fire."
     print(matched_items(text))

def matched_items(text):

    return re.findall(r'#[a-zA-Z][\w_]*', text)

if __name__=="__main__":
    main()