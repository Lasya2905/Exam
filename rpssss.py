import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Try again.")
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"
def play_rps():
    print("Let's play Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    for _ in range(3): 
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        print("-" * 20)
    print(" Game Over ")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")
play_rps()
