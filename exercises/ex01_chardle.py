"""EX01 - Chardle - A cute step towards wardle."""

__author__ = "730394353"

your_word: str = input("Enter a 5-character word: ")
if len(your_word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) > 1:
    print("Error: Character must be a single character ")
    exit()
print("Searching for " + single_character + " in " + your_word)
if single_character == your_word[0]:
    print(single_character + " found at index 0")
if single_character == your_word[1]:
    print(single_character + " found at index 1")
if single_character == your_word[2]:
    print(single_character + " found at index 2")
if single_character == your_word[3]:
    print(single_character + " found at index 3")
if single_character == your_word[4]:
    print(single_character + " found at index 4")
counter: int = 0
if single_character == your_word[0]:
    counter = counter + 1
if single_character == your_word[1]:
    counter = counter + 1
if single_character == your_word[2]:
    counter = counter + 1
if single_character == your_word[3]:
    counter = counter + 1
if single_character == your_word[4]:
    counter = counter + 1
if counter < int(1):
    print("No instances of " + single_character + " found in " + your_word)
if counter == int(1):
    print("1 instance of " + single_character + " found in " + your_word)
if counter == int(2):
    print("2 instances of " + single_character + " found in " + your_word)
if counter == int(3):
    print("3 instances of " + single_character + " found in " + your_word)
if counter == int(4):
    print("4 instances of " + single_character + " found in " + your_word)
if counter == int(5):
    print("5 instances of " + single_character + " found in " + your_word)
