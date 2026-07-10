import random

secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 10.")

while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    
    if guess < 1 or guess > 10:
        print("please chose number between 1 and 10")
        continue
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Too Low!")