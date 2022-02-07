"""Ex03 - wordle."""

__author__ = "730394353"


def contains_char(any_word: str, single_character: str) -> bool:
    """Return True if character is in word, but False if it is not."""
    assert len(single_character) == 1
    i: int = 0
    while i < len(any_word):
        if single_character == any_word[i]:
            return True
            '# this will show that the character is in the word'
        i += 1
    return False
    '# this will show that the character is not in the word'


def emojified(guess: str, secret_word: str) -> str:
    """Return a string of emojis."""
    assert len(guess) == len(secret_word)
    white_emoji: str = "\U00002B1C"
    green_emoji: str = "\U0001F7E9"
    yellow_emoji: str = "\U0001F7E8"
    emoji_string: str = ""
    counter: int = 0
    while counter < len(secret_word):
        if guess[counter] == secret_word[counter]:
            emoji_string = emoji_string + green_emoji
        elif contains_char(secret_word, guess[counter]):
            emoji_string = emoji_string + yellow_emoji
        else:
            emoji_string = emoji_string + white_emoji
        counter += 1
    return emoji_string
    '# this will return a string of emojis based off the letters in the guess and the letters in the secret word'


def input_guess(expected_length: int) -> str:
    """To make sure the length of guess is length of secret word."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
    '# this makes sure that the guess is the right amount of characters'


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    i: int = 1
    guess: str = ""
    secret: str = "codes"
    while i <= 6 and guess != secret:
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {i}/6 turns!")
        i += 1
        '# will tell you that you won in i/6 amount of guesses'
    while i == 7:
        print("X/6 - Sorry, try again tomorrow!")
        i += 1
        '# will tell you to try again tomorrow if you get it wrong in all 6 tries'
    return None


if __name__ == "__main__":
    main()