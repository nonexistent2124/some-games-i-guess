import random
words = [
    "apple", "bread", "crust", "dance", "eagle",
    "flake", "grape", "honey", "ivory", "jumps",
    "knife", "lemon", "mango", "nectar", "olive",
    "pearl", "quilt", "rocky", "sweet", "tiger",
    "usher", "vivid", "whale", "yeast","zebra",
    "abode", "blush", "chair", "dream", "audio"
    "event", "frost", "grain", "hilly", "ingot",
    "jolly", "knoll", "layer", "mirth", "niche",
    "ozone", "patch", "query", "rinse", "stone",
    "trend", "urban", "verve", "woven", "xerus",
    "yield", "zephyr", "azure", "binge", "crest",
    "dewey", "elfin", "forge", "gleam", "hover",
    "inset", "jiffy", "kneel", "latch", "mower",
    "nifty", "orbit", "pledge", "quirk", "roost",
    "swoop", "thrum", "usurp", "vigor", "wince",
    "x-ray", "youth", "zesty", "alley", "bloom",
    "cider", "dicey", "ember", "fable", "glint",
    "inner", "jumpy", "knack", "lemon", "mirth",
    "night", "outer", "peace", "quest", "rusty",
    "straw", "trust", "unity", "vixen"
]
word = random.choice(words)
letters = []
wrongLetters = []
print("Virtual hangman")
def guess():
    letter_guess = str(input("Guess a letter "))

    if len(letter_guess) > 1:
        print("1 character silly")
        exit(1)
    if letter_guess == "":
            print("A real letter")
            exit(1)
    else:
        if letter_guess in word:
            if letter_guess in letters:
                print("that letter is already correct")
                print("Letters wrong:", wrongLetters, "Letters correct:", letters)
                guess()
            else:
                print("yay you got a letter")
            letters.append(letter_guess)
            print("Letters wrong:", wrongLetters, "Letters correct:", letters)
            if len(letters) == 5:
                print("you won yay")
                print("the word was", word)
                exit(0)
            guess()
        elif letter_guess not in word:
            if letter_guess in wrongLetters:
                print("that letter is already wrong")
                print("Letters wrong:", wrongLetters, "Letters correct:", letters)
                guess()
            else:
                print("try again")
                wrongLetters.append(letter_guess)
                print("Letters wrong:", wrongLetters, "Letters correct:", letters)
                print(letters)
                guess()


guess()