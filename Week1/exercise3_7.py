# Random character
import time
currentTime = time.time() # Get current time
milliseconds = currentTime - int(currentTime) # Get milliseconds
randomNumber =  int(milliseconds * 100) # Get random two-digit number
print(randomNumber)
while (randomNumber < 65): # format number to uppercase letter ASCII range
	randomNumber = randomNumber + 65
while (randomNumber > 90):
	randomNumber = randomNumber - 7
letter = chr(randomNumber) # convert current second to ASCII letter
print(letter)