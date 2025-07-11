import random
targetNum = random.randint(1, 20)
print("Guess a number from 1 to 20")
def test(playerGuess):
    global targetNum
    if (playerGuess == targetNum):
        print("Your guess is correct")
        return True
    elif (playerGuess < targetNum):
        print("Your guess is too low")
        return False
    elif (playerGuess > targetNum):
        print("Your guess is too high")
        return False
while (True):
    playerGuess = 0
    try:
        playerGuess = int(input("Your number: "))
    except ValueError:
        print("Enter a valid number, pls")
        continue
    if (test(playerGuess)):
        break
    
        
    
    
    
