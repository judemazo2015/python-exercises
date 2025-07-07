import re

def main():
    text1 = "00:00"      # True  
    text2 = "23:59"      # True  
    text3 = "12:30"      # True  
    text4 = "24:00"      # False  
    text5 = "12:60"      # False  
    text6 = "7:05"       # False (no leading zero)  
    text7 = "08:5"       # False (no leading zero)  
    text8 = "18:32"      # True  
    text9 = "03:07"      # True  
    text10 = "99:99"     # False  
 


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

    return bool(re.fullmatch(r"([0-1][0-9]|2[0-3]):[0-5][0-9]", text))

if __name__=="__main__":
    main()