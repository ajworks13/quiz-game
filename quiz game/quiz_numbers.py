import random  # module created by people

# r = random.randint(0, 11) # includes 11 with randint
# random.randrange(-5, 11)  # up to 10

print("\n\n")

top_of_range = input("Type a number: ")

# returns true if its a number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0
print(random_number)

while True:
    guesses += 1
    user_guess = input("\nMake a guess: ")
    if user_guess.lower() == "q":
        quit()

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.")
        continue  # goes back up to top of loop with continue.

    if user_guess == random_number:
        print("You got it! ")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

# not necesary to do spaces with commas
print("You got it in", guesses, "guesses")
