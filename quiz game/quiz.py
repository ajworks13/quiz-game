print("\n\n\n\nWelcome to my computer quiz mang!")

playing = input("Do you wnat to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! lets play :) ")
score = 0

answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1

else:
    print("Incorrect!")

answer = input("\nWhat does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1

else:
    print("Incorrect!")

answer = input("\nWhat does PSU stand for? ")
if answer.lower() == "Power supply":
    print("Correct! ")
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + "%.")
