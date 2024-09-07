print("Welcome to computer quiz!")
play = input("Do you want to play?")
if play.lower() != "yes":
    quit()

print("Lets play!")
score = 0
ans = input("What dose RAM stands for? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Inorrect!")

ans = input("What dose ROM stands for? ")
if ans.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Inorrect!")

ans = input("What dose WWW stands for? ")
if ans.lower() == "world wide web":
    print("Correct!")
    score += 1
else:
    print("Inorrect!")

ans = input("What dose GPU stands for? ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Inorrect!")

ans = input("What dose PSU stands for? ")
if ans.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Inorrect!")

print("You got " + str(score) + " questions correct.")
print("You got " + str((score/5)*100) + " %")
