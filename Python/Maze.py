import os
import time

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Maze layout (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Start and end coordinates
start = [0, 0]
end = [4, 4]

# Player's current position
player = start.copy()

# Display the maze (P = player, E = end)
def print_maze():
    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[i])):
            if [i, j] == player:
                row += "P "
            elif [i, j] == end:
                row += "E "
            elif maze[i][j] == 1:
                row += "# "
            else:
                row += ". "
        print(row)
    print()

# Show welcome message
clear_screen()
print("======================================")
print("         🌀 TEXT MAZE GAME 🌀")
print("======================================")
print("Welcome, player!")
print("Your goal is to move from 'P' (start) to 'E' (exit).")
print("Avoid walls marked with '#', and stay inside the maze.")
print()
print("Commands you can use:")
print(" - north : move up")
print(" - south : move down")
print(" - east  : move right")
print(" - west  : move left")
print()
print("Good luck! Let's begin!")
print("======================================\n")
time.sleep(3)  # Wait 3 seconds before starting

while True:
    clear_screen()
    print_maze()
    move = input("Your move: ").strip().lower()

    # Save old position before moving
    old_position = player.copy()

    if move == "north":
        player[0] -= 1
    elif move == "south":
        player[0] += 1
    elif move == "east":
        player[1] += 1
    elif move == "west":
        player[1] -= 1
    else:
        print("❌ Invalid command. Try again.")
        time.sleep(1.5)
        continue

    # Check for boundaries or wall collision
    if (player[0] < 0 or player[0] >= len(maze) or
        player[1] < 0 or player[1] >= len(maze[0]) or
        maze[player[0]][player[1]] == 1):
        print("💥 You hit a wall! Try again.")
        player = old_position
        time.sleep(1.5)
        continue

    # Check for winning condition
    if player == end:
        clear_screen()
        print_maze()
        print("🏆 Congratulations! You reached the exit!")
        time.sleep(2)
        break
