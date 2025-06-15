from utils import clear_screen
import re

def main():
    clear_screen()
    letter_counts = get_letter_freq(text = input("Input: "))
    print(get_most_freq(letter_counts))


def get_letter_freq(text):
    char = ""
    count = 0
    score_board = []
    text = text.lower().strip()
    letters = re.findall(r"\w+",text)
    pure_text = "".join(letters)
    
    while pure_text:
        char = pure_text[0]
        for letter in pure_text:
            if char == letter:
                count+=1
        score_board.append([char,count])
        pure_text = pure_text.replace(char,"")
        count=0
    
    return score_board

def get_most_freq(letter_counts):
    highest_score = max(score[1] for score in letter_counts)
    list_winner_letters = [letter[0] for letter in letter_counts if letter[1]==highest_score]
    winner_letters = " ".join(list_winner_letters)
    
    return f"Output: Most frequent letter(s): {winner_letters} ({highest_score} times)"

if __name__=="__main__":
    main()