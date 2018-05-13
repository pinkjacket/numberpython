import random

print("-------------------------------------")
print("          GUESS THE NUMBER")
print("-------------------------------------")
print()

number = random.randint(0, 100)
guess = -1

name = input("Name, please. ")
while guess != number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)

    if guess < number:
        print("{0} is too low, {1}.".format(guess, name))
    elif guess > number:
        print("{0} is too high, {1}.".format(guess, name))
    else:
        print("You win!")
