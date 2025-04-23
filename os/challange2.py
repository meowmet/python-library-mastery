# Folder Russian Roulette – You Win if You Survive!
# 🎯 Your Mission:
# You will navigate between folders, and each folder represents a chamber.

# Inside each folder, there will be a status.txt file.

# If you survive, it will say: "You survived!".

# If you pick the folder with the bullet, it will say: "BANG! You lost!".

# Game Flow:
# You have 6 chambers (folders).

# One folder randomly has the bullet, and if you pick that folder, you lose.

# If you survive by not picking the folder with the bullet, you win!

# Updated Code for Folder Russian Roulette (with Winning Condition):

import random

def select_level():
    print("Select difficulty level:")
    print("1 - Easy (3 bullets, 9 empty)")
    print("2 - Normal (6 bullets, 6 empty)")
    print("3 - Hard (9 bullets, 9 empty)")

    while True:
        choice = input("Enter level (1-3): ")
        if choice in ["1", "2", "3"]:
            levels = {"1": (3, 9), "2": (6, 6), "3": (9, 9)}
            return levels[choice]
        else:
            print("Invalid choice. Try again.")

def setup_chambers(bullets, empties):
    chambers = ["BANG!"] * bullets + ["Click!"] * empties
    random.shuffle(chambers)
    return chambers

def machine_turn(chambers, used_indices):
    while True:
        index = random.randint(0, len(chambers) - 1)
        if index not in used_indices:
            used_indices.add(index)
            print("\nMachine pulls the trigger at you...")
            result = chambers[index]
            if result == "BANG!":
                print("💥 Machine hit you! You lost 1 heart.")
                return -1, True
            else:
                print("🤖 Machine missed!")
                return 0, True

def player_turn(chambers, used_indices):
    while True:
        print("\nYour turn!")
        print("1 - Shoot yourself")
        print("2 - Shoot the machine")
        choice = input("Choose (1/2): ")

        if choice not in ["1", "2"]:
            print("Invalid choice.")
            continue

        while True:
            index = random.randint(0, len(chambers) - 1)
            if index not in used_indices:
                used_indices.add(index)
                break

        result = chambers[index]
        print(f"\nYou pulled the trigger... {result}")

        if choice == "1":  # Shoot yourself
            if result == "BANG!":
                print("💥 You shot yourself! -1 heart.")
                return -1, True, 0
            else:
                print("😅 Lucky! You survived. +2 points.")
                return 0, False, 2
        else:  # Shoot machine
            if result == "BANG!":
                print("🎯 Direct hit! +2 points.")
                return 0, False, 2
            else:
                print("😬 Missed the machine.")
                return 0, True, 0

def play_game():
    bullets, empties = select_level()
    chambers = setup_chambers(bullets, empties)
    used_indices = set()

    hearts = 3
    points = 0
    turn = "player"

    while hearts > 0 and len(used_indices) < len(chambers):
        if turn == "player":
            heart_change, switch_turn, point_gain = player_turn(chambers, used_indices)
            hearts += heart_change
            points += point_gain
            if switch_turn:
                turn = "machine"
        else:
            heart_change, switch_turn = machine_turn(chambers, used_indices)
            hearts += heart_change
            if hearts <= 0:
                break
            if switch_turn:
                turn = "player"

        print(f"\n[Status] Hearts: {hearts} | Points: {points} | Remaining chambers: {len(chambers) - len(used_indices)}")

    print("\n=== GAME OVER ===")
    if hearts <= 0:
        print("You lost all your hearts. Better luck next time!")
    else:
        print("You survived all chambers!")
    print(f"Final Score: {points}")

if __name__ == "__main__":
    play_game()