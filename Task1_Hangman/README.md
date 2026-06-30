# Task 1 - Hangman Game

## Overview

This project is developed as part of the **CodeAlpha Python Programming Internship**.

The Hangman Game is a console-based Python application that randomly selects a word from a predefined list of five words. The player guesses one letter at a time to reveal the hidden word and has a maximum of six incorrect attempts to complete the game.

## Features

- Random word selection using the `random` module
- Five predefined words
- Maximum of six incorrect guesses
- Displays the current progress after each guess
- Validates user input
- Prevents duplicate letter guesses
- Displays appropriate win and game over messages
- Console-based implementation

## Programming Language

- Python

## Python Concepts Used

- Random Module
- Lists
- Strings
- While Loop
- For Loop
- If-Else Statements
- User Input
- Conditional Logic

## Project Structure

```
Task1_Hangman/
├── main.py
└── README.md
```

## How to Run

1. Ensure Python 3 is installed on your system.
2. Navigate to the `Task1_Hangman` folder.
3. Run the following command:

```bash
python main.py
```

## How It Works
- A random word is selected from a predefined list
- The user guesses one letter at a time
- Correct guesses reveal letters in the word
- Incorrect guesses reduce remaining attempts
- The game ends when the word is guessed or attempts reach zero

## Sample Output

```text
===================================
       HANGMAN GAME
===================================
Guess the hidden word!
You have 6 incorrect attempts.

Word: _ _ _ _ _ _ _
Attempts Left: 6
Enter a letter: e
Correct!

Word: _ _ _ e _ _ e
Attempts Left: 6
Enter a letter: t
Incorrect!

Word: _ _ _ e _ _ e
Attempts Left: 5
Enter a letter: s
Correct!

Word: s _ _ e _ _ e
Attempts Left: 5
Enter a letter: c
Correct!

Word: s c _ e _ c e
Attempts Left: 5
Enter a letter: i
Correct!

Word: s c i e _ c e
Attempts Left: 5
Enter a letter: n
Correct!

Word: s c i e n c e
Attempts Left: 5

Congratulations!
You guessed the word: science

Thank you for playing!
```

## Author

**Yogashri R**

## Future Enhancements
- Add multiple difficulty levels (Easy, Medium, Hard) by varying word complexity and attempts  
- Expand the word database or integrate an external dictionary API for dynamic word selection  
- Implement a graphical user interface (GUI) using Tkinter or PyQt for better user experience  
- Add a scoring system based on number of attempts and time taken  
- Include a hint system to assist users after a certain number of wrong attempts

