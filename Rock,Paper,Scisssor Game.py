print("Welcome to Rock,Paper,Scissor Game!")
print("-" * 80) 

import random
user_score = 0
computer_score = 0

#Generate the random choice for the computer
def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

#Determines the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
         return "You win!"
    else:
         return "Computer wins!"


while True:
    user_choice = input("Enter your choice (rock, paper,scissor or q): ").lower()
    # q for quit
    if user_choice == "q":
        break
    if user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        continue
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
        
print("-" * 80)       
print("Final scores:")
print(f"You win {user_score} times.")
print(f"Computer wins {computer_score} times.")
print("GoodBye!")

