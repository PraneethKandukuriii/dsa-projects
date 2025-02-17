import random

# Board setup: Snakes and Ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move player
def move_player(player, position):
    dice_value = roll_dice()
    print(f"{player} rolled a {dice_value}")

    new_position = position + dice_value

    if new_position > 100:
        print("Can't move, need exact roll!")
        return position

    if new_position in snakes:
        print(f"Oh no! Bitten by a snake at {new_position} → {snakes[new_position]}")
        return snakes[new_position]

    if new_position in ladders:
        print(f"Yay! Climbed a ladder at {new_position} → {ladders[new_position]}")
        return ladders[new_position]

    return new_position

# Game loop
def play_game():
    while True:
        try:
            no_of_players = int(input("Enter the number of players (2-4): "))
            if 2 <= no_of_players <= 4:
                break
            else:
                print("Invalid input! Enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Get player names
    players = {}
    for i in range(1, no_of_players + 1):
        name = input(f"Enter the name of player {i}: ")
        players[name] = 0  # Start position at 0

    players_name = list(players.keys()) 
    turn_index = 0

    while True:
        turn = players_name[turn_index]
        print(f"\n{turn}'s Turn (Current Position: {players[turn]})")

        input("Press Enter to roll the dice...")

        new_position = move_player(turn, players[turn])
        players[turn] = new_position

        print(f"{turn} moved to {new_position}")

        if new_position == 100:
            print(f"\n🎉 {turn} WON THE GAME! 🎉")
            break

        # Switch turn
        turn_index = (turn_index + 1) % no_of_players

if __name__ == "__main__":
    play_game()


        
            
            