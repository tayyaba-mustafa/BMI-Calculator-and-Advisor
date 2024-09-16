print("Welcome to Number Guessing Game!")

play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()
print("-" * 80)

print("Lets play!")

# Generate a random number between 1 and 100
import random
secret_number = random.randint(1, 100)

# Get the user's initial guess
Guess = int(input("I'm thinking of a number between 1 and 100. What's your guess? "))

#Guess count
guess_count = 0
#Guess limit
guess_limit = 5

# Keep prompting the user until they guess correctly or reach the limit
while Guess != secret_number and guess_count < guess_limit - 1:
    if Guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    Guess = int(input("Try again: "))
    guess_count += 1

print("-" * 80)

# Check if the user guessed correctly or reached the limit
if Guess == secret_number:
    print(f"Congratulations! You guessed the number in ",guess_count+1,"attempts.")
else:
    print(f"Sorry, you ran out of guesses.The secret number was {secret_number}.")


