import random

guess = 0
guess_history = []

secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Try to guess the secret number between 1 and 10.")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue 
    if guess < secret_number:
        print("Your guess is too low!")
        guess_history.append(guess)
        print("Your incorrect guesses so far:", guess_history)
    elif guess > secret_number:
        print("Your guess is too high!")
        guess_history.append(guess)
        print("Your incorrect guesses so far:", guess_history)
    else:
        print(f"Congratulations! You guessed the correct number: {secret_number}")
        print("\nHere is your full guess history:")
        for historic_guess in guess_history:
            print(historic_guess)
        break 