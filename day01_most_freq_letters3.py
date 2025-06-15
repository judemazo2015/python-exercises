from utils import clear_screen
from collections import Counter
import re

def main():
    clear_screen()
    letters = get_letters(text = input("Input: "))
    print(get_most_frequent(letters))

def get_letters(text):
    letters = re.findall(r"[a-z]", text.lower())
    return Counter(letters)

def get_most_frequent(letters):
    if not letters:
        return "No letters found."
    else:
        highest_freq = max(letters.values())
        total_letters = sum(letters.values())
        most_freq = [f"'{letter.upper()}'" for letter, count in letters.items() if count == highest_freq]
        most_freq.sort()
        output1 = f"Output:\nMost frequent letter(s): {'||'.join(most_freq)} ({highest_freq} times)"
        output2 = f"Total letters counted: {total_letters}"
        percentage = get_percentage(total_letters, letters)
        return f"{output1}\n{output2}\n\n{percentage}"

def get_percentage(total, letters):
    output_percentage =[]
    for letter, count in letters.items():
        output_percentage.append(
            f"{letter.upper()} appeared {count} {'time' if count == 1 else 'times'} - {(count/total)*100:.1f}%" 
        )
    return "\n".join(output_percentage)   

if __name__=="__main__":
    main()