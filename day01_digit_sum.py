from utils import clear_screen

def main():
    clear_screen()
    while True:
        try:
            digit = input("Input: ")
            if int(digit)<0:
                raise ValueError
            clear_screen()
            print(sum_validator(digit))
            break
        except ValueError:
            clear_screen()
            print("Invalid input. Please enter a positive integer.\n")            

def sum_validator(digit):
    digit_sum = 0
    digits = list(digit[:])
    for x in digits:
        digit_sum += int(x)

    if digit_sum%2==0:
        return f"Digit sum: {digit_sum}\nEven digit sum!"
    else:
        return f"Digit sum: {digit_sum}\nOdd digit sum!"

if __name__=="__main__":
    main()