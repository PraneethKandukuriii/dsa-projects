import random

def get_winner(player, computer):

    outcomes = {
        ("rock","scissors"):"Player Wins!",
        ("scissors","rock"):"Player Wins!",
        ("rock","paper"):"Computer Wins!",
        ("paper","rock"):"Player Wins!",
        ("scissors","paper"):"Player Wins!",
        ("paper","scissors"):"Computer Wins!",
        ("rock","rock"):"It's a tie!",
        ("paper","paper"):"It's a tie!",
        ("scissors","scissors"):"It's a tie!"
    }


    if player == computer:
        return "It's a tie!"
    return outcomes.get((player, computer), "Invalid choice")


def play_game():

    choices = ['rock','paper','scissors']

    player_choice = input("Enter your choice:").lower()


    if player_choice not in choices:
        print("Invalid choice")
        return play_game()
    
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    result = get_winner(player_choice, computer_choice)
    print(result)


    replay = input("Do you want to play again? (yes/no):").lower()
    if replay == "yes":
        play_game()
    else:
        print("Thanks for playing!")



if __name__ == '__main__':
    play_game()










