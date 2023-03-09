winnerNumber = 9

winnerFlag = False
i = 0
while i < 3:
    guessNumber = int(input("Guess:"))
    if guessNumber == winnerNumber:
        winnerFlag = True
        break
    i += 1

if winnerFlag:
    print("You win!")
else:
    print("You loose!!")


