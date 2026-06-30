import random

words = ["python", "computer", "science", "college", "keyboard"]

word = random.choice(words)
guessed = []
tries = 6

print("=" * 35)
print("       HANGMAN GAME")
print("=" * 35)
print("Guess the hidden word!")
print("You have 6 incorrect attempts.")

while tries > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())
    print("Attempts Left:", tries)

    if "_" not in display:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        tries -= 1
        print("Incorrect!")

if tries == 0:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")
