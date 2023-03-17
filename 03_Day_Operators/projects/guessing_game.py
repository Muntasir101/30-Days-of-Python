# Simple guessing game
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, you guessed the wrong number. The number was ", number)
