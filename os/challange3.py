# Aha, so you want to **play** a game in the terminal where you have to **navigate between folders** (rooms) and can't just jump to any room? Got it! This is going to be a **text-based adventure game** where folders are your rooms, and you need to interact with files to move forward. Let’s create something **fun** but simple for your terminal!
#
# ---
#
# 🎮 **Folder Escape Game – Terminal Adventure**
#
# #### 🎯 Your Mission:
#
# - You will start in the `dungeon` folder, and you can **only navigate** between rooms (folders) by interacting with the **clue files** and **unlocking rooms** one at a time.
#
# ### **How It Works:**
# 1. **Create your folders and files** as before:
#    - `dungeon/room_1/clue.txt`
#    - `dungeon/room_2/clue.txt`
#    - `dungeon/room_3/sword.txt`
#
# 2. **Game Flow**:
#    - You’ll start in **room 1** and have to read the `clue.txt` to know where to go next.
#    - After reading the clue, you **move** to the next room and repeat until you find the **sword** and escape.
#
# ### **Example Interaction (what you will type and see)**:
#
# ---
#
# **1. Start at room 1**:
# - Your starting point is `dungeon/room_1`. You can list the files there using `os.listdir()`. You should see `clue.txt`.
#
# ```
# You are in room 1.
# Files here: clue.txt
# What do you do? (read clue.txt to proceed)
# > cat clue.txt
# ```
#
# **Content of `clue.txt`**: 
# ```
# The key to escaping lies beyond room 2...
# ```
#
# Now, you know that **room 2** holds the next clue. You can move to it.
#
# ---
#
# **2. Move to room 2**:
# - You need to go to **room_2** and read `clue.txt`.
#
# ```
# You are in room 2.
# Files here: clue.txt
# What do you do? (read clue.txt to proceed)
# > cat clue.txt
# ```
#
# **Content of `clue.txt`**:
# ```
# You need to find the sword in room 3 to proceed!
# ```
#
# After this, you know that **room 3** is the final step.
#
# ---
#
# **3. Move to room 3**:
# - In room 3, you will find the **sword** file.
#
# ```
# You are in room 3.
# Files here: sword.txt
# What do you do? (read sword.txt to proceed)
# > cat sword.txt
# ```
#
# **Content of `sword.txt`**:
# ```
# Congratulations! You've found the sword! Now, you can escape.
# ```
#
# After reading the final file, you’ve **escaped the dungeon**! 🎉
#
# ---
#
# ### 🧠 How To Create It in Code:
#
# 1. **Create folders** and **files**:
#    - You can write a script that sets up the entire dungeon and its rooms.
#    
# 2. **Interaction with the terminal**:
#    - You can simulate a terminal interaction with basic `os` operations, like `os.listdir()` and `open()` to read files.
#
# ### 🧰 **Code Setup for the Game**:
#
# 
# 
# ---
#
# ### 🧠 What’s happening:
# - The **`setup_dungeon()`** function creates the folders and files.
# - The **`start_game()`** function handles your interaction in each "room" (folder), moving through the dungeon based on the text you read from the clue files.
#
# ### 🎉 How To Play:
# 1. Run the script, and you'll interact with the game in the terminal.
# 2. Navigate from room to room by reading the clues in the text files.
#
# ---
#
# This is **a more interactive and engaging folder-based game**. You can expand this with more rooms, different items, and even puzzles! 🎮 Let me know if you want to add more features or challenges to this adventure.












import os
#


def setup_dungeon():

    os.makedirs("dungeon/room_1", exist_ok=True)
    os.makedirs("dungeon/room_2", exist_ok=True)
    os.makedirs("dungeon/room_3", exist_ok=True)
    

    with open("dungeon/room_1/clue.txt", "w") as f:
        f.write("The key to escaping lies beyond room 2...")
        

    with open("dungeon/room_2/clue.txt", "w") as f:
        f.write("You need to find the sword in room 3 to proceed!")
        
   
    with open("dungeon/room_3/sword.txt", "w") as f:
        f.write("Congratulations! You've found the sword! Now, you can escape.")
    
   
    

def start_game():
    print("You are in room 1.")
    while True:
        print("\nFiles here:", os.listdir("dungeon/room_1"))
        action = input("What do you do? (read clue.txt to proceed): ")
        
        if action == "cat clue.txt":
            print("\nThe key to escaping lies beyond room 2...")
            print("\nYou move to room 2.")
            print("\nYou are in room 2.")
            
            while True:
                print("\nFiles here:", os.listdir("dungeon/room_2"))
                action = input("What do you do? (read clue.txt to proceed): ")
                
                if action == "cat clue.txt":
                    print("\nYou need to find the sword in room 3 to proceed!")
                    print("\nYou move to room 3.")
                    print("\nYou are in room 3.")
                    
                    while True:
                        print("\nFiles here:", os.listdir("dungeon/room_3"))
                        action = input("What do you do? (read sword.txt to proceed): ")
                        
                        if action == "cat sword.txt":
                            print("\nCongratulations! You've found the sword! Now, you can escape.")
                            return
                        else:
                            print("Invalid action. Try again.")
        else:
            print("Invalid action. Try again.(try 'cat' command to read the text file)")


setup_dungeon()
start_game()

