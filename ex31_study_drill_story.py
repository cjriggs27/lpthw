print("""Welcome to L.A.!
It's not as clean as you thought it would be but meh \\('')/
So you just finished eating at this little taco place and you
spot The Comedy Store across the street!""")
print("""You're faced with two choices:
1. You go in and check out the show.
2. You go back to your hotel with your girlfriend.""")

opportunity = input("> ")

if opportunity == "1":
    print("You walk into the store and wow! Everyone is there, Lee, Callen, D'elia, Schaub, Rogan, Vonn.")
    print("You hang at the bar and watch the show with your girlfriend and you two have a blast!")
    print("After the show you see an opportunity to approach Callen to ask for advice about a joke your writing")
    print("1. Approach him 2. Head back to your hotel with your girlfriend")

    approach = input("> ")

    if approach == "1":
        print("He loves your jokes! You swap emails and he tells you to keep in touch. You head back to the hotel and have an awesome nights sleep.")
    elif approach == "2":
        print("You head hope and have a wonderful night with your girlfriend recalling each of your favorite jokes!")
    else:
        print("You panic, unable to make a dicision you slip on a rouge ice cube and wake up in the back of the ambulance with your girlfriend and free tickets to the store for life! woo!")

elif opportunity == "2":
    print("You head back to your hotel and rent a hilarious comedy your both love.")

else:
    print("You can't make a decision. You look to your girlfriend for a good idea and you notice a man choking. You run to help the man and he coughs up the food and is so grateful that he writes you a check for $1,000,000,000 and we all live happily ever after.")
