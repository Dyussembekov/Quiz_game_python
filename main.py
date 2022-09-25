print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("How to say hello in spanish? ")
if answer.lower() == "hola":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Where is Spain? ")
if answer.lower() == "europe":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("In free fall, a body is moving? ")
if answer.lower() == "uniformly accelerated":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The text is written in blue letters on a white background. When viewed through red glass, the letters will appear? ")
if answer.lower() == "dark":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")