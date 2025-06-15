from utils import clear_screen
import re

def main():
    clear_screen()
    text = input("Input: ")
    print(is_palindrome(text.lower()))

def is_palindrome(text):
    text_list = re.findall(r"\w+",text)
    combined_text = "".join(text_list)
    reversed_text = combined_text[::-1]
    
    if combined_text == reversed_text:
        return "Palindrome!"
    else:
        return "Not a palindrome."

if __name__ == "__main__":
    main()