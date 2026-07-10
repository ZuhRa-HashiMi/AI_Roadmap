secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Too Low!")