import random


def guess_the_number():
   
    secret_number = random.randint(1, 100)

   
    guess_count = 0
    guessed_number = None

    print("Welcome to the Number Guessing Game!")

    while guessed_number != secret_number:
      
        try:
            guessed_number = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        
        guess_count += 1

        
        if guessed_number == secret_number:
            print(f"Congratulations! You guessed the correct number in {guess_count} attempts.")
        elif guessed_number < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_the_number()

