from sys import exit

doors = ["gold", "blue", "penguin", "goldfish"]

def start():

    print("\nYou're in an enormous castle!")
    print("\nWow, how'd you manage that?")
    print(f"\nNo matter, you look toward the end of the hall on your right and there is a bright {doors[1]} door.")
    print(f"\nTo your left you see a {doors[2]} door.")
    print(f"\nThat's weird. I don't think I've ever seen a {doors[2]} door before.")
    print("\nYou hear foot steps coming down the hall!")
    print("\nWhich door do you choose?")

    choice = input("> ")

    if f"{doors[2]}" in choice:
        pie_room()
    elif f"{doors[1]}" in choice:
        knight_room()
    elif "nothing" and "wait" in choice:
        print("\nThe gaurds have found you!")
        print("\nYou dash out the door and run back to your tour group! That was a close one phew..")
        exit(0)
    else:
        print("\nWell, I'm not really sure what to do with that response... ")
        print("\nJust pick a door!")
        start()

def pie_room():
    print("\nWow! This room is overflowing with pie!")
    print("\nThey have every flavor you can think of")
    print("\nWhat flavor is your favorite?")

    choice = input("> ")

    if "cherry" or "apple" or "blueberry" or "strawberry" in choice:
        print(f"\nWow that looks delicious! You grab your {choice} pie and start stuffing your face. Good job!")
        exit(0)
    elif "cherry" or "apple" or "blueberry" or "strawberry" not in choice:
        print(f"\nYou grab your gross {choice} pie and start stuffing your face. Gross.")
        exit(0)
    else:
        print(f"I'm not sure how, but I think that was a time traveling {choice} pie!")
        print("(You're transported back to the main hall of the enormous castle)")
        start()

def knight_room():
    print("\nYou walk into the room and there is a big towering knight standing in front of the king's gold.")
    print("\nWhat do you do?")
    knight_moved = False

    while True:
            choice = input("> ")

            if "taunt" in choice:
                print("\nThe Knight doesnt find you funny")
                print("\nHe escorts you out of the castle. Bummer.")
                exit(0)
            elif "talk" in choice and not knight_moved:
                print("\nThe knight appreciates your conversation and trusts you to watch the kings gold alone. That was easy!")
                knight_moved = True
            elif "take" in choice and knight_moved:
                print("\nYou take the gold and magically become king. Weird how that works.")
                print("\nGreat job!")
                exit(0)
            elif "fight" and "attack" in choice:
                print("\nThe knight laughs and cuts your head off. Great job!")
                exit(0)
            else:
                print("\nWell, you just made it awkward..")
                start()

start()
