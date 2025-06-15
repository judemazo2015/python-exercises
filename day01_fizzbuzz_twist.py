from utils import clear_screen

def main():
    clear_screen()
    number = input ("Enter an integer: ")
    fizzbuzz_twist(int(number))

def fizzbuzz_twist(n):
    for i in range(1,n+1):
        prime = is_prime(i)
        if i%3 == 0:
            print("Fizz ", end="")
            print("(prime)" if prime else "")
        elif i%5 == 0:
            print("Buzz ", end="")
            print("(prime)" if prime else "")
        else:
            print(f"{i} ", end="")
            print("(prime)" if prime else "")

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False    
    if x!=1:
        return True
    else:
        return False

if __name__=="__main__":
    main()