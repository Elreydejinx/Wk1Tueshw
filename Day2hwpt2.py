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
if place == "jungle":
    pass # add this in later
    print("there are other places to go too")

#Quick Decisions: The Event Planner 

attendees = input("Enter number of attendees:")  

y = int(attendees)

x = int(attendees)

if y >= 100:
    print("large hall")
elif x <= 99:
    print("conference room")

 
  
# Catering Choices

Food = "vegetarian" 

if Food == "vegetarian":
    print("Veggie Delight Caterers? yes/no:")
if "yes":
    print("great lets eat!")
    if "no":
        print("steak")
elif Food == "steak":
        print("Gourmet Meals Caterers")