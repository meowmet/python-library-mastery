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


"""
import os
import random

# Setup function to create the game folders and files
def setup_game():
    if not os.path.exists("roulette_game"):
        os.makedirs("roulette_game")

    # Create 6 chambers (folders)
    for i in range(1, 7):
        chamber_path = f"roulette_game/chamber_{i}"
        os.makedirs(chamber_path, exist_ok=True)
        # Create a status.txt file inside each chamber
        with open(f"{chamber_path}/status.txt", "w") as f:
            f.write("Survived")

    # Randomly choose one chamber to place the bullet
    bullet_chamber = random.randint(1, 6)
    with open(f"roulette_game/chamber_{bullet_chamber}/status.txt", "w") as f:
        f.write("BANG! You lost!")

    print("Game setup complete! Time to play!\n")

# Game logic
def play_game():
    print("Welcome to Folder Russian Roulette!")
    print("There are 6 chambers (folders), one of them contains the bullet.")
    print("Choose a chamber (folder) and open the status.txt file to see if you survived.\n")
    
    # Player gets 6 chances, but the goal is to survive!
    chances = 6
    while chances > 0:
        chamber_choice = input("Pick a chamber (1-6): ")
        if chamber_choice.isdigit() and 1 <= int(chamber_choice) <= 6:
            chamber_choice = int(chamber_choice)
            chamber_path = f"roulette_game/chamber_{chamber_choice}"
            
            # Open the status.txt file to check the result
            with open(f"{chamber_path}/status.txt", "r") as file:
                result = file.read().strip()
                
            print(f"\nYou opened chamber {chamber_choice}...\n")
            
            if result == "BANG! You lost!":
                print(f"*BANG!* You fired the bullet. GAME OVER.\n")
                break
            else:
                print(f"*Click!* You survived this round! ({chances - 1} chances left)\n")
                chances -= 1
        else:
            print("Invalid chamber choice. Please choose a number between 1 and 6.\n")
        
        if chances == 0:
            print("Congratulations! You survived all the chambers and won the game!")

# Setup the game
setup_game()

# Start the game
play_game()

"""