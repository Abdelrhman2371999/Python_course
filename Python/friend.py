import random
import time
import os

# Ask user to input friends separated by commas
friends_input = input("Enter your friends' names, separated by commas: ")
friends = [name.strip() for name in friends_input.split(",") if name.strip()]

# Ask user how many times to show random friends
count = input("How many times do you want to pick a random friend? ")
if not count.isdigit() or int(count) <= 0:
    print("Invalid input. Using default value 5.")
    count = 5
else:
    count = int(count)

# Function to choose the next friend randomly
def next_friend(friends_list):
    return random.choice(friends_list)

# Show random friends 'count' times
for _ in range(count):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Next friend in the group...")
    time.sleep(1)
    friend = next_friend(friends)
    print(friend)
    time.sleep(1)

print("All random friends have been shown.")
input("Press Enter to exit.")