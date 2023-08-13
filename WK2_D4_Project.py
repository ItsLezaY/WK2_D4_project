import random

def get_user_choice():
    print("\nChoose: rock, paper, scissors, or quit")
    choice = input().lower()
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_name):
    print(f"Welcome, {player_name}, let's start the game!\n")

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            break
        
        computer_choice = get_computer_choice()

        print(f"\t{player_name} chose: \n{user_choice}")
        print(f"\tComputer chose: \n{computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
    
    print(f"\nThank you for playing, {player_name}!")

player_name = input("\nEnter your name: ") # added a player name feature =)

play_game(player_name)