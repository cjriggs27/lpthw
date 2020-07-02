from sys import exit


def welcome_home():
    print("Welcome home!")
    print("You just walked through the door.")
    print("What shall we do first? Make some food or go to your room?")

    choice = input("> ")

    if "my room" in choice:
        print("You walk into your room and lay on your bed.")
        print("Do you turn on the tv or start working on your python projects?")
        choice = input("> ")

        if "tv" in choice:
            print("You turn on your tv and start watching your new favorite show! Enjoy!")
        elif "python" in choice:
            print("You open your laptop and start working on a new python project! How exciting!")
        else:
            print("You stand in the door way unable to make a decision until you fall asleep. Good job!")
    elif "food" or "kitchen" in choice:
        print("You walk into the ktchen and make your favorite meal! Good job!")

    else:
        print("Maybe you should eat! its been a long day!")

welcome_home()
