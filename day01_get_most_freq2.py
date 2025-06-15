from utils import clear_screen
from collections import Counter
import re

def main():
    clear_screen()
    letter_counts = get_letter_freq(text=input("Input: "))
    print(get_most_freq(letter_counts))

def get_letter_freq(text):
    letters = re.findall(r"\w", text.lower())
    return Counter(letters)

def get_most_freq(letter_counts):
    highest_score = max(letter_counts.values())
    winners = [letter for letter, count in letter_counts.items() if count == highest_score]
    winner_letters = " ".join(winners)
    return f"Output: Most frequent letter(s): {winner_letters} ({highest_score} times)"

if __name__=="__main__":
    main()
