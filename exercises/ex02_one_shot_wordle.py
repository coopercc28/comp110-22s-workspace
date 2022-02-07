"""Ex02 - Wordle."""

__author__ = "730394353"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
printed_box: str = ""
i: int = 0
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        printed_box = printed_box + green_box
    else:
        character: bool = False
        alternate_indices: int = 0
        while not character and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == guess[i]:
                printed_box = printed_box + yellow_box
                character = True 
            alternate_indices = alternate_indices + 1
        if not character:
            printed_box = printed_box + white_box
    i = i + 1 
print(printed_box)
if guess != secret_word:
    print("Not quite. Play again soon!")
if guess == secret_word:
    print("Woo! You got it!")
