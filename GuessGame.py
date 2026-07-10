secret_number = 7

while True:
    guess = int(input("Guess a number: "))

    if guess == secret_number:
        print("Correct!")
        break
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Too Low!")