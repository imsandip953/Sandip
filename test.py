import random

def play_game():
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("You got it! 🌟")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_game()