import re

def main():
     text = "Dates: 2024-06-25, 1999-12-31, 2100-01-01, 2023-00-10, and 2022-13-01"
     print(matched_items(text))

def matched_items(text):
    return re.findall(r"\b(?:19[0-9][0-9]|20[0-9][0-9])-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])\b", text)

if __name__=="__main__":
    main()