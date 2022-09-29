print("Welcome to my computer quiz")
Playing = input("Do you want to play? ")

if Playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stands for?\n ")
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!!")
answer = input("Do you want to study?  \n")
if answer.lower() == "no":
    print("correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does RAM stands for?\n ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does CPU stands for? \n")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!!")

print("You got " + str(score) + " questions correct !")
print("You got " + str((score/4)*100) + "%")

