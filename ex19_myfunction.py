def switch_games(switch_games_I_want, switch_games_I_have):
    print("I just bought a nintendo switch!")
    print(f"There are {switch_games_I_want} games that I want right now")
    print(f"When I bought my switch it came with {switch_games_I_have}!")
    print("I can't wait to play them all!")
    print("The switch is so fun!!! \n")

print("\nThere are are many different ways you can write a function! Here are 10:\n")

#1 -------------------------------------------------
print("1. Give functions numbers directly:\n")

switch_games(10, 2)

#2 ------------------------------------------------
print("2. We can use variables:\n")

I_want_em = 10
ones_I_have = 2

switch_games(I_want_em, ones_I_have)

#3 --------------------------------------------
print("3. We can do math inside:\n")

switch_games(5 + 5, 1 + 1)

#4 --------------------------------------------
print("4. We can use variables and math:\n")

switch_games(I_want_em, 1 + 1)

#5 --------------------------------------------
print("5. We can use user input:\n")

print("How many games do you have?", end=' ')
games_you_have = input()

print("How many games do you want??", end=' ')
games_you_want = input()
print("\n")
switch_games(games_you_want, games_you_have)

#6 --------------------------------------------
print("6. Using user input and math:\n")

switch_games(games_you_want, 1 + 1)

#7 -------------------------------------------
#redundant? I'm assigning a user input to the variable games_you_want already so is it technically just to variables in the end?
print("7. Using user input and variables:\n")

switch_games(games_you_want, ones_I_have)

#8 -------------------------------------------
print("8. Maybe I can use f {} references???:\n")

switch_games(f"{I_want_em}", f"{ones_I_have}")

print("Success!!!!")

#9 ------------------------------------------
print("9. Running out of ideas here. Math and f{} references:\n")

switch_games(f"{I_want_em}", 1 + 1)

#10 ----------------------------------------
print("10. You saw it coming. User input and f{} references:\n")

switch_games(games_you_want, f"{ones_I_have}")
