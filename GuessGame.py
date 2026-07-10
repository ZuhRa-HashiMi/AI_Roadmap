secret_number = 7
guess = int(input("Guess a number: "))
print(f"You guessed {guess}")

if guess == secret_number:
    print("Correct!")
elif guess > secret_number:
    print("Too Hight!")
else:
    print("Too Low!")
