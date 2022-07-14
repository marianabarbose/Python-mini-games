print("Welcome to my Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Ok!Let's play!")
score = 0

answer = input("What was the first toy to be advertised on television? ")
if answer.lower() == "mr potato head from toy story":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("In what 1976 thriller does Robert De Niro famously say 'You talkin' to me?' ")
if answer.lower() == "taxi driver":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("For what movie did Steven Spielberg win his first Oscar for Best Director? ")
if answer.lower() == "schindler's list ":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3) * 100) + "%.")
