import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

for guessTaken in range(1, 7):
    print("Take a guess.")
    user_guess = int(input())

    if user_guess < secret_number:
        print("Your guess is too low.")
    elif user_guess > secret_number:
        print("Your guess is too high.")
    else:
        break

    if user_guess == secret_number:
        print("Good job! You guessed my number in" + str(guessTaken) + 'guesses!')
    else:
        print("Nope. The number I was thinking of was " + str(secret_number))
