# Nested Decisions: The Adventure Game

# Code Correction
# Buggy Code:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("you missed the hole there!")
    elif action == "proceed in the dark":
        print("wow that's odd i can't see anything passed the entrence!")