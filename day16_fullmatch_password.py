import re

def main():
    text1 = "Password1!"         # True  
    text2 = "weakpass"           # False (no digit, no special, no uppercase)  
    text3 = "STRONG1!"           # False (no lowercase)  
    text4 = "Strong!"            # False (no digit)  
    text5 = "Strong1"            # False (no special)  
    text6 = "Str1!"              # False (too short)  
    text7 = "Valid123$"          # True  
    text8 = "GoodPass9@"         # True  
    text9 = "NoSpecial123"       # False  
    text10 = "C0mpl3x!"          # True  

    print(is_matched(text1))
    print(is_matched(text2))
    print(is_matched(text3))
    print(is_matched(text4))
    print(is_matched(text5))
    print(is_matched(text6))
    print(is_matched(text7))
    print(is_matched(text8))
    print(is_matched(text9))
    print(is_matched(text10))


def is_matched(text):

    return bool(re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}", text))

if __name__=="__main__":
    main()